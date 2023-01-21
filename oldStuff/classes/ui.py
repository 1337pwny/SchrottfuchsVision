import tkinter as tk
from PIL import ImageTk, Image
import playsound

class UIClass:
    def playAudio(self, filename):
        if self.variables.audio == "true" and filename != "None":
            print("playing Sound")
            playsound.playsound(filename)

    def __init__(self, width, height, variables):
        self.globalWidht = width
        self.globalHeight = height
        self.laneAssistState = "lane_ready"
        self.SignAssistState = "sign_failed"
        self.additionalSignAssistState = "sign_failed"
        self.distanceAssistState = "distance_ok"
        self.variables = variables

        self.window = tk.Tk()
        self.infoLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text="Schrottfuchs-vision 1.0")
        self.infoLabel.pack()

        image = self.variables.getUiElementByName(self.laneAssistState).elementImage
        text = self.variables.getUiElementByName(self.laneAssistState).elementText
        self.laneCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.laneCanvas.pack()
        self.imgLane = ImageTk.PhotoImage(Image.open(image))
        self.laneCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgLane)
        self.laneLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=text)
        self.laneLabel.pack()

        image = self.variables.getUiElementByName(self.SignAssistState).elementImage
        text = self.variables.getUiElementByName( self.SignAssistState).elementText
        self.signCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.signCanvas.pack()
        self.imgSign = ImageTk.PhotoImage(Image.open(image))
        self.signCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgSign)
        self.signLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=text)
        self.signLabel.pack()

        image = self.variables.getUiElementByName(self.additionalSignAssistState).elementImage
        text = self.variables.getUiElementByName(self.additionalSignAssistState).elementText
        self.additionalSignCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.additionalSignCanvas.pack()
        self.imgAdditionalSign = ImageTk.PhotoImage(Image.open(image))
        self.additionalSignCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgAdditionalSign)
        self.additionalSignLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=text)
        self.additionalSignLabel.pack()

        image = self.variables.getUiElementByName(self.distanceAssistState).elementImage
        text = self.variables.getUiElementByName(self.distanceAssistState).elementText
        self.distanceCanvas = tk.Canvas(width=self.globalWidht, height=self.globalHeight, bg="black")
        self.distanceCanvas.pack()
        self.imgDistance = ImageTk.PhotoImage(Image.open(image))
        self.distanceCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgDistance)
        self.distanceLabel = tk.Label(bg="black", fg="red", width=int(self.globalWidht / 7), text=text)
        self.distanceLabel.pack()

        self.window.update_idletasks()
        self.window.update()

    def updateLaneState(self, laneState):
        self.laneAssistState = laneState
        uiElement = self.variables.getUiElementByName(self.laneAssistState)
        image = uiElement.elementImage
        text = uiElement.elementText
        audio = uiElement.elementSound
        self.imgLane = ImageTk.PhotoImage(Image.open(image))
        self.laneCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgLane)
        self.laneLabel['text'] = text
        self.window.update_idletasks()
        self.window.update()
        self.playAudio(audio)

    def updateSignState(self, SignState):
        self.SignAssistState = SignState
        uiElement = self.variables.getUiElementByName(self.SignAssistState)
        image = uiElement.elementImage
        text = uiElement.elementText
        audio = uiElement.elementSound
        self.imgSign = ImageTk.PhotoImage(Image.open(image))
        self.signCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgSign)
        self.signLabel['text'] = text
        self.window.update_idletasks()
        self.window.update()
        self.playAudio(audio)

    def updateAdditionalSignState(self, SignState):
        self.additionalSignAssistState = SignState
        uiElement = self.variables.getUiElementByName(self.additionalSignAssistState)
        image = uiElement.elementImage
        text = uiElement.elementText
        audio = uiElement.elementSound
        self.imgAdditionalSign = ImageTk.PhotoImage(Image.open(image))
        self.additionalSignCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgAdditionalSign)
        self.additionalSignLabel['text'] = text
        self.window.update_idletasks()
        self.window.update()
        self.playAudio(audio)

    def updateDistanceState(self, DistanceState):
        self.distanceAssistState = DistanceState
        uiElement = self.variables.getUiElementByName(self.distanceAssistState)
        image = uiElement.elementImage
        text = uiElement.elementText
        audio = uiElement.elementSound
        self.imgDistance = ImageTk.PhotoImage(Image.open(image))
        self.distanceCanvas.create_image(self.globalWidht / 2, self.globalHeight / 2, anchor=tk.CENTER, image=self.imgDistance)
        self.distanceLabel['text'] = text
        self.window.update_idletasks()
        self.window.update()
        self.playAudio(audio)