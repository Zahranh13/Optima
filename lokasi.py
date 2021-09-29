from flask import Flask, jsonify, request
from sqlLib_Optima import check_id_mitra, get_report_lokasi, input_report_lokasi
from waitress import serve
app = Flask(__name__)

@app.route('/lokasi/input', methods = ['POST'])
def input_location():
    json_data = request.json
    if json_data == None:
        hasil = {"message": "process failed"}
        respon = jsonify(hasil)
        return respon, 400
    else:
        if 'id_mitra' not in json_data or 'nama_project' not in json_data or 'lat' not in json_data or 'lng' not in json_data:
            hasil = {"message": "error request"}
            respon = jsonify(hasil)
            return respon, 401
        else:
            im = json_data['id_mitra']
            np = json_data['nama_project']
            lat = json_data['lat']
            lng = json_data['lng']
            cek_idm = check_id_mitra(im)
            if cek_idm == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                input_check = input_report_lokasi(np, lat, lng)
                if input_check == False:
                    hasil = {"message": "error input lokasi"}
                    respon = jsonify(hasil)
                    return respon, 205
                else:
                    hasil = {"message": "Input success"}
                    respon = jsonify(hasil)
                    return respon, 200

@app.route('/lokasi/get/mitra', methods = ['POST'])
def mitra_get_lokasi():
    json_data = request.json
    if json_data == None:
        hasil = {"message": "error process"}
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
            cek_idm = check_id_mitra(im)
            if cek_idm == False:
                hasil = {"message": "Forbidden"}
                respon = jsonify(hasil)
                return respon, 403
            else:
                check,data = get_report_lokasi(np)
                if check == False:
                    hasil = {"message": "no data"}
                    respon = jsonify(hasil)
                    return respon, 204
                else:
                    hasil = {"message": "OK", "lat":data[0], "lng":data[1]}
                    respon = jsonify(hasil)
                    return respon, 200

if __name__ == '__main__':
    #serve(app, host="0.0.0.0", port=6014)
    app.run(port=6014, debug=True)