import scene_separator



def convert(scenes):
    output = {}
    counter = 1
    for scene in scenes:
        output['scene' + str(counter)] = list(scene.words.keys())
        counter += 1
    return output

def trial2():
    scenes = scene_separator.trial()
    a = convert(scenes)
    return a
