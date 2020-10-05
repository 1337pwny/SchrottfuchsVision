# import the necessary packages
import numpy as np
import argparse
import imutils
import glob
import cv2


visualize = True
possibilityThreshold=0.29
frameTreshold=0
possibilityThresholdFine=0.20

def fineSearch(source, template, message, qualityThreshold):
    found = None
    clone = None
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    templateCanny = cv2.Canny(template, 100, 200)
    #cv2.imshow("Template2", templateCanny)
    cv2.waitKey(1)
    for scale in np.linspace(0.6, 0.8, 3)[::-1]:

        resizedTemplate = imutils.resize(templateGray, width=int(templateGray.shape[1] * scale))
        r = templateGray.shape[1] / float(resizedTemplate.shape[1])
        templateCanny = cv2.Canny(resizedTemplate, 100, 200)

        result = cv2.matchTemplate(edged, templateCanny, cv2.TM_CCOEFF_NORMED)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)


        #print(maxVal)
        if maxVal > qualityThreshold:

            cv2.waitKey(1)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)

        clone = np.dstack([edged, edged, edged])
        cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                      (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
    if found is not None:
        print("##################################################")
        print("--- "+message+" ---")
        print("##################################################")
        #cv2.imshow("Fine", clone)
        cv2.waitKey(0)
        return True
        #print("Safety: " + str(maxVal))
        #print("Scaling: " + str(scale))




cap = cv2.VideoCapture('fahrt.mp4')


# load the image image, convert it to grayscale, and detect edges
template = cv2.imread("sign2.jpg")
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
templateCanny = cv2.Canny(template, 100, 200)
(tH, tW) = template.shape[:2]
#cv2.imshow("Template", templateCanny)
cv2.waitKey(1)
frameCount=0

while(True):
    frameCount+=1
    ret, frame = cap.read()
    image = frame
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 100, 200)
    found = None
    clone = None
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





