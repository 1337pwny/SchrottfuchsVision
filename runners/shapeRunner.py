import cv2
import numpy as np
import imutils
from classes.TemplateClass import TemplateClass

def search(egdedFrame, templateObject, message, qualityThreshold):
    found = None
    templateCanny = templateObject.canny
    cv2.waitKey(1)

    r = templateObject.r
    result = cv2.matchTemplate(egdedFrame, templateCanny, cv2.TM_CCOEFF_NORMED)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

    #print(maxVal)
    if maxVal > qualityThreshold:

        cv2.waitKey(1)
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)

    clone = np.dstack([egdedFrame, egdedFrame, egdedFrame])
    cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),(maxLoc[0] + templateObject.tW, maxLoc[1] + templateObject.tH), (0, 0, 255), 2)
    if found is not None:
        #print("##################################################")
        #print("--- "+message+" ---")
        #print("##################################################")
        #cv2.waitKey(0)
        return True