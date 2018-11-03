# each frame might have different amount of words

# threshold to determine how much errors determining the scene change
max_error = 8

class Scene:
    def __init__(self, start_frame, words):
        self.interval = [start_frame, None]    # list
        self.words = {word: 1 for word in words}    # dict

def print_scene(scene):
    print("From frame {} to frame {}, there are".format(scene.interval[0], scene.interval[1]))
    for word, count in scene.words.items():
        print(word, count)

def separate(frames):
    # intialize the first scene
    scenes = [Scene(0, frames[0])]

    # each frame contains 10 words
    for fi in range(1, len(frames)):
        scene = set(scenes[-1].words) 
        frame = set(frames[fi])

        # get the groups of words: shared and exclusive
        shared_words = scene.intersection(frame)
        exclusive_words = frame.difference(scene)

        # absolute change: change scene (significant change)
        if len(exclusive_words) >= max_error:
            scenes[-1].interval[1] = fi

            # sort from max to min counts
            scenes[-1].words = dict(sorted(scenes[-1].words.items(), key=lambda kv: kv[1], reverse=True))

            scenes.append(Scene(fi, frames[fi]))

        # relative change: stay in the same scene
        else:
            # increment each shared word
            for word in shared_words:
                scenes[-1].words[word] += 1

            # add new words
            for word in exclusive_words:
                scenes[-1].words[word] = 1
    scenes[-1].interval[1] = len(frames)-1

    return scenes

# sample set
sample = [["people", "table", "food", "dog", "spoon", "coffee", "chicken", "light", "plate", "tv"], 
["man", "shirt", "table", "food", "chicken", "glasses", "cup", "knife", "hair", "books"],
["woman", "shoes", "table", "food", "dog", "coffee", "light", "spoon", "fork", "plate"],
["kid", "shoes", "ball", "hat", "backpack", "table", "light", "food", "books", "door"],
["car", "street", "sky", "cloud", "sun", "light", "door", "house", "grass", "tree"],
["car", "wheel", "street", "light", "sky", "house", "man", "woman", "kid", "key"]]

for scene in separate(sample):
    print_scene(scene)
    print()