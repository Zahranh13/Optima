import flask 
from flask import Flask, jsonify, request
import hashlib 
import json 
import uuid
from sqlLib_Optima import login_admin
from waitress import serve
app = Flask(__name__)

@app.route('/auth/admin/login', methods = ['POST'])
def adminlogin():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify (hasil)
        return respon, 400
    else:
        if 'username' not in json_data or 'password' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            un = json_data['username']
            psw = json_data['password']
            pw = hashlib.sha256(psw.encode()).hexdigest()
            check = login_admin(un,pw)
            if check == None:
                hasil = {"message": "Unregistered account"}
                respon = jsonify(hasil)
                return respon, 203
            else:
                hasil = {"message": check}
                respon = jsonify(hasil)
                return respon, 200

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6003)
    app.run (port=6003, debug=True)