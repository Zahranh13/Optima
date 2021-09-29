import flask
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/welcome', methods = ['POST'])
def welcome():
    hasil = {"message": "welcome"}
    return jsonify(hasil)

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6000)
    app.run(port=6000, debug=True)