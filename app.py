#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
import os
import pickle
import sklearn
import pandas as pd

app = Flask(__name__)

gill_size_data = ['b', 'n']
gill_color_data = ['b', 'e', 'g', 'h', 'k', 'n' ,'o', 'p' ,'r', 'u', 'w' ,'y']
buries_data = ['f', 't']
stalk_shape_data = ['e', 't']
stalk_color_above_ring = ['b', 'c', 'e' ,'g', 'n', 'o', 'p', 'w', 'y']
info = [gill_size_data, gill_color_data, buries_data, stalk_shape_data, stalk_color_above_ring]
name = ['gill-size', 'gill-color', 'burises', 'stalk-shape', 'stalk-color-above-ring']
#메인 페이지  
@app.route("/")
def home():
    return render_template("index.html", info = info, name = name)

@app.route("/pred", methods=['POST'])
def predict():
    if request.method == 'POST':
        result = request.form
        pred_data = make_data(result)
        pred = model.predict(pred_data)
        if  pred == 'p': #독버섯
            res = '축하합니다! 독버섯입니다!!!!'
        elif pred == 'e': #식용
            res = '아쉽습니다.... 식용버섯입니다....'
        else: #오류
            print('error')
    return render_template("events.html", res = res)

def make_data(result):
    tmp = 0
    data = [[0,0, 0,0,0,0,0,0,0,0,0,0,0,0, 0,0, 0,0, 0,0,0,0,0,0,0,0,0]]
    check = [result['gill-size'], result['gill-color'], result['burises'], result['stalk-shape'],
             result['stalk-color-above-ring']]
    for i in range(len(info)):
        for j in range(len(info[i])):
            if check[i] == info[i][j]: 
                data[0][tmp+j] = 1
        tmp += len(info[i])
    return data

if __name__=="__main__":
    f = open("static/model.pkl", 'rb')
    model = pickle.load(f)
    f.close()
    app.run(debug=True, host="0.0.0.0")
