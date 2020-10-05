import cv2
import imutils
import numpy as np
from classes.TemplateClass import TemplateClass

class BasicSign:
    def __init__(self, resizeStages, message, templateImage):
        self.threshold = 0.29
        self.message = message
        self.templateFile = templateImage
        self.templateList = []
        # Converting the image
        print("Processing template BasicSignRound")
        template = cv2.imread(self.templateFile)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        # Resizing template and saving as list
        for scale in np.linspace(0.6, 0.75, resizeStages)[::-1]:
            resizedTemplate = imutils.resize(template, width=int(template.shape[1] * scale))
            r = template.shape[1] / float(resizedTemplate.shape[1])
            templateCanny = cv2.Canny(resizedTemplate, 100, 200)
            self.templateList.append(TemplateClass(template, templateCanny, r))
