# import flask class, and render template
from flask import Flask, render_template, redirect
import requests
import json
from pprint import pprint
# Create a Flask object; This is the main WSGI application;
# WSGI applications are standardized interfaces between
# Web servers and Python Web frameworks/applications;
app = Flask(__name__)

""" My Open Weather API Key """
OPEN_WEATHER_API_KEY = "b442adec22b775ed42e5f28172e5a43a"


def get_weather_json():
    """ Access the Open Weather API to grab weather in Raleigh """
    url = 'http://api.openweathermap.org/data/2.5/weather?id={id}&APPID={key}&units=imperial'
    url = url.format(id="4482348", key=OPEN_WEATHER_API_KEY)
    req = requests.get(url)

    """ Load request into json """
    return json.loads(req.content)


@app.route('/')
def index():
    weather_data = get_weather_json()
    return render_template('index.html', weather_data=weather_data)


@app.route('/contact')
def contact():

    return render_template('contact.html')


@app.route('/dyrenex')
def dyrenex():

    return redirect('http://www.dyrenex.com')


@app.route('/list_all')
def list_all():

    weather_data = get_weather_json()
    return render_template('list_all.html', weather_data=weather_data)


app.run(host='0.0.0.0', port=5000, debug=True)
