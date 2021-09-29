import flask 
from flask import Flask, jsonify, request
import json 
from sqlLib_Optima import insert_request, check_nodin_request, cek_ia, get_all_request, get_request, check_nodin_request, get_perihal, search_get_permintaan, update_permintaan
from waitress import serve
app = Flask(__name__)

@app.route('/permintaan/input', methods = ['POST'])
def input_request():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_admin' not in json_data or 'nodin' not in json_data or 'pemohon' not in json_data or 'perihal' not in json_data or 'tanggal' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            nodin = json_data['nodin']
            pemohon = json_data['pemohon']
            hal = json_data['perihal']
            tgl = json_data['tanggal']
            cek_ida = cek_ia(ia)
            if cek_ida == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                request_check = check_nodin_request(nodin)
                if request_check == False:
                    hasil = {"message": "Already exist"}
                    respon = jsonify(hasil)
                    return respon, 208
                else:
                    insert_request(nodin, pemohon, hal, tgl)
                    hasil = {"message": "Input success"}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route('/permintaan/show', methods = ['POST'])
def show_all_request():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_admin' not in json_data:
            hasil = []
            respon = jsonify(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            cek_ida = cek_ia(ia)
            if cek_ida == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                hasil = get_all_request()
                return hasil, 200

@app.route('/permintaan/search', methods = ['POST'])
def show_request_perihal():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_admin' not in json_data or 'value' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            value = json_data['value']
            cek_ida = cek_ia(ia)
            if cek_ida == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                hasil = search_get_permintaan(value)
                return hasil, 200

@app.route('/permintaan/perihal', methods = ['POST'])
def get_list_perihal():
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
            cek_ida = cek_ia(ia)
            if cek_ida == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_perihal()
                return respon, 200

@app.route('/permintaan/update', methods = ['POST'])
def update_request():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_admin' not in json_data or 'nodin' not in json_data or 'pemohon' not in json_data or 'perihal' not in json_data or 'tanggal' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            nodin = json_data['nodin']
            pemohon = json_data['pemohon']
            hal = json_data['perihal']
            tgl = json_data['tanggal']
            cek_ida = cek_ia(ia)
            if cek_ida == False:
                hasil = {"message": "Forbidden"}
                respon = json.dumps(hasil)
                return respon, 403
            else:
                update_permintaan(pemohon, hal, tgl, nodin)
                hasil = {"message": "update success"}
                respon = jsonify(hasil)
                return respon, 200
                


if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6005)
    app.run(port=6005, debug=True)