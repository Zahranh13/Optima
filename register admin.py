import flask 
from flask import Flask, jsonify, request
import hashlib 
import json 
import uuid
from sqlLib_Optima import register_admin, cek_ua, cek_email_admin
from waitress import serve
app = Flask(__name__)

@app.route('/auth/admin/regist', methods = ['POST'])
def admin_register():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'username' not in json_data or 'password' not in json_data or 'nohp' not in json_data or 'email' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            ia= str(uuid.uuid4().hex)
            un= json_data['username']
            pwd = json_data['password']
            nohp = json_data['nohp']
            em = json_data['email']
            pw = hashlib.sha256(pwd.encode()).hexdigest()
            cn = cek_ua(un)
            ce = cek_email_admin(em)
            if cn == False or ce == False:
                hasil = {"message": "username and email are already existed"}
                respon = jsonify(hasil)
                return respon, 208
            else:
                register_admin (ia, un, pw, nohp, em)
                hasil = {"message": "Regist Success"}
                respon = jsonify(hasil)
                return respon, 202

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6004)
    app.run(port=6004, debug=True)