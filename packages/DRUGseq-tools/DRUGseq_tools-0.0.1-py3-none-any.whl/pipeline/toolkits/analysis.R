script_path <- this.path::this.dir()
source(paste(script_path, '/tools.R', sep=''))
library(argparse, quietly = TRUE, verbose = FALSE)

parser <- ArgumentParser()

parser$add_argument("--count_matrix",
                    required=TRUE,
                    help="Count matrix.")
parser$add_argument("--group_info",
                    required=TRUE,
                    help="Group info file.")
parser$add_argument("--project",
                    required=TRUE,
                    help="Project name.")
parser$add_argument("--group_by",
                    default='tag',
                    help="Group by.")
parser$add_argument("--outdir",
                    required=TRUE,
                    help="Output directory.")
parser$add_argument("--normalization.method",
                    help="Normalize method for integration.",
                    choices=c('LogNormalize', 'SCT'),
                    default='LogNormalize')
parser$add_argument("--dims",
                    default=NULL,
                    help="PCA nums.")
parser$add_argument("--k_filter",
                    default=30,
                    help="Mininum cell nums of sample.")
args <- parser$parse_args()



### read in countdata and group data
# common parameters
min.cells = 4
min.features = 200
project = args$project
seurat_list_results = paste(args$project, '.seurat.rds', sep='')
seurat_results = paste(args$project, '.seurat.res', sep='')




if (!file.exists(paste(args$outdir,'/', seurat_results, '.h5seurat', sep=''))) {
  make_seurat_list(count_file = args$count_matrix,
                   group_info = args$group_info,
                   filename = seurat_list_results,
                   outdir = args$outdir)
  integrate_seurat_list(paste(args$outdir, seurat_list_results, sep='/'),
                        outdir=args$outdir,
                        normalization.method = args$normalization.method,
                        filename = seurat_results,
                        k.filter = as.integer(args$k_filter))
}

if (!is.null(args$dims)) {
  dims = as.integer(args$dims)
} else {
  dims <- user.input('Please select your dims (integer): ')
  dims <- as.integer(dims)
}

standard_seurat_analysis(paste(args$outdir,'/', seurat_results, '.h5seurat', sep=''), 
                         filename = seurat_results,
                         outdir = args$outdir,
                         dims=as.integer(dims))

seurat_plot(paste(args$outdir,'/', seurat_results, '.h5seurat', sep=''), 
            outdir = args$outdir)


score_compound(paste(args$outdir,'/', seurat_results, '.h5seurat', sep=''),
               outdir=args$outdir,
               normalization.method = args$normalization.method,
               NC = 'NC',
               PC='PC1')



