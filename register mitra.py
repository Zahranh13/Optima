import flask 
from flask import Flask, jsonify, request
import hashlib 
import json 
import uuid
from sqlLib_Optima import check_mitra, reg_mitra
from waitress import serve
app = Flask(__name__)

@app.route('/auth/mitra/register', methods = ['POST'])
def mitra_register():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'nama_mitra' not in json_data or 'nama_pic' not in json_data or 'no_telp' not in json_data or 'email' not in json_data or 'pass' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            nm = json_data['nama_mitra']
            np = json_data ['nama_pic']
            notelp = json_data['no_telp']
            em = json_data ['email']
            pwd = json_data['pass']
            im = str(uuid.uuid4().hex)
            pw = hashlib.sha256(pwd.encode()).hexdigest()
            if check_mitra(nm) == True:
                hasil = {"message": "Already existed"}
                respon = jsonify(hasil)
                return respon, 208
            else:
                a = reg_mitra(im, nm, np, notelp, em, pw)
                if a == True:
                    hasil = {"message": "Regist Success"}
                    respon = jsonify(hasil)
                    return respon, 202
                else:
                    hasil = {"message": "Regist Failed"}
                    respon = jsonify(hasil)
                    return respon, 204
                

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6001)
    app.run(port=6001, debug=True)

    