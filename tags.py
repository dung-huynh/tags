from scenes_separator import annotate_scenes, print_scene
from word_count import annotate_frames
from video_splitter import split_video

def annotate():
    path = '../frames/'
    filename = '../videos/gone_girl.mp4'
    skip = 10

    # split the video into frames and put them into the specified folder
    split_video(filename, path, skip)

    # find all words in each frame
    frames = annotate_frames(path)

    # check for groups of scenes
    scenes = annotate_scenes(frames)

    for scene in scenes:
        print_scene(scene)

annotate()