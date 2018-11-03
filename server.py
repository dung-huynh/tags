import json
import requests
from flask import Flask, render_template, request, redirect, url_for
import os
import jinja2

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('templates'))

app = Flask(__name__)

extensions = ['.webm', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.mpg','.mpeg','.m2v','.3gp','mp4']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods = ['POST'])
def form():
    video_url = request.form['text']
    r = requests.get(video_url)
    video_file = video_url.split('/')[-1]
    #yield "Downloading file: "  + video_file + '\n'
    if video_file.split('.')[-1] not in extensions:
        return "Invalid file format"
    # create response object 
    r = requests.get(video_url, stream = True) 
        
    # download started 
    with open(video_file, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 
        
    return render_template('output.html')

app.run(debug = True)

