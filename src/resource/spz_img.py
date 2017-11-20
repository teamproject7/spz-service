from flask import request
from flask_restful import abort, Resource
from src.openalpr import alpr
from src.model.egv import *
from src.const import *
from werkzeug.utils import secure_filename


# TODO move
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# TODO move
def recognize(img_path):
    results = alpr.recognize_file(img_path)

    i = 0
    for plate in results['results']:
        i += 1
        print("Plate #%d" % i)
        print("   %12s %12s" % ("Plate", "Confidence"))
        for candidate in plate['candidates']:
            prefix = "-"
            if candidate['matches_template']:
                prefix = "*"

            print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))


class SPZ_IMG(Resource):
    def get(self, spz_string):
        pass

    def post(self, spz_string):

        # check if the post request has the file part
        if 'file' not in request.files:
            abort(404, message="No file part found", error_code='SPZ_NOT_FOUND')

        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename

        if file.filename == '':
            abort(404, message="No selected file", error_code='SPZ_NOT_FOUND')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))

            # result = recognize(filename)

            return generate_egv_object('BA-000AA')

        else:
            abort(404, message="File not allowed", error_code='SPZ_NOT_FOUND')


# recognize('C:\/Users\/mpc\/Downloads\/spz1.jpg')
