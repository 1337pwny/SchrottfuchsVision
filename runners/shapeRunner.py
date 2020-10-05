import cv2
import numpy as np
import imutils
from classes.TemplateClass import TemplateClass

def search(egdedFrame, templateObject, message, qualityThreshold, printMessage):
    found = None
    templateCanny = templateObject.canny
    cv2.waitKey(1)

    r = templateObject.r
    result = cv2.matchTemplate(egdedFrame, templateCanny, cv2.TM_CCOEFF_NORMED)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

    if maxVal > qualityThreshold:
        if printMessage is True:
            print("##################################################")
            print("--- "+message+" ---")
            print("##################################################")
        return result
    return None
