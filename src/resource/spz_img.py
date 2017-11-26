from flask_restful import reqparse, Resource, abort

from src.my_filestorage import save_b64_to_file, allowed_file
from src.my_openalpr import recongnize as recognize_img

parser = reqparse.RequestParser()
parser.add_argument('image')


class SPZ_IMG(Resource):
    def get(self):
        return 'get spz img'

    def post(self):
        args = parser.parse_args()

        fpath = save_b64_to_file(args['image'])

        if not fpath:
            abort(404, message="Unexpected error", error_code='UNEXPECTED_ERROR')

        if not allowed_file(fpath):
            abort(404, message="File is not allowed", error_code='FILE_NOT_ALLOWED')
        else:
            return recognize_img(fpath)
