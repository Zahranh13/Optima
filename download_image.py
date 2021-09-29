from flask import Flask, send_from_directory, request, send_file
from waitress import serve
from sqlLib_Optima import check_id_mitra, get_filebukti

app = Flask(__name__)
UPLOAD_FOLDER = '/bukti'

@app.route('/mitra/downloadfile', methods = ['POST'])
def download_file():
    json_data = request.json
    if json_data == None:
        return 400
    else:
        if 'id_mitra' not in json_data or 'level' not in json_data or 'keterangan' not in json_data or 'nama_project' not in json_data:
            return 401
        else:
            im = json_data['id_mitra']
            np = json_data ['nama_project']
            lvl = json_data['level']
            ket = json_data['keterangan']
            cek_idm = check_id_mitra(im)
            if cek_idm == False:
                return 403
            else:
                file_name = get_filebukti(np, lvl, ket)
                if file_name == None:
                    return 204
                else:
                    data = UPLOAD_FOLDER + file_name[0]
                    return send_file(data, attachment_filename=file_name[0]), 200

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6011)
    app.run(port=6011, debug=True)