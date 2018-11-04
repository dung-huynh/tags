import json
import requests
from flask import Flask, render_template, request, redirect, url_for
import os
import jinja2
import scenes_to_json


jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('templates'))

app = Flask(__name__)

extensions = ['.webm', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.mpg','.mpeg','.m2v','.3gp','mp4']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods = ['POST'])
def form():
    #Get url from html form
    video_url = request.form['link']

    #Check if link refers to a valid video file
    video_file = video_url.split('/')[-1]
    if video_file.split('.')[-1] not in extensions:
       return "Invalid file format"
    
    # create response object 
    r = requests.get(video_url, stream = True) 
        
    # download started 
    with open("video" + video_file.split('.')[-1], 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
    
    return render_template('output.html', data = scenes_to_json.trial2(), link = video_url)

app.run(debug = True)

