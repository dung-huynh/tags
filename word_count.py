import io
import os

# Imports the Google Cloud client library
from collections import Counter
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

path = '/home/osama/Desktop/Hackathons/jacobsHack/tags/frames/'
frames = {}
objects = []
total = {}
counter = 1

#iterating over every frame in a folder
for frame in os.listdir(path):
    file_name = os.path.join(os.path.dirname(path), frame)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image, max_results=20)
    labels = response.label_annotations
    
    objects += [x.description for x in labels]    

    #printing the objects in each frame
    frames[counter] = ([x.description for x in labels])
    counter += 1

#total = ((x,objects.count(x)) for x in set(objects))
print(frames)
print('')
print(Counter(objects))
print('')