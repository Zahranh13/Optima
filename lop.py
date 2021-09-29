import flask
from flask import Flask, jsonify, request
from mysql.connector import cursor
from sqlLib_Optima import get_general_project_base_on_nodin, get_id_mitra, insert_lpo, check_id_admin, check_project, get_project, get_nama_project, cek_project_lop, get_project_belum_diserahkan, get_project_sudah_diserahkan, get_all_nodin, sql_connection, update_data_center, update_lop
import json
from waitress import serve
app = Flask(__name__)

@app.route ('/lop/input', methods = ['POST'])
def input_lop():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else: 
        if 'nama_project' not in json_data or 'nodin' not in json_data or 'witel' not in json_data or 'paket' not in json_data or 'sto' not in json_data or 'id_admin' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify (hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            np = json_data['nama_project']
            nodin = json_data['nodin']
            wtl = json_data['witel']
            pkt = json_data['paket']
            sto = json_data['sto']
            admin_check = check_id_admin(ia)
            if admin_check == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                check = cek_project_lop(np, nodin)
                if check == False:
                    hasil = {"message": "Already exist"}
                    respon = jsonify(hasil)
                    return respon, 208
                else:
                    insert_lpo(np, nodin, wtl, pkt, sto)
                    hasil = {"message": "Input success"}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route ('/lop/show', methods = ['POST'])
def show_lop():
    json_data = flask.request.json
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
            n_p = json_data['nama_project']
            check = check_id_admin(ia)
            if check == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_project(n_p)
                return respon, 200

@app.route ('/lop/show/all', methods = ['POST'])
def show_all_lop():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else: 
        if 'id_admin' not in json_data or 'nodin' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            nodin = json_data['nodin']
            check = check_id_admin(ia)
            if check == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_general_project_base_on_nodin(nodin)
                return respon, 200

@app.route ('/lop/show/belum', methods = ['POST'])
def show_lop_belum():
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
            id_check = check_id_admin(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_project_belum_diserahkan()
                return respon, 200

@app.route ('/lop/show/sudah', methods = ['POST'])
def show_lop_sudah():
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
            id_check = check_id_admin(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_project_sudah_diserahkan()
                return respon, 200                
        
@app.route ('/lop/project', methods = ['POST'])
def list_project():
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
            id_check = check_id_admin(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_nama_project()
                return respon, 200

@app.route ('/lop/nodin', methods = ['POST'])
def list_nodin():
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
            id_check = check_id_admin(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_all_nodin()
                return respon, 200

@app.route ('/lop/update', methods = ['POST'])
def lop_update():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = json.dumps(hasil)
        return respon, 400
    else: 
        if 'id_admin' not in json_data or 'witel' not in json_data or 'paket' not in json_data or 'sto' not in json_data or 'nama_mitra' not in json_data or 'nama_project_new' not in json_data or 'nama_project_old' not in json_data:
            hasil = {"message": "error request"}
            respon = json.dumps(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            wtl = json_data['witel']
            pkt = json_data['paket']
            sto = json_data['sto']
            nm = json_data['nama_mitra']
            np_old = json_data['nama_project_old']
            np_new = json_data['nama_project_new']
            id_check = check_id_admin(ia)
            if id_check == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                cek_np_old = check_project(np_old)
                if cek_np_old == False:
                    hasil = {"message": "data is not existed"}
                    respon = jsonify(hasil)
                    return respon, 203
                else:
                    id_mitra = get_id_mitra(nm)
                    update_lop (wtl, pkt, sto, np_new, np_old)
                    update_data_center(np_new, id_mitra, np_old)
                    hasil = {"message": "Update success"}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route ('/lop/show/nodin', methods = ['POST'])
def show_lop_nodin():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else: 
        if 'id_admin' not in json_data or 'nodin' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            ia = json_data['id_admin']
            nodin = json_data['nodin']
            id_check = check_id_admin(ia)
            if id_check == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                respon = get_general_project_base_on_nodin(nodin)
                return respon, 200

if __name__ == "__main__":
    #serve(App, host = "0.0.0.0", port=6006)
    app.run(port=6006, debug=True)