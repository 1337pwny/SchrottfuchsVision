# import the necessary packages
import numpy as np
import imutils
import cv2
from classes.BasicSign import BasicSign
from runners.shapeRunner import search

registeredObjects = [BasicSign(3, "30 KM/h", "assets/thirtySign.png")]
registeredShapes = [BasicSign(2, "PLACEHOLDER", "assets/basicSignRound.png")]


#Todo Cleanup Main


# Load Video File
# ToDo: Implement switch for video file or live video
cap = cv2.VideoCapture('fahrt.mp4')

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

    # ToDo: only doing one shape template since there is no other
    for baseTemplate in registeredShapes[0]:
        foundShape = search(edged,baseTemplate, baseTemplate[0].message, baseTemplate[0].threshold)
        # ToDo check if foundShape is true, if, then do fine Search
        # ToDo Finesearch in multithread
        # ToDo Implement result in search


    for scale in np.linspace(0.6, 0.75, 2)[::-1]:

        resizedTemplate = imutils.resize(template, width=int(template.shape[1] * scale))
        r = template.shape[1] / float(resizedTemplate.shape[1])
        templateCanny = cv2.Canny(resizedTemplate, 100, 200)
        #cv2.imshow("template", templateCanny)
        #cv2.waitKey(1)

        result = cv2.matchTemplate(edged, templateCanny, cv2.TM_CCORR_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        #r = gray.shape[1]

        #print(maxVal)
        if maxVal > possibilityThreshold:
            #print("Safety: "+str(maxVal))
            #print("Scaling: "+str(scale))
            cv2.waitKey(1)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)

            clone = np.dstack([edged, edged, edged])
            cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                          (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
        else:
            clone = np.dstack([edged, edged, edged])


    cv2.imshow("Visualize", clone)
    cv2.waitKey(1)

    if found is None:
        #print("no match")
        cv2.imshow("Image", image)
        cv2.waitKey(1)
    elif frameCount > frameTreshold:
        frameCount = 0
        (_, maxLoc, r) = found
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

        thirtyTemplate=cv2.imread("30orig.jpg")
        parkTemplate=cv2.imread("park1.jpg")
        thirty=fineSearch(image,thirtyTemplate,"Bitte fahren Sie 30!",0.20)
        fineSearch(image, parkTemplate, "Parkverbot!", 0.24)
        if thirty is True:
            input("Press Enter to exit")
            exit()

        # draw a bounding box around the detected result and display the image
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
        cv2.imshow("Image", image)
        cv2.waitKey(1)