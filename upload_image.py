import os
import urllib
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename

from flask import Flask, request
from flask_restful import Resource, Api
from flask import make_response, render_template
#from json import dumps
from flask import Response
#from flask_csv import send_csv
from waitress import serve
#import sqlite3
import json
import logging

UPLOAD_FOLDER = '/bukti'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 *1024

api = Api(app)
total = 0

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1) [1].lower() in ALLOWED_EXTENSIONS

class UploadFile(Resource):
    def post(self):
        #check if the post request has the file part
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and allowed_file (file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp

api.add_resource(UploadFile, '/mitra/uploadfile', methods= ['POST'])

if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port=6010)