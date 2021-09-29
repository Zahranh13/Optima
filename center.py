import flask
from flask import Flask, jsonify, request
from sqlLib_Optima import insert_center, get_center, cek_im, cek_ia, get_id_mitra, check_insert_center, update_status_pada_center, get_all_mitra, search_get_general_project, list_paket, list_sto
import json
from waitress import serve
app = Flask(__name__)

@app.route('/center/show/belum', methods = ['POST'])
def show_center_belum():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data['id_mitra']
            st = "belum"
            id_check = cek_im(im)
            if id_check == False:
                hasil = []
                respon = json.dumps (hasil)
                return respon, 403
            else:
                respon = get_center(im, st)
                return respon, 200

@app.route ('/center/show/proses', methods = ['POST'])
def show_center_proses():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data['id_mitra']
            st = "proses"
            id_check = cek_im(im)
            if id_check == False:
                hasil = []
                respon = json.dumps (hasil)
                return respon, 403
            else:
                respon = get_center(im, st)
                return respon, 200
    
@app.route ('/center/show/selesai', methods = ['POST'])
def show_center_selesai():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data['id_mitra']
            st = "selesai"
            id_check = cek_im(im)
            if id_check == False:
                hasil = []
                respon = json.dumps (hasil)
                return respon, 403
            else:
                respon = get_center(im, st)
                return respon, 200 

@app.route ('/center/input', methods = ['POST'])
def input_center():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "error request"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'nama_mitra' not in json_data or 'nama_project' not in json_data or 'tanggal' not in json_data or 'id_admin' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            nm = json_data['nama_mitra']
            np = json_data ['nama_project']
            tgl = json_data['tanggal']
            im = get_id_mitra(nm)
            id_check = cek_ia(ia)
            if id_check == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                input_check = check_insert_center(np, im)
                if input_check == False:
                    hasil = {'message': "Already exist"}
                    respon = jsonify(hasil)
                    return respon, 208
                else:
                    insert_center(im, np, 0, tgl, "belum")
                    hasil = {'message': "Input success"}
                    respon = jsonify(hasil)
                    return respon, 200


@app.route ('/center/update', methods = ['POST'])
def update_center():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data or 'tanggal' not in json_data or 'status' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            im = json_data['id_mitra']
            np = json_data['nama_project']
            tgl = json_data ['tanggal']
            stat = json_data['status']
            id_check = cek_im(im)
            if id_check == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                update_status_pada_center(tgl, stat, np, im)
                hasil = {"message" :"Update success"}
                respon = jsonify(hasil)
                return respon, 200
                    
@app.route('/center/mitra', methods = ['POST'])
def show_all_mitra():
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
            ia = json_data['id_admin']
            id_check = cek_ia(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps (hasil)
                return respon, 403
            else:
                respon = get_all_mitra()
                return respon, 200 

@app.route('/center/search/project', methods = ['POST'])
def search_get_generalproject():
    json_data = request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_admin' not in json_data or 'nama_project' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            np = json_data['nama_project']
            id_check = cek_ia(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps (hasil)
                return respon, 403
            else:
                hasil = search_get_general_project(np)
                return hasil, 200

@app.route('/center/get/sto', methods = ['POST'])
def get_list_sto():
    json_data = request.json
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
            ia = json_data['id_admin']
            id_check = cek_ia(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps (hasil)
                return respon, 403
            else:
                respon = list_sto()
                return respon, 200

@app.route('/center/get/paket', methods = ['POST'])
def get_list_paket():
    json_data = request.json
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
            ia = json_data['id_admin']
            id_check = cek_ia(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps (hasil)
                return respon, 403
            else:
                respon = list_paket()
                return respon, 200

if __name__ == "__main__":
    #serve (app, host="0.0.0.0", port=6008)
    app.run(port=6008, debug=True)