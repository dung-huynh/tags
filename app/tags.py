# Before starting: you must change all of the user-defined parameters at the bottom of the script!

import cv2, os, sys

from file import File
from scene import SceneAnnotator
from frame import FrameAnnotator

def annotate(path, filename, skip):
    frames = []

    # check whether the frames folder existed, if not, create
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except:
            sys.exit()

    # create a VideoCapture object for reading frames 
    # and retrieve its intrinsic parameters
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_XI_FRAMERATE)
    frames_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    # print('frame rate: %f' % fps)

    # read and export every nth frame from the video
    frame_index = 0
    success, image = video.read()
    while success:
        if frame_index % skip == 0:
            # show process
            print('dividing video into frames: {:.3%}'.format(float(frame_index/frames_count)), end='\r')

            # write image
            cv2.imwrite(path + "/%d.jpg" % int(frame_index/skip), image)
        frame_index += 1
        success, image = video.read()
    print()

    # find all words in each frame
    count = 0
    files = File.get_files(path, '.jpg', File.get_named)
    for file in files:
        # show process
        print('annotating frames: {:.3%}'.format(float(count/len(files))), end='\r')

        # annotate image and append it to the list of frames
        frames.append(FrameAnnotator.annotate(File.get_content(path, file)))

        count += 1
    print()

    # group scenes that share common words
    error = 0.7
    scenes = SceneAnnotator.group(frames, error)

    # get real frame index
    for scene in scenes:
        # print words in scene
        scene.show()
        scene.start *= skip
        scene.end *= skip

    return scenes

# CHANGE HERE
path = '../frames/'
filename = '../videos/desert.mp4'
skip = 50
annotate(path, filename, skip)