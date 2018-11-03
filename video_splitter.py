import cv2, os, sys

#videoName needs to become input.
#step 1: Take video, make a new directory for images
videoName = 'Mortal Engines - Official Trailer (HD).mp4'
directoryName = videoName[:10]+"Frames"
vidcap = cv2.VideoCapture(videoName)
try:
  os.makedirs(directoryName)
except:
  print("Error creating directory")
  sys.exit()

#step2: Loop over all frames. Every tenth frame, save.
success,image = vidcap.read()
count = 0
i = 0
while success:
  if i % 10 == 0:
    cv2.imwrite(directoryName + "/frame_%d.jpg" % count, image)     # save frame as JPEG file
    count += 1
  success,image = vidcap.read()
  i += 1