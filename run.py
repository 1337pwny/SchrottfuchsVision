from classes.Variables import Variables
from classes.ui import UIClass
import numpy as np
import time
import imutils
import cv2
from classes.BasicSign import BasicSign
from runners.shapeRunner import search
from _thread import start_new_thread
vars = Variables()
#ui = UIClass(160, 160, vars)

if vars.useSingleCam == "true":
    # Usinging only one cam
    if vars.filebaseMode == "true":
        cap = cv2.VideoCapture(vars.videoFileSigleCam)
        print(vars.videoFileSigleCam)
    else:
        cap = cv2.VideoCapture(1)


    # Load Video File
    while True:
        ret, frame = cap.read()

        imageLane = frame[vars.laneCamCropYStart:vars.laneCamCropYStop, vars.laneCamCropXStart:vars.laneCamCropXStop]
        imageSign = frame[vars.signCamCropYStart:vars.signCamCropYStop, vars.signCamCropXStart:vars.signCamCropXStop]
        #cv2.imshow("sign", imageSign)
        alpha = 2  # Contrast control (1.0-3.0)
        beta = 50  # Brightness control (0-100)
        imageLane = cv2.convertScaleAbs(imageLane, alpha=alpha, beta=beta)
        cv2.imshow("Lane", imageLane)
        grayLane = cv2.cvtColor(imageLane, cv2.COLOR_BGR2GRAY)


        grayLane = cv2.convertScaleAbs(grayLane, alpha=alpha, beta=beta)
        edgedLane = cv2.Canny(grayLane, 100, 200)
        graySign = cv2.cvtColor(imageSign, cv2.COLOR_BGR2GRAY)
        edgedSign = cv2.Canny(graySign, 100, 200)
        #cv2.imshow("edgedLane", edgedLane)
        #cv2.imshow("edgedsign", edgedSign)
        key = cv2.waitKey(1)
        if key == 27:
            break

else:
    print("not implemented")