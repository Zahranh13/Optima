import flask 
from flask import Flask, jsonify, request
import json
from sqlLib_Optima import show_project_amount, check_id_mitra, check_project, count_project_stat_belum, count_project_stat_proses, count_project_stat_selesai
from waitress import serve
app = Flask(__name__)

@app.route('/project/check/center', methods = ['POST'])
def hitung_projek():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            im = json_data['id_mitra']
            np = json_data['nama_project']
            tahun = json_data['tahun']
            cek_id = check_id_mitra(im)
            cek_np = check_project(np)
            if cek_id == False or cek_np == False or tahun == None:
                hasil = {"message": "error request"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                
                jumlah_belum = count_project_stat_belum(tahun)
                jumlah_proses = count_project_stat_proses(tahun)
                jumlah_selesai = count_project_stat_selesai(tahun)
                z = show_project_amount(jumlah_belum, jumlah_proses, jumlah_selesai)
                if z == True:
                    hasil = {"belum" : jumlah_belum, "proses" : jumlah_proses, "selesai": jumlah_selesai}
                    respon = jsonify(hasil)
                    return respon, 200
                else:
                    hasil = {"error"}
                    respon = jsonify(hasil)
                    return respon, 204

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6015)
    app.run(port=6015, debug=True)