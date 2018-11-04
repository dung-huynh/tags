#Parameter: "False scenes"
#Process : merge similar scenes together
#Return : True scenes
def merge(scenes):
    true_scenes = []
    s = scenes[0]
    #merge scenes if len(diff) > len(common)
    for scene in scenes[1:]:
        for _ in range(min(len(scene.words.keys()), len(s.words.keys()))):
            common = set(scene.words.keys()).intersection(set(s.words.keys()))
            diff = set(scene.words.keys()).difference(set(s.words.keys()))

            if len(common) > len(diff):
                s.words.update(scene.words)
            else:
                true_scenes.append(s)
                s = scene
    
    return true_scenes
            

