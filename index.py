from base64 import decode
from os import abort
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
def post_filter():
    img = utils.decodeImg()
    blur = utils.filterImg(img)
    code = utils.encodeImg(blur)
    return code

@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)