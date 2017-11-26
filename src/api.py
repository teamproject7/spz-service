from flask import Flask
from flask_restful import reqparse, Api

from src.my_openalpr import init_openalpr
from src.resource.spz import SPZ
from src.resource.spz_img import SPZ_IMG
from src.storage import *


# TODO simple logovanie nefici dobre
# http://flask.pocoo.org/docs/dev/logging/
def before_start():
    init_openalpr()
    init_storage()


before_start()
app = Flask(__name__)

api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('spz')
api.add_resource(SPZ, '/spz/<spz_string>')
api.add_resource(SPZ_IMG, '/spz_img/')
