import sys
from openalpr import Alpr

alpr = None


def init_openalpr():
    global alpr
    alpr = Alpr("eu", "/path/to/openalpr.conf", "/tmp/openalpr/runtime_data/")
    print('Initializing OpenALPR ...')
    if not alpr.is_loaded():
        print("Error loading OpenALPR")
        sys.exit(1)
    else:
        print('OpenALPR initialized ...')

    alpr.set_top_n(20)
    alpr.set_default_region("md")

# TODO move to proper place
# Call when completely done to release memory
# alpr.unload()
