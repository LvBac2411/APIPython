import cv2
import base64
import json
import numpy as np

#ma hoa base64
def encodeImg(data, file="encodedData.json"):
    encode = json.dumps([base64.b64encode(data).decode('utf-8'),
    str(data.dtype),
    data.shape])
    with open(file, "w+") as f:
        f.write(encode)
    return encode
 
 #giai ma base64
def decodeImg(file="encodedData.json"):
    with open(file, "r") as f:
        encodedData = json.load(f)

    img, dtype, shape = encodedData
    
    img = np.frombuffer(base64.b64decode(img), dtype=dtype).reshape(shape)
    # cv2.imshow("data", img)
    # cv2.waitKey(0)
    return img

def filterImg(img):
    blur = cv2.bilateralFilter(img,9,60,60)
    return blur

#tim canh bang PP Canny
def CannyDetection(img, percentage=100):
    edges = cv2.Canny(img, 100, 200)
    edges = _Percentage(edges, percentage)
    cv2.imshow('image', edges)
    cv2.waitKey(0)

#Nhan dien khuon mat
def FaceRec(img, percentage=100):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(20, 20),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    img = _Percentage(img, percentage)
    cv2.imshow('nhan dien khuon mat', img)
    cv2.waitKey(0)

#chinh kich co anh
def _Percentage(img, per):
    scale_percent = per
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return resized

#encodeImg("D:\Pictures\clock.jpg", "encodedData.json")