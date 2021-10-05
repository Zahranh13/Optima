import flask 
from flask import Flask, jsonify, request
import json 
from sqlLib_Optima import check_mitra, check_selesai_progress_instalasi, insert_progress, insert_progress_instalasi, show_progress, check_id_admin, check_id_mitra, check_progress, show_level_progress_percentage, show_progress_desc, update_status, check_selesai_progress_persiapan, check_selesai_progress_go_live, insert_progress_persiapan, insert_progress_go_live, get_id_mitra, update_status_pada_center, count_progress, hitung_progress_level, get_progress_project, search_get_progress_project, progress_desc, get_tgl_target
from waitress import serve
app = Flask(__name__)

@app.route('/progress/input', methods = ['POST'])
def input_progress():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data or 'tanggal' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data ['nama_project']
            tgl = json_data['tanggal']
            cek_mitra = check_id_mitra(im)
            if cek_mitra == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                cek_p = check_progress(np, im)
                if cek_p == False:
                    hasil = {"message": "Regist Success"}
                    respon = jsonify(hasil)
                    return respon, 208
                else:
                    update_status_pada_center(tgl, "proses", np, im)
                    insert_progress_persiapan(np, im, tgl)
                    hasil = {"message": "Input success"}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route('/progress/show/level/mitra', methods = ['POST'])
def level_progress():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data ['nama_project']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                hasil = show_level_progress_percentage(np)
                respon = jsonify(hasil)
                return respon, 200

@app.route('/progress/show/keterangan/mitra', methods = ['POST'])
def ket_progress():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = json.dumps(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'level' not in json_data or 'nama_project' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            lvl = json_data['level']
            np = json_data ['nama_project']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                hasil = progress_desc(np, lvl)
                respon = jsonify(hasil)
                return respon, 200                

@app.route('/progress/update/status/mitra', methods = ['POST'])
def update_stat_progress():
    json_data = flask.request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data or 'level' not in json_data or 'status' not in json_data or 'tanggal' not in json_data or 'keterangan' not in json_data or 'bukti' not in json_data or 'deskripsi' not in json_data:
            hasil = {"message": "process failed"}
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data ['nama_project']
            lvl = json_data['level']
            ket = json_data['keterangan']
            stat = json_data['status']
            tgl = json_data['tanggal']
            bukti = json_data['bukti']
            desc = json_data['deskripsi']
            bukti = bukti.replace (" ", "_")
            bukti = bukti.replace (",","")
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                up_stat = update_status(stat, bukti, tgl, desc, im, np, lvl, ket)
                persiapan_check = check_selesai_progress_persiapan(im, np)
                instalasi_check = check_selesai_progress_instalasi (im, np)
                go_live_check = check_selesai_progress_go_live (im, np)
                if persiapan_check == True and instalasi_check == True and go_live_check == True:
                    update_status_pada_center(tgl, "selesai", np, im)
                elif persiapan_check == True and instalasi_check == False and go_live_check == False:
                    insert_progress_instalasi(np, im, tgl)
                elif persiapan_check == True and instalasi_check == True and go_live_check == False:
                    insert_progress_go_live(np, im, tgl)    
                hasil = {"message": "Update success"}
                respon = jsonify(hasil)
                return respon, 200

@app.route('/progress/hitung/mitra', methods = ['POST'])
def jumlah_progress():
    json_data = flask.request.json
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
            np = json_data ['nama_project']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = {"message": "Forbidden"}
                respon = json.dumps(hasil)
                return respon, 403
            else:
                persent = count_progress(im, np) 
                if persent == None:
                    hasil = {"message": "Update failed"}
                    respon = jsonify(hasil)
                    return respon, 203
                else:
                    hasil = {"message": "Update success"}
                    respon = jsonify(hasil)
                    return respon, 200

#@app.route('/progress/hitung/level/mitra', methods = ['POST'])
#def jumlah_level_progress():
#    json_data = flask.request.json
#    if json_data == None:
#        hasil = {"message": "process failed"}
#        respon = jsonify(hasil)
#        return respon, 400
#    else:
#        if 'id_mitra' not in json_data or 'nama_project' not in json_data or 'level' not in json_data:
#            hasil = {"message": "error request"}
#           respon = json.dumps(hasil)
#            return respon, 401
#        else:
#            im = json_data ['id_mitra']
#            np = json_data ['nama_project']
#           lvl = json_data['level']
#            cek_id = cek_im(im)
#            if cek_id == False:
#                hasil = {"message": "Forbidden"}
#                respon = json.dumps(hasil)
#                return respon, 403
#            else:
#                persent = hitung_progress(im, np, lvl)    
#                hasil = {"message": persent}
#                respon = jsonify(hasil)
#               return respon, 200

@app.route('/progress/show/project/admin', methods = ['POST'])
def show_project_progress():
    json_data = request.json
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
            im = json_data ['id_mitra']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:
                hasil = get_progress_project()
                return hasil, 200

@app.route('/progress/search/project/admin', methods = ['POST'])
def search_progress():
    json_data = flask.request.json
    if json_data == None:
        hasil = []
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data:
            hasil = []
            respon = json.dumps(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data ['nama_project']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = []
                respon = json.dumps(hasil)
                return respon, 403
            else:  
                hasil = search_get_progress_project(np)
                return hasil, 200

@app.route('/progress/get/deskripsi', methods = ['POST'])
def get_desc():
    json_data = request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'nama_project' not in json_data or 'level' not in json_data or 'keterangan' not in json_data or 'id_mitra' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data ['nama_project']
            lvl = json_data['level']
            ket = json_data['keterangan']
            cek_id = check_id_mitra(im)
            if cek_id == False:
                hasil = {"message": "Forbidden"}
                respon = json.dumps(hasil)
                return respon, 403
            else:
                dat = progress_desc(np, lvl, ket)
                if dat == None:
                    hasil = {"message": "No-content"}
                    respon = jsonify(hasil)
                    return respon, 204
                else:
                    hasil = {"message": dat}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route('/progress/get/target', methods = ['POST'])
def get_target():
    json_data = request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'nama_project' not in json_data or 'id_mitra' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            im = json_data ['id_mitra']
            np = json_data ['nama_project']
            check = check_id_mitra(im)
            if check == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                dat = get_tgl_target(np, im)
                if dat == None:
                    hasil = {"message": "No-content"}
                    respon = jsonify(hasil)
                    return respon, 204
                else:
                    hasil = {"message": dat}
                    respon = jsonify(hasil)
                    return respon, 200

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6007)
    app.run(port=6007, debug=True)