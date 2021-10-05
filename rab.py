import flask 
from flask import Flask, jsonify, request
import json 
from sqlLib_Optima import check_get_rab, input_target_rab, check_id_admin, edit_rab, check_id_mitra, get_tgl_target
from convert_rupiah import transfrom_to_rupiah_format
import decimal
from waitress import serve
app = Flask(__name__)

@app.route('/rab&target/mitra/input', methods = ['POST'])
def input_rab():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data or 'biaya' not in json_data or 'target' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data['nama_project']
            cost = json_data['biaya']
            target = json_data['target']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                rab_check = check_get_rab(np, im)
                if rab_check != None:
                    hasil = {"message" : "Already exist"}
                    respon = jsonify(hasil)
                    return respon, 208
                else:
                    input_target_rab(np, im, cost, target)
                    hasil = {"message": "input success"}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route('/rab/show', methods = ['POST'])
def show_rab():
    json_data = request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data:
            hasil = {"message": "error request"}
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data['nama_project']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                rab_check = check_get_rab(np, im)
                if rab_check == None:
                    hasil = {"message": "No-content"}
                    respon = jsonify(hasil)
                    return respon, 204
                else:
                    go = float(rab_check)
                    go = "{:.2f}".format(go)
                    go = transfrom_to_rupiah_format(decimal.Decimal(go))
                    hasil = {"message": go}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route('/rab/admin/edit', methods = ['POST'])
def rab_edit():
    json_data = request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data or 'biaya' not in json_data or 'id_admin' not in json_data:
            hasil = {"message": "error request"}
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            ia = json_data ['id_admin']
            np = json_data['nama_project']
            cost = json_data['biaya']
            cek_idm = check_id_mitra(im)
            cek_ida = check_id_admin(ia)
            if cek_idm == False or cek_ida == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                rab_check = check_get_rab(np, im)
                if rab_check == None:
                    hasil = {"message": "No-content"}
                    respon = jsonify(hasil)
                    return respon, 204
                else:
                    e_r = edit_rab(cost, np, im)
                    if e_r == False:
                        hasil = {"message": "Update failed"}
                        respon = jsonify(hasil)
                        return respon, 203
                    else:
                        hasil = {"message": "Update success"}
                        respon = jsonify(hasil)
                        return respon, 200

@app.route('/target/show', methods = ['POST'])
def show_target():
    json_data = request.json
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
            im = json_data ['id_mitra']
            np = json_data['nama_project']
            target = get_tgl_target(np, im)
            if target == None:
                hasil = {"message": "No-content"}
                respon = jsonify(hasil)
                return respon, 204
            else:
                hasil = {"message": target}
                respon = jsonify(hasil)
                return respon, 200

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6012)
    app.run(port=6012, debug=True)