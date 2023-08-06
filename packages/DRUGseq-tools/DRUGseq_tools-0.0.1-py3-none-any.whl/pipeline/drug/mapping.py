import re
import subprocess

import pandas as pd

from pipeline.__init__ import RUN_THREADS
from pipeline.drug.__init__ import __STEPS__
from pipeline.toolkits import utils
from pipeline.toolkits.report import reporter


class MAPPING():
    """
    Features:
    - Mapping reads to genome and sort bam file.
    
    Arguments:
    - `fq`: Clean fastq file after trimming. Required.
    - `genomeDir` Genome index directory. Required.
    - `out_unmapped` Ouput unmapped reads. 
    - `outFilterMatchNmin` Alignment will be output only if the number of matched bases is higher than or equal to this value. Default `0`.
    - `outFilterMultimapNmax` Maximum number of loci the read is allowed to map to. Alignments (all of them) will be output only if the read maps to no more loci than this value. Otherwise no alignments will be output, and the read will be counted as "mapped to too many loci" in the Log.final.out. Default `1`.
    - `STAR_param` Other star parameters. Default `None`.
    
    Outputs:
    - `{sample}_Aligned.out.bam` Unsorted bam file.
    - `{sample}_Aligned.sortedByCoord.out.bam` Sorted bam file.
    - `{sample}_Log.final.out` STAR summary file.
    - `{sample}_Log.out` STAR log.
    - `{sample}_Log.progress.out` STAR log.
    - `{sample}_SJ.out.tab`
    - `summary.txt` Mapping summary file.
    """
    def __init__(self, step, args):
        self.step = step
        self.outdir = args.outdir
        self.sample = args.sample
        self.fq = args.clean_fq
        self.genomeDir = args.genomeDir
        self.out_unmapped = args.out_unmapped
        self.outFilterMatchNmin = int(args.outFilterMatchNmin)
        self.outFilterMultimapNmax = int(args.outFilterMultimapNmax)
        self.STAR_param = args.STAR_param
        self.thread = args.thread

        self.refflat = f"{self.genomeDir}/refFlat.txt"
        
        # parse
        self.stat_prefix = 'Reads'

        # out
        self.out_prefix = f'{self.outdir}/0{__STEPS__.index(self.step)}.{self.step}'
        self.starFilePrefix = f'{self.out_prefix}/{self.sample}_'

        self.STAR_map_log = f'{self.starFilePrefix}Log.final.out'
        self.unsort_STAR_bam = f'{self.starFilePrefix}Aligned.out.bam'
        self.STAR_bam = f'{self.starFilePrefix}Aligned.sortedByCoord.out.bam'
        
        self.picard_region_log = f'{self.starFilePrefix}region.log'
        
        self.stat_dict = {}
    
    @utils.logit
    def STAR(self):
        cmd = [
            'STAR',
            '--runThreadN', str(RUN_THREADS[self.step]),
            '--genomeDir', self.genomeDir,
            '--readFilesIn', self.fq,
            '--outFilterMultimapNmax', str(self.outFilterMultimapNmax),
            '--outFileNamePrefix', self.starFilePrefix,
            '--outSAMtype', 'BAM', 'Unsorted', # controls sort by Coordinate or not
            '--outFilterMatchNmin', str(self.outFilterMatchNmin)
        ]
        if self.out_unmapped:
            cmd += ['--outReadsUnmapped', 'Fastx']
        if self.fq[-3:] == ".gz":
            cmd += ['--readFilesCommand', 'zcat']
        cmd = ' '.join(cmd)
        if self.STAR_param != None:
            cmd += (" " + self.STAR_param)
        MAPPING.STAR.logger.info(cmd)
        subprocess.check_call(cmd, shell=True)
        
    @utils.logit
    def sort_bam(self):
        cmd = (
            f'samtools sort {self.unsort_STAR_bam} '
            f'-o {self.STAR_bam} '
            f'--threads {self.thread} '
        )
        MAPPING.sort_bam.logger.info(cmd)
        subprocess.check_call(cmd, shell=True)

    @utils.logit
    def index_bam(self):
        cmd = f"samtools index {self.STAR_bam}"
        MAPPING.index_bam.logger.info(cmd)
        subprocess.check_call(cmd, shell=True)
        
    @utils.logit 
    def picard(self):
        cmd = [
            'picard',
            '-Xmx20G',
            '-XX:ParallelGCThreads=4',
            'CollectRnaSeqMetrics',
            'I=%s' % (self.STAR_bam),
            'O=%s' % (self.picard_region_log),
            'REF_FLAT=%s' % (self.refflat),
            'STRAND=NONE',
            'VALIDATION_STRINGENCY=SILENT']
        cmd_str = ' '.join(cmd)
        MAPPING.picard.logger.info(cmd_str)
        subprocess.check_call(cmd_str, shell=True)        


    def gen_star_summary(self):
        """
        step metrics
        """

        with open(self.STAR_map_log, 'r') as map_log:
            # number amd percent
            unique_reads_list = []
            multi_reads_list = []
            for line in map_log:
                if line.strip() == '':
                    continue
                if re.search(r'Uniquely mapped reads', line):
                    unique_reads_list.append(line.strip().split()[-1])
                if re.search(r'of reads mapped to too many loci', line):
                    multi_reads_list.append(line.strip().split()[-1])
        unique_reads = int(unique_reads_list[0])
        unique_reads_fraction = unique_reads_list[1]
        multi_reads = int(multi_reads_list[0])
        multi_reads_fraction = multi_reads_list[1]

        self.stat_dict[f'Uniquely Mapped {self.stat_prefix}:'] = unique_reads
        self.stat_dict[f'Uniquely Mapped {self.stat_prefix} fraction:'] = unique_reads_fraction
        self.stat_dict[f'Multi-Mapped {self.stat_prefix}:'] = multi_reads
        self.stat_dict[f'Multi-Mapped {self.stat_prefix} fraction:'] = multi_reads_fraction
        
        self.picard()
        with open(self.picard_region_log, 'r') as picard_log:
            region_dict = {}
            for line in picard_log:
                if not line:
                    break
                if line.startswith('## METRICS CLASS'):
                    header = picard_log.readline().strip().split('\t')
                    data = picard_log.readline().strip().split('\t')
                    region_dict = dict(zip(header, data))
                    break
        
        total = float(region_dict['PF_ALIGNED_BASES'])
        exonic_regions = int(region_dict['UTR_BASES']) + \
            int(region_dict['CODING_BASES'])
        intronic_regions = int(region_dict['INTRONIC_BASES'])
        intergenic_regions = int(region_dict['INTERGENIC_BASES'])


        star_plot = {'region_labels': ['Exonic Regions', 'Intronic Regions', 'Intergenic Regions'],
                'region_values': [exonic_regions, intronic_regions, intergenic_regions]}   
        

        mappping_summary = pd.DataFrame.from_dict(self.stat_dict, orient="index")
        mappping_summary.to_csv(f'{self.out_prefix}/{self.sample}_summary.txt', sep='\t', header=False)

        report = reporter(assay='drug',
                        name=self.step,
                        outdir=f'{self.outdir}',
                        sample=self.sample,
                        stat_file=f'{self.out_prefix}/{self.sample}_summary.txt',
                        plot=star_plot)
        report.get_report()
        
    def run_star(self):
        self.STAR()
        self.sort_bam()
        self.index_bam()
        self.gen_star_summary()
        
def mapping(args):
    step = 'mapping'
    mapping_obj = MAPPING(step, args)
    mapping_obj.run_star()
    

def get_mapping_para(parser, optional=False):
    parser.add_argument('--clean_fq', help="Required. R2 fastq file.", required=True)
    parser.add_argument(
        '--genomeDir', 
        help='Required. Genome directory.'
    )
    if optional:
        parser.add_argument(
            '--outFilterMatchNmin', 
            help="""Default `0`. Alignment will be output only if the number of matched bases 
    is higher than or equal to this value.""", 
            default=0
        )
        parser.add_argument(
            '--out_unmapped', 
            help='Output unmapped reads', 
            action='store_true'
        )
        parser.add_argument('--STAR_param', help='Other STAR parameters', default=None)
        parser.add_argument(
            '--outFilterMultimapNmax', 
            help='Default `1`. How many places are allowed to match a read at most.', 
            default=1
        )
        
        parser = utils.common_args(parser)
    return parser