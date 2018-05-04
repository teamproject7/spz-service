import sys
import os
from openalpr import Alpr
from src.const import OPENALPR_COUNTRY

alpr = Alpr(
    country=OPENALPR_COUNTRY,
    config_file=os.environ['OPENALPR_CONFIG_FILE'],
    runtime_dir=os.environ['OPENALPR_RUNTIME_DIR']
)

print('Initializing OpenALPR ...')
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)
else:
    print('OpenALPR initialized ...')

alpr.set_top_n(3)
alpr.set_default_region("sk")


def recongnize(img_path):
    global alpr
    if alpr is None:
        print('ALPR is not initialized')

    print('Recongnizing')

    # "processing_time_ms": 77.234795,
    # "data_type": "alpr_results",
    # "img_height": 358,
    # "img_width": 636,
    # "results": [ {...}, ... ]
    result = alpr.recognize_file(img_path)
    # TODO log processing time
    return result
