import os
__VERSION__ = "0.0.1"
ASSAY_DICT = {"drug": "Drug seq analysis workflow."}


RUN_THREADS = {
    'trim': 5,
    'mapping': 20,
    'count': 5
}

ROOT_DIR = os.path.dirname(__file__)