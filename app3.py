import os, sys, shutil, time

from flask import Flask, request, jsonify, render_template,send_from_directory
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import urllib.request
import json
from geopy.geocoders import Nominatim
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle


app = Flask(__name__)



@app.route('/')
def root():
    return render_template('index.html')

@app.route('/images/<Paasbaan>')
def download_file(Paasbaan):
    return send_from_directory(app.config['images'], Paasbaan)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/result.html', methods = ['POST'])
def predict():
   def predict():
    lrm = joblib.load('model.pkl')
    print('model loaded')

    if request.method == 'POST':

        address2 = request.form['Location2']
        geolocator = Nominatim()
        location = geolocator.geocode(address,timeout=None)
        print(location.address)
        lat=[location.latitude]
        log=[location.longitude]
       

        DT= request.form['Year']
        #arr=lat,log,DT
        #my_prediction=lrm.predict(np.array([[arr[0],arr[1],arr[2]]]))
        my_prediction=100

    return render_template('result2.html', prediction = my_prediction)




if __name__ == '__main__':
    app.run(debug = True)
