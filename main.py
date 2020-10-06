# import the necessary packages
import numpy as np
import time
import imutils
import cv2
from classes.BasicSign import BasicSign
from runners.shapeRunner import search
from _thread import start_new_thread
######## Configuration ##########

### Basic options
# Filename for the input source
videoFile = "assets/fahrt1.mp4"
# Wether there should be a visualization
visualise = True
# use multithreading for the search of an object (Shape search will not be affected by this setting)
# ToDo: Does not work because QObject::startTimer: Timers cannot be started from another thread
multithreading = False
# Crop the input source to a specific area (Parameters for the area in the image options)
crop = False

### Image options
# Crop parameters
xStart = 200
xStop = 500
yStart = 100
yStop = 550
# Which fot you want to use for overlays
font = cv2.FONT_HERSHEY_SIMPLEX

### Register your shapes and objects here
# ToDo: Add output in shape handling for signs that can be determined only by shape
# ToDo: Add paramenter to sign definition, if the sign overides speed limit, to avoid a parkverbot sign overriding the 30 sign
registeredObjects = [BasicSign(4, "Parkverbot", "assets/park.jpg",0.21, "signpark"), BasicSign(4, "30 KM/h", "assets/thirtySign.jpg",0.20, "sign30")]
registeredShapes = [BasicSign(2, "PLACEHOLDER", "assets/sign2.jpg", 0.25, "shapeRound")]

####### End Configuration #######



# Load Video File
# ToDo: Implement switch for video file or live video
cap = cv2.VideoCapture(videoFile)
# Without this OpenCV wont work
cv2.waitKey(1)
# Internal variables
frameCount = 0
currentTimestamp = int(time.time() * 1000)
lastUpdateTimestamp = int(time.time() * 1000)
fps = 0


while True:
    frameCount+=1
    ret, frame = cap.read()
    image = frame
    if crop is True:
        # ToDo: Fix cropping, copy original image for visualize funktion, so orignial video is always shown (cropped only for the edged view)
        image = image[yStart:yStop, xStart:xStop]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 100, 200)
    found = None
    clone = None
    clone = np.dstack([edged, edged, edged])


    for shape in registeredShapes:
        for baseTemplate in shape.templateList:
            foundShape = search(edged, baseTemplate, shape.message, shape.threshold, False)
            if foundShape is not None:
                for sign in registeredObjects:
                    for signTemplate in sign.templateList:
                        if multithreading is True:
                            start_new_thread(search, (edged, signTemplate, sign.message, sign.threshold, True,))
                        # If multithreading is on, you cant use visualisation of the found object, since there is no return value atm
                        if visualise is True and multithreading is False:
                            foundObject = search(edged, signTemplate, sign.message, sign.threshold, True)
                            if foundObject is not None:
                                (_, maxVal, _, maxLoc) = cv2.minMaxLoc(foundObject)
                                cv2.rectangle(clone, (maxLoc[0], maxLoc[1]), (maxLoc[0] + signTemplate.tW, maxLoc[1] + signTemplate.tH),(0, 0, 255), 2)
                                cv2.imshow("Visualize", clone)
                                cv2.waitKey(0)

        if visualise is True:
            currentTimestamp = int(time.time() * 1000)
            timediff = currentTimestamp - lastUpdateTimestamp
            if timediff > 1000:
                fps = int(frameCount / (timediff/1000))
                frameCount = 0
                lastUpdateTimestamp = int(time.time() * 1000)
            cv2.putText(image, "FPS"+str(fps), (10, 60), font, 2, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow("Visualize", clone)
            cv2.imshow("Image", image)
        cv2.waitKey(1)
