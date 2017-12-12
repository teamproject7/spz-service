from flask import Flask
from flask_restful import Api
from src.resource.spz import SPZ
from src.resource.spz_img import SPZ_IMG

app = Flask(__name__)

api = Api(app)
api.add_resource(SPZ, '/spz/')
api.add_resource(SPZ_IMG, '/spz_img/')
