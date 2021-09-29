import flask 
from flask import Flask, jsonify, request
import json 
from sqlLib_Optima import check_id_admin, get_all_mitra_with_status, check_id_mitra
from waitress import serve
app = Flask(__name__)


@app.route('/mitra/show', methods = ['POST'])
def show_mitra_all():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_admin' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            ia = json_data ['id_admin']
            cek_id = check_id_admin(ia)
            if cek_id == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_all_mitra_with_status()
                return respon, 200 

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6009)
    app.run(port=6009, debug=True)