# import the necessary packages
import numpy as np
import imutils
import cv2
from classes.BasicSign import BasicSign
from runners.shapeRunner import search

registeredObjects = [BasicSign(3, "30 KM/h", "assets/thirtySign.jpg",0.20, "sign30")]
registeredShapes = [BasicSign(2, "PLACEHOLDER", "assets/sign2.jpg", 0.25, "shapeRound")]


# Load Video File
# ToDo: Implement switch for video file or live video
cap = cv2.VideoCapture('assets/fahrt1.mp4')

cv2.waitKey(1)
frameCount = 0

while(True):
    frameCount+=1
    ret, frame = cap.read()
    image = frame
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 100, 200)
    found = None
    clone = None
    clone = np.dstack([edged, edged, edged])

    # ToDo: only doing one shape template since there is no other
    for baseTemplate in registeredShapes[0].templateList:
        foundShape = search(edged, baseTemplate, registeredShapes[0].message, registeredShapes[0].threshold, False)

        if foundShape is not None:
            print("Found Shape")
            for signTemplate in registeredObjects[0].templateList:
                foundObject = search(edged, signTemplate, registeredObjects[0].message, registeredObjects[0].threshold, True)
                if foundObject is not None:
                    print("found object")
                    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(foundObject)
                    cv2.rectangle(clone, (maxLoc[0], maxLoc[1]), (maxLoc[0] + signTemplate.tW, maxLoc[1] + signTemplate.tH),(0, 0, 255), 2)
                    cv2.imshow("Visualize", clone)
                    cv2.waitKey(0)
            # ToDo Finesearch in multithread

        cv2.imshow("Visualize", clone)
        cv2.waitKey(1)
