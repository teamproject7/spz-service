from storage import *
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from resources.spz_resource import SPZ


def before_start():
    init_storage()


before_start()
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('spz')
api.add_resource(SPZ, '/spz/<spz_string>')

if __name__ == '__main__':
    app.run(debug=True)
