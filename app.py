#-*- coding:utf-8 -*-
from flask import Flask, render_template
import os

app = Flask(__name__)

#메인 페이지  
@app.route("/")
def home():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
