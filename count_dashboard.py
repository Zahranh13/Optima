import flask 
from flask import Flask, jsonify, request
import json 
from sqlLib_Optima import check_id_admin, count_project_stat_belum, count_project_stat_proses, count_project_stat_selesai, list_tahun_center
from waitress import serve
app = Flask(__name__)

@app.route('/dashboard/count', methods = ['POST'])
def count_dashboard():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "error process"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_admin' not in json_data or 'tahun' not in json_data:
            hasil = {"message": "error request"}
            respon = json.dumps(hasil)
            return respon, 401
        else:
            ia = json_data ['id_admin']
            thn = json_data [ 'tahun']
            cek_ida = check_id_admin(ia)
            if cek_ida == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                bel = count_project_stat_belum(thn)
                pros = count_project_stat_proses(thn)
                sel = count_project_stat_selesai (thn)
                if bel == True and pros == True and sel == True:
                    hasil = {"message": "success", "belum":bel, "proses":pros, "selesai":sel}
                    respon = jsonify(hasil)
                    return respon, 200
                else:
                    hasil = {"message": "failed"}
                    respon = jsonify(hasil)
                    return respon, 204

@app.route('/dashboard/tahun', methods = ['GET'])
def list_tahun():
    hasil = list_tahun_center()
    return hasil, 200

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6013)
    app.run(port=6013, debug=True)