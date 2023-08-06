import glob
import gzip
import statistics
from collections import Counter, defaultdict
from itertools import chain, combinations, product

import pandas as pd
import pysam

from pipeline.drug.__init__ import __STEPS__
from pipeline.toolkits.report import reporter
from pipeline.toolkits.utils import check_dir, common_args, logit, format_int


def findall_mismatch(seq: str, n_mismatch: int, bases="ACGTN") -> list:
    """
    ## Description:
        choose locations where there's going to be a mismatch using combinations
    and then construct all satisfying lists using product.
    
    ## Parameters:
        seq (str): sequence.
        n_mismatch (int): maxium allowed mismatch num.
        bases (str): default "ACGTN".
        
    ## Return:
        seq_set (list): all mismatch sequence of the raw sequence.
        
    Example:
    >>> seq_set = seq.findall_mismatch("ACG")
    >>> seq_set == answer
    >>> answer = set(["TCG", "AAG", "ACC", "ATG", "ACT", "ACN", "GCG", "ANG", "ACA", "ACG", "CCG", "AGG", "NCG"])
    True
    """
    seq_set = set()
    seq_len = len(seq)
    if n_mismatch > seq_len:
        n_mismatch = seq_len
    for locs in combinations(range(seq_len), n_mismatch):
        seq_locs = [[base] for base in seq]
        for loc in locs:
            seq_locs[loc] = list(bases)
        for poss in product(*seq_locs):
            seq_set.add("".join(poss))
            
    seq_set = list(seq_set)
    return seq_set


def generate_seq_dict(seq_list: list, n_mismatch: int) -> dict:
    """
    ## Description:
        Generate barcode dictionary.
        
    ## Parameters:
        seq_list (list): str list, recording barcode information. 
        n_mismatch (int): maxium allowed mismatch num.
    
    ## Return:
        seq_dict: {mismatch_seq: raw_seq}      
    """

    seq_dict = {}
    for bc in seq_list:
        mismatch_seqs = findall_mismatch(bc, n_mismatch)
        for i in mismatch_seqs:
            seq_dict[i] = bc
    return seq_dict
    
    
def correct_seq(error_seq: str, seq_dict: dict) -> str:
    """
    ## Description:
        Replace incorrect barcode sequence with right barcode.
        
    ## Parameters:
        error_seq (str): incorrect barcode sequence with mismatch base pairs.
        
    ## Return:
        raw_seq (str): correct barcode sequence.
    """
    raw_seq = seq_dict[error_seq]
    return raw_seq


def get_read(library_id, library_path, read='1'):
    read1_list = [f'_{read}', f'R{read}', f'R{read}_001']
    fq_list = ['fq', 'fastq']
    suffix_list = ["", ".gz"]
    read_pattern_list = [
        f'{library_path}/*{library_id}*{read}.{fq_str}{suffix}' 
        for read in read1_list 
        for fq_str in fq_list 
        for suffix in suffix_list
    ]
    fq_list = [glob.glob(read1_pattern) for read1_pattern in read_pattern_list]
    fq_list = sorted(non_empty for non_empty in fq_list if non_empty)
    fq_list = list(chain(*fq_list))
    if len(fq_list) == 0:
        print("Allowed R1 patterns:")
        for pattern in read_pattern_list:
            print(pattern)
        raise Exception(
            '\n'
            f'Invalid Read{read} path! \n'
            f'library_id: {library_id}\n'
            f'library_path: {library_path}\n'
        )
    return fq_list

    

class BARCODE:
    """
    ## Features: 
    - Extract the Barcode and UMI information in R1, and use it as the header of R2 read.
    - Filter barcode: Only one base mismatch is allowed at most, and the mismatched base must be a low-quality base.
        
    ## Arguments:
    - `fq1` R1 read path, required.
    - `fq2` R2 read path, required.
    - `barcode_list` Barcode file path. E.g. "barcode_name\tbarcode_seq". Required.
    - `barcode_range` Barcode range in the R1 read. Default: `1,10`.
    - `umi_range` UMI range in the R1 read. Default: `11,20`.
    - `min_qual` Minimum base quality in a barcode sequence. Default: `20`.
    - `gzip` Output fastq files in compressed format.

    ## Outputs:
    - `{sample}.fq(.gz)` R2 data with modified read header.
    - `stat.txt` Barcode summary.
    """
    def __init__(self, args, step):
        self.step = step
        # required parameters
        self.plate_tsv = args.plate_tsv
        self.sample = args.sample
        # default parameters
        self.outdir = args.outdir
        self.barcode_range = args.barcode_range.split(',')
        self.umi_range = args.umi_range.split(',')
        self.n_mismatch = 1
        self.min_qual = int(args.min_qual)
        self.gzip = args.gzip
        
        self.out_prefix = f'{self.outdir}/0{__STEPS__.index(self.step)}.{self.step}'
        
        
    @logit
    def parse_plate(self, barcode_tsv: str) -> dict:
        """
        ## Description:
            Parse barcode file and return a dict containning plate barcode info.
            
        ## Parameters:
            barcode_tsv (str): barcode file, 3 columns: Sample\tWell\tBarcode\tSmile.
            
        ## Return:
            barcode_dict (dict): barcode dict. Each barcode corresponds to a well on each plate.
        """
        df = pd.read_csv(filepath_or_buffer=barcode_tsv,
                        sep='\t',
                        header=0)
        df['Tag'] = df['Plate'].astype(str) + '-' + df['Well'].astype(str)
        sample_dict = df.to_dict('list')
        return sample_dict
        

    @logit
    def parse_fastq(self, plate_tsv: str) -> dict:
        """
        ## Description:
            Parse sample file and return a dict containning fastq path.
            
        ## Parameters:
            plate_tsv (str): sample file, 2 columns: Sample\tPath\tLibrary.
            
        ## Return:
            fastq_dict (dict): fastq file dict.
        """
        fastq_dict = defaultdict(dict)
        df = pd.read_csv(filepath_or_buffer=plate_tsv,
                        sep='\t',
                        header=0)
        df_dict = df.to_dict('list')
        for i in range(len(df_dict['Library'])):
            l = df_dict['Library'][i]
            p = df_dict['Path'][i]
            info = df_dict['Info'][i]
            f1 = get_read(library_id=l,
                          library_path=p,
                          read=1)
            f2 = get_read(library_id=l,
                          library_path=p,
                          read=2)
            if len(f1) != len(f2):
                raise Exception(f"{l} Read1 and Read2 fastq number do not match!")
            fastq_dict[l]['fq1']=f1
            fastq_dict[l]['fq2']=f2
            fastq_dict[l]['info'] = info
        
        return fastq_dict
          
          
    @logit    
    def run(self):
        # prepare
        barcode_range, umi_range = self.barcode_range, self.umi_range
        fastq_dict = self.parse_fastq(plate_tsv=self.plate_tsv)
        # output
        # check outdir
        check_dir(f'{self.out_prefix}')
        # store fastq file (gzip)
        if self.gzip:
            out_fq = gzip.open(f'{self.out_prefix}/{self.sample}.fq.gz', "wt")
        else:
            out_fq = open(f'{self.out_prefix}/{self.sample}.fq', "wt")
        # statement 
        # total reads
        # valid reads
        # mean reads per barcode
        # Q30 of Barcodes
        # Q30 of UMIs
        s = Counter()
        reads_counter = defaultdict(int)
        # process
        for f in fastq_dict:
            info = fastq_dict[f]['info']
            fq1 = fastq_dict[f]['fq1'][0]
            fq2 = fastq_dict[f]['fq2'][0]
            print(fq1, fq2)
            # parse barcode file
            plate_info = self.parse_plate(info)
            # generate barcode dict
            barcode_dict = generate_seq_dict(plate_info['Barcode'], self.n_mismatch)
            barcode2tag = {plate_info['Barcode'][i]: plate_info['Tag'][i] for i in range(len(plate_info['Barcode']))}      
            # use pysam to read fastq file
            f1, f2 = pysam.FastxFile(fq1), pysam.FastxFile(fq2)
            # performing reads
            for entry1, entry2 in zip(f1, f2):
                s['total_reads'] += 1
                tmp = s['total_reads']
                if tmp % 5000000 == 0:
                    BARCODE.run.logger.info(f'Processed {tmp} reads.')
                f1_seq = entry1.sequence
                f1_qual = entry1.quality
                barcode = f1_seq[int(barcode_range[0])-1:int(barcode_range[1])]
                bc_qual = f1_qual[int(barcode_range[0])-1:int(barcode_range[1])]
                umi = f1_seq[int(umi_range[0])-1:int(umi_range[1])]
                umi_qual = f1_qual[int(umi_range[0])-1:int(umi_range[1])]
                
                ### At most one base mismatch is allowed, and the base must be a low-quality base.
                # filter barcode:
                # 1. only barcode in the barcode dict is accepted.
                # 2. only one missmatch is allowed in the barcode.
                # 3. the missmatch base is a low quality base.
                if barcode in barcode_dict:
                    bc_qual = [ord(i)-33 for i in bc_qual]
                    bc_q30 = sum(bc_qual)/len(bc_qual)
                    diff_idx = [i for i in range(len(barcode)) if barcode[i]!=barcode_dict[barcode][i]]
                    umi_qual = [ord(i)-33 for i in umi_qual]
                    umi_q30 = sum(umi_qual)/len(umi_qual)
                    umi_pass = True
                    # filter UMI:
                    # Must not be a homopolymer, e.g. AAAAAAAAAA
                    # Must not contain N
                    # Must not contain bases with base quality < 10
                    if min(umi_qual)<10 or 'N' in umi or len(set(list(umi)))==1:
                        umi_pass = False
                    if diff_idx==[] and umi_pass==True:
                        
                        if bc_q30>=30:
                            s['barcode Q30'] += 1
                        if umi_q30>=30:
                            s['UMI Q30'] += 1
                    elif diff_idx!=[] and umi_pass==True:
                        if bc_qual[diff_idx[0]]<10:
                            if bc_q30>=30:
                                s['barcode Q30'] += 1   
                            if umi_q30>=30:
                                s['UMI Q30'] += 1                     
                        else:
                            continue
                    elif diff_idx!=[] and umi_pass==False:
                        continue
                    s['valid reads'] += 1
                    reads_counter[barcode2tag[barcode_dict[barcode]]] += 1
                    # write valid reads
                    new_head = f'@{barcode2tag[barcode_dict[barcode]]}_{umi}_{tmp}'
                    new_seq = f'{new_head}\n{entry2.sequence}\n+\n{entry2.quality}\n'  
                    out_fq.write(f'{new_seq}')      
        
        out_fq.close()
        
        reads_counter = sorted(reads_counter.items(), key = lambda i: -i[1])
                
        ### sum barcode step:
        barcode_summary = defaultdict()
        barcode_summary['Total reads:'] = format_int(s['total_reads'])
        valid_reads = s['valid reads']
        valid_reads_percent = round(valid_reads*100/s['total_reads'], 2)
        barcode_summary['Valid reads:'] = f'{format_int(valid_reads)} ({valid_reads_percent}%)'
        barcode_summary['Median read counts for barcode:'] = int(statistics.median([i[1] for i in reads_counter]))
        barcode_q30_reads = s['barcode Q30']
        barcode_q30_reads_percent = round(s['barcode Q30']*100/s['total_reads'], 2)
        barcode_summary['Barcodes Q30:'] = f'{format_int(barcode_q30_reads)} ({barcode_q30_reads_percent}%)'
        umi_q30_reads = s['UMI Q30']
        umi_q30_reads_percent = round(s['UMI Q30']*100/s['total_reads'], 2)
        barcode_summary['UMIs Q30:'] = f'{format_int(umi_q30_reads)} ({umi_q30_reads_percent}%)'
        barcode_summary = pd.DataFrame.from_dict(barcode_summary, orient="index")
        barcode_summary.to_csv(f'{self.out_prefix}/{self.sample}_summary.txt', sep='\t', header=False)

        barcode_plot = {'count_values': [i[1] for i in reads_counter],
                        'count_labels': [i[0] for i in reads_counter]}
        
        report = reporter(assay='drug',
                        name=self.step,
                        outdir=f'{self.outdir}',
                        sample=self.sample,
                        stat_file=f'{self.out_prefix}/{self.sample}_summary.txt',
                        plot=barcode_plot)
        report.get_report()

def barcode(args):
    step = "barcode"
    barcode_obj = BARCODE(args, step)
    barcode_obj.run()
    
    
def get_barcode_para(parser, optional=False):
    # parser.add_argument("--fq1", help="R1 read.", required=True)
    # parser.add_argument("--fq2", help="R2 read.", required=True)
    parser.add_argument("--plate_tsv", help="", 
                        required=True)
    parser.add_argument("--barcode_range", help="Barcode range in Read 1.",
                        default="1,10")
    parser.add_argument("--umi_range", help="UMI range in Read 1.", 
                        default="11,20")
    if optional:
        parser.add_argument("--gzip", help="Output gzip fastq file.", 
                            action="store_true")
        parser.add_argument("--min_qual", help="Min barcode base quality", 
                            default=10)
        parser = common_args(parser)
    
    return parser
