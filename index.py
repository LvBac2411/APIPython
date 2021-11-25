from base64 import decode
from os import abort, getcwd, path
import os
import cv2
from flask import Flask, json,jsonify, request
import utils

app = Flask(__name__)

@app.route("/picture/",methods=["POST"])
def post_add():
    if not request.data:
        abort(400)
    with open("encodedData.json","w+") as f:
        f.write(request.data.decode("utf-8"))
    return request.data.decode("utf-8")

@app.route("/picture/filterImg/",methods=["GET"])
def get_filter():
    # path = request.headers['path']
    blur = utils.filterImg()
    blur = getcwd() + os.sep + blur
    return blur

@app.route("/myip", methods=["GET"])
def get_my_ip():
    return jsonify({'your ip address': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
