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

alpr.set_top_n(20)
alpr.set_default_region("md")


def recongnize(img_path):
    print('recongniying')
    global alpr
    if alpr is None:
        print('alpr is not initialized')

    return alpr.recognize_file(img_path)['results']

# TODO move to proper place
# Call when completely done to release memory
# alpr.unload()
