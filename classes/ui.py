import tkinter as tk
from PIL import ImageTk, Image

#globalWidht = 160
#globalHeight = 160
class UIClass:
    def __init__(self, width, height):
        self.globalWidht = width
        self.globalHeight = height
        self.laneAssistState = "1"
        self.SignAssistState = "2"
        self.additionalSignAssistState = "2"
        self.distanceAssistState = "1"

        self.laneStateDict = {
            "1": "Ready!",
            "2": "All OK!",
            "3": "Right Fail!"
        }
        self.laneImageDict = {
            "1": "ui/images/lane_empty.png",
            "2": "ui/images/lane_left_right_ok.png",
            "3": "ui/images/lane_left_ok.png"
        }

        self.signStateDict = {
            "1": "No Sign",
            "2": "30 KM/h",
            "3": "50 KM/h"
        }
        self.signImageDict = {
            "1": "ui/images/sign_failed.png",
            "2": "ui/images/30.png",
            "3": "ui/images/50.png"
        }

        self.additionalSignStateDict = {
            "1": "No Sign",
            "2": "No Overtaking!",
        }
        self.additionalSignImageDict = {
            "1": "ui/images/sign_failed.png",
            "2": "ui/images/no_overtake.png",
        }

        self.distanceStateDict = {
            "1": "Nothing there",
            "2": "OK",
            "3": "NOT OK",
        }
        self.distanceImageDict = {
            "1": "ui/images/distance_no.png",
            "2": "ui/images/distance_ok.png",
            "3": "ui/images/distance_to_close.png",
        }

        self.window = tk.Tk()
        self.infoLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text="Schrottfuchs-vision 1.0")
        self.infoLabel.pack()

        self.laneCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.laneCanvas.pack()
        self.imgLane = ImageTk.PhotoImage(Image.open(self.laneImageDict[self.laneAssistState]))
        self.laneCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgLane)
        self.laneLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=self.laneStateDict[self.laneAssistState])
        self.laneLabel.pack()

        self.signCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.signCanvas.pack()
        self.imgSign = ImageTk.PhotoImage(Image.open(self.signImageDict[self.SignAssistState]))
        self.signCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgSign)
        self.signLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=self.signStateDict[self.SignAssistState])
        self.signLabel.pack()

        self.additionalSignCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.additionalSignCanvas.pack()
        self.imgAdditionalSign = ImageTk.PhotoImage(Image.open(self.additionalSignImageDict[self.additionalSignAssistState]))
        self.additionalSignCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgAdditionalSign)
        self.additionalSignLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=self.additionalSignStateDict[self.additionalSignAssistState])
        self.additionalSignLabel.pack()

        self.distanceCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.distanceCanvas.pack()
        self.imgDistance = ImageTk.PhotoImage(Image.open(self.distanceImageDict[self.distanceAssistState]))
        self.distanceCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgDistance)
        self.distanceLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=self.distanceStateDict[self.distanceAssistState])
        self.distanceLabel.pack()

        self.window.update_idletasks()
        self.window.update()

    def updateLaneState(self, laneState):
        self.laneAssistState = laneState
        self.imgLane = ImageTk.PhotoImage(Image.open(self.laneImageDict[self.laneAssistState]))
        self.laneCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgLane)
        self.laneLabel['text'] = self.laneStateDict[self.laneAssistState]
        self.window.update_idletasks()
        self.window.update()

    def updateSignState(self, SignState):
        self.SignAssistState = SignState
        self.imgSign = ImageTk.PhotoImage(Image.open(self.signImageDict[self.SignAssistState]))
        self.signCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgSign)
        self.signLabel['text'] = self.signStateDict[self.SignAssistState]
        self.window.update_idletasks()
        self.window.update()

    def updateAdditionalSignState(self, SignState):
        self.additionalSignAssistState = SignState
        self.imgAdditionalSign = ImageTk.PhotoImage(Image.open(self.additionalSignImageDict[self.additionalSignAssistState]))
        self.additionalSignCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgAdditionalSign)
        self.additionalSignLabel['text'] = self.additionalSignStateDict[self.additionalSignAssistState]
        self.window.update_idletasks()
        self.window.update()

    def updateDistanceState(self, DistanceState):
        self.distanceAssistState = DistanceState
        self.imgDistance = ImageTk.PhotoImage(Image.open(self.distanceImageDict[self.distanceAssistState]))
        self.distanceCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgDistance)
        self.distanceLabel['text'] = self.distanceStateDict[self.distanceAssistState]
        self.window.update_idletasks()
        self.window.update()