#-*- coding:utf-8 -*-
from flask import Flask, render_template, request
import os
import pickle
import sklearn
import pandas as pd

app = Flask(__name__)

#메인 페이지  
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pred", methods=['POST'])
def predict():
    if request.method == 'POST':
      result = request.form
      pd = make_data(result)
    model.predict(pd)
    return render_template("list.html")

def make_data(result):
    data = pd.DataFrame()
    gill_size_data = ['b', 'n']
    gill_color_data = ['b', 'e', 'g', 'h', 'k', 'n' ,'o', 'p' ,'r', 'u', 'w' ,'y']
    buries_data = ['f', 't']
    stalk_shape_data = ['e', 't']
    stalk_color_above_ring = ['b', 'c', 'e' ,'g', 'n', 'o', 'p', 'w', 'y']

    gill_size = result['gill-size']
    gill_color = result['gill-color']
    bruises = result['bruises']
    stalk_shape = result['stalk-shape']
    stalk_ring = result['stalk-color-above-ring']

    for i in gill_size_data:
        if gill_size == i:
            data['gill-size_'+i] = 1
        else:
            data['gill-size_'+i] = 0

    for i in gill_color_data:
        if gill_color == i:
            data['gill_color_'+i] = 1
        else:
            data['gill_color_'+i] = 0

    for i in buries_data:
        if bruises == i:
            data['buries_'+i] = 1
        else:
            data['buries_'+i] = 0
        
    for i in stalk_shape_data:
        if stalk_shape == i:
            data['stalk-shape_'+i] = 1
        else:
            data['stalk-shape_'+i] = 0

    for i in stalk_color_above_ring:
        if stalk_ring == i:
            data['stalk-color-above-ring_'+i] = 1
        else:
            data['stalk-color-above-ring_'+i] = 0
    print(data.head())
    return data

if __name__=="__main__":
    f = open("static/model.pkl", 'rb')
    model = pickle.load(f)
    f.close()
    app.run(debug=True, host="0.0.0.0")
