from flask import Flask, send_from_directory, request, send_file
from waitress import serve
app = Flask(__name__)
folder = '/bukti'
data = ''
download_path = folder+data

@app.route('/download', methods = ['POST'])
def download_simulation():
    return send_file (download_path, attachment_filename=data)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=6011)