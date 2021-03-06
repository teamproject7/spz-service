from flask import Flask
from flask_restful import Api
from src.resource.spz import SPZ
from src.resource.spz_img import SPZ_IMG
from src.resource.spz_v1 import SPZ_V1
from src.resource.spz_img_v1 import SPZ_IMG_V1

app = Flask(__name__)

api = Api(app)
api.add_resource(SPZ, '/spz/')
api.add_resource(SPZ_IMG, '/spz_img/')
api.add_resource(SPZ_V1, '/api/v1.0/spz/')
api.add_resource(SPZ_IMG_V1, '/api/v1.0/spz_img/')
