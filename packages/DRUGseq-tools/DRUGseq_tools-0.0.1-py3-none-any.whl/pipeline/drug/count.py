import gzip
import os
import shutil
from collections import defaultdict
from itertools import groupby

import pandas as pd
import pysam
from scipy import io, sparse

from pipeline.drug.__init__ import __STEPS__
from pipeline.toolkits import utils


class COUNT():
    """
    Features:
    - Count umi for each gene in each barcode.
    - Filter UMI: 
        1. Cannot contain 'N'.
        2. Cannot be a multimer, such as 'AAAAAAAAAA'.
        3. Cannot have base quality lower than 10.

    Arguments:
    - `bam` Featurecounts output bam file, containing gene info. Required.
    - `gtf` GTF file path. Required.

    Outputs:
    - `{sample}_count.tsv` UMI, read count raw file.
    - `{sample}_matrix.txt` Gene expression matrix.
    """
    def __init__(self, step, args):

        # init
        self.step = step
        self.sample = args.sample
        self.outdir = args.outdir

        # required parameters
        self.bam = args.bam
        self.gtf = args.gtf

        # default parameters
        self.out10X = args.out10X

        # output files
        self.outdir_prefix = f'{self.outdir}/0{__STEPS__.index(self.step)}.{self.step}'
        utils.check_dir(f'{self.outdir_prefix}')
        self.fileprefix = f'{self.outdir_prefix}/{self.sample}'
        self.count_detail_file = f'{self.fileprefix}_count.tsv'
        self.count_summary = f'{self.fileprefix}_metadata.txt'
        
        if self.out10X:
            self.tenX_out = f'{self.outdir_prefix}/10X_output'
            utils.check_dir(self.tenX_out)

    @staticmethod
    def correct_umi(umi_dict, percent=0.1):
        """
        Description: Correct umi_dict in place.
        
        Args:
            umi_dict: {umi_seq: umi_count}
            percent: if hamming_distance(low_seq, high_seq) == 1 and
                low_count / high_count < percent, merge low to high.
        Returns:
            n_corrected_umi: int
            n_corrected_read: int
        """
        n_corrected_umi = 0
        n_corrected_read = 0

        # sort by value(UMI count) first, then key(UMI sequence)
        umi_arr = sorted(
            umi_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        while True:
            # break when only highest in umi_arr
            if len(umi_arr) == 1:
                break
            umi_low = umi_arr.pop()
            low_seq = umi_low[0]
            low_count = umi_low[1]

            for umi_kv in umi_arr:
                high_seq = umi_kv[0]
                high_count = umi_kv[1]
                if float(low_count / high_count) > percent:
                    break
                if utils.hamming_distance(low_seq, high_seq) == 1:
                    n_low = umi_dict[low_seq]
                    n_corrected_umi += 1
                    n_corrected_read += n_low
                    # merge
                    umi_dict[high_seq] += n_low
                    del (umi_dict[low_seq])
                    break
        return n_corrected_umi, n_corrected_read

    @utils.logit
    def bam2table(self):
        """
        bam to detail table
        must be used on name_sorted bam
        """
        samfile = pysam.AlignmentFile(self.bam, "rb")
        with open(self.count_detail_file, 'wt') as fh1:
            fh1.write('\t'.join(['Barcode', 'geneID', 'UMI', 'count']) + '\n')

            def keyfunc(x):
                return x.query_name.split('_', 1)[0]
            for _, g in groupby(samfile, keyfunc):
                gene_umi_dict = defaultdict(lambda: defaultdict(int))
                for seg in g:
                    (barcode, umi) = seg.query_name.split('_')[:2]
                    if not seg.has_tag('XT'):
                        continue
                    gene_id = seg.get_tag('XT')
                    gene_umi_dict[gene_id][umi] += 1
                for gene_id in gene_umi_dict:
                    COUNT.correct_umi(gene_umi_dict[gene_id])

                # output
                for gene_id in gene_umi_dict:
                    for umi in gene_umi_dict[gene_id]:
                        fh1.write('%s\t%s\t%s\t%s\n' % (barcode, gene_id, umi,
                                                        gene_umi_dict[gene_id][umi]))
        samfile.close()

    @staticmethod
    def get_df_sum(df, col='UMI'):
        def num_gt2(x):
            return pd.Series.sum(x[x > 1])

        df_sum = df.groupby('Barcode', as_index=False).agg({
            'count': ['sum', num_gt2],
            'UMI': 'count',
            'geneID': 'nunique'
        })
        df_sum.columns = ['Barcode', 'readcount', 'UMI2', 'UMI', 'GeneCount']
        df_sum = df_sum.sort_values(col, ascending=False)
        return df_sum


    @utils.logit
    def write_matrix(self, df):
        # output count matrix and count summary
        df_UMI = df.groupby(['Barcode', 'geneID'],
                            as_index=False).agg({'UMI': 'count'})
        mtx = df_UMI.pivot(values='UMI',
                           columns='Barcode',
                           index='geneID',).fillna(0).astype(int)
        mtx.insert(0, 'gene_id', mtx.index)
        mtx.insert(0, 'gene_name', mtx['gene_id'].apply(
            lambda x: self.id_name[x]))
        
        mtx.to_csv(path_or_buf=f'{self.outdir_prefix}/counts.txt',
                sep='\t',
                header =True,
                index=False)
        
        if self.out10X:
            mtx = mtx.set_index(['gene_id', 'gene_name'], drop=True)
            sparse_mtx = sparse.coo_matrix(mtx.values)
            io.mmwrite(os.path.join(self.tenX_out,'matrix.mtx'),
                            sparse_mtx)
            with open(os.path.join(self.tenX_out,'matrix.mtx'),'rb') as mtx_in:
                    with gzip.open(os.path.join(self.tenX_out,'matrix.mtx') + 
                                '.gz','wb') as mtx_gz: 
                        #创建一个读写文件'matrix.mtx.gz'，用以将matrix.mtx拷贝过去
                        shutil.copyfileobj(mtx_in, mtx_gz)
            os.remove(os.path.join(self.tenX_out,'matrix.mtx'))
            ##save barcodes.tsv.gz
            barcodesFile = pd.DataFrame(mtx.columns.tolist())
            barcodesFile.to_csv(path_or_buf=os.path.join(self.tenX_out,"barcodes.tsv.gz"),
                                sep='\t',
                                header =False,
                                index=False)
            ##save features.tsv.gz
            featuresFile = pd.DataFrame(mtx.index.tolist())
            featuresFile.to_csv(os.path.join(self.tenX_out,"features.tsv.gz"),
                                sep='\t',
                                header =False,
                                index=False)

    @utils.logit
    def run(self):
        self.id_name = utils.get_id_name_dict(self.gtf)
        self.bam2table()
        df = pd.read_csv(self.count_detail_file, sep='\t')
        self.write_matrix(df)
        df_sum = self.get_df_sum(df)
        df_sum.to_csv(self.count_summary, sep='\t', index=False)


def count(args):
    step = 'count'
    count_obj = COUNT(step, args)
    count_obj.run()


def get_count_para(parser, optional=False):
    parser.add_argument("--bam", help="Sorted featureCounts output bamfile.",
                        required=True)
    parser.add_argument("--gtf", help="GTF file path.",
                        required=True)
    parser.add_argument("--out10X", help="Whether write out 10X outputs.",
                        action="store_true")
    if optional:
        parser = utils.common_args(parser)
    return (parser)
