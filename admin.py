import flask 
from flask import Flask, jsonify, request
import hashlib 
import json 
import uuid
from sqlLib_Optima import login_admin
from waitress import serve
app = Flask(__name__)

@app.route("/auth/admin/login", methods = ['POST'])
def alogin():
    json_data = flask.request.json
    if json_data == None:
        result = {"message" : "process failed"}
        respond = jsonify (result)
        return respond, 400
    else:
        if 'username' not in json_data or 'password' not in json_data:
            result = {"message": "error request"}
            respond = jsonify(result)
            return respond, 401
        else:
            em = json_data['username']
            psw = json_data['password']
            pw = hashlib.sha256(psw.encode()).hexdigest()
            check = login_admin(em,pw)
            if check == None:
                result = {"message": "Unregistered account"}
                respond = jsonify(result)
                return respond, 203
            else:
                result = {"message": check}
                respond = jsonify(result)
                return respond, 200

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=6003)
    app.run(port=6003, debug=True)