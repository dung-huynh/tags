import json
import requests
import os
import jinja2
from flask import Flask, render_template, request

# from scene import SceneAnnotator
# from tags import annotate

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader('templates'))
app = Flask(__name__)
extensions = ['.webm', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.mpg','.mpeg','.m2v','.3gp','mp4']

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/',methods = ['POST'])
# def form():
#     # get url of video link
#     url = request.form['link']

#     # check whether the link refers to a valid video file
#     video = url.split('/')[-1]
#     if video.split('.')[-1] not in extensions:
#        return "Invalid file format"
    
#     # create response object 
#     res = requests.get(url, stream = True) 
        
#     # download and save the video
#     filename = "../videos/video" + video.split('.')[-1];
#     with open(filename, 'wb') as file: 
#         for chunk in res.iter_content(chunk_size = 1024*1024): 
#             if chunk: 
#                 file.write(chunk)

#     # annotate video
#     path = '../frames/'      # relative to the 'app' directory
#     skip = 10
#     scenes = annotate(path, filename, skip)
    
#     return render_template('output.html', data = SceneAnnotator.to_dict(scenes), link = url)

app.run()