import tkinter as tk
from tkdial import Meter
from PIL import ImageTk, Image


class UIElement:
    def __init__(self, name, posX, posY, sizeX, sizeY, textContent, contentType, value=0, imageFile = "null", unit="", maxVal=100):
        self.posX=posX
        self.name = name
        self.posY = posY
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.imageFile = imageFile
        self.textContent = textContent
        self.contentType = contentType
        self.value = value
        self.unit = unit
        self.maxVal = maxVal

    def setContent(self, imageFile="", textContent="", value=0):
        self.imageFile = imageFile
        self.textContent = textContent
        self.value = value



class DisplayUI:
    def updateTKUIElementGraph(self, uiElementName):
        try:
            uiElement = self.uiElementDict[uiElementName]
        except Exception as err:
            print("UI Element "+uiElementName+" not found....")
            return
        canvasName = uiElementName + "_canvas"
        labelName = uiElementName + "_label"
        imageName = uiElementName + "_image"
        img = ImageTk.PhotoImage(Image.open(uiElement.imageFile))
        self.uiTKDict[imageName] = img
        self.uiTKDict[canvasName].create_image(uiElement.sizeX/2, uiElement.sizeY/2,anchor=tk.CENTER, image=self.uiTKDict[imageName])
        self.uiTKDict[labelName]['text'] = uiElement.textContent
        labelWidth = self.uiTKDict[labelName].winfo_reqwidth()
        labelPosX = (uiElement.sizeX - labelWidth) / 2
        labelPosX = int(labelPosX + uiElement.posX)
        self.uiTKDict[labelName].place(x=labelPosX, y=uiElement.posY + uiElement.sizeY + 1)

    def updateTKUIElementGauge(self, uiElementName):
        try:
            uiElement = self.uiElementDict[uiElementName]
        except Exception as err:
            print("UI Element "+uiElementName+" not found....")
            return
        self.uiTKDict[uiElementName+"_gauge"].set(uiElement.value)


    def createUIElements(self):
        for name in self.uiElementDict:
            uiElem = self.uiElementDict[name]
            canvasName = name + "_canvas"
            labelName = name + "_label"
            canvas = tk.Canvas(width=uiElem.sizeX - 1, height=uiElem.sizeY + 20, bg="black")
            if uiElem.contentType == "graph":
                imageName = name + "_image"

                img = ImageTk.PhotoImage(Image.open(uiElem.imageFile).resize((uiElem.sizeX, uiElem.sizeY)))
                self.uiTKDict[imageName] = img
                canvas.create_image(uiElem.sizeX/2, uiElem.sizeY/2,anchor=tk.CENTER, image=self.uiTKDict[imageName])
            elif uiElem.contentType == "gauge":
                gaugeName = name + "_gauge"
                #gauge = tk_tools.Gauge(self.window, max_value=uiElem.maxVal, unit=uiElem.unit, width=uiElem.sizeX, height=uiElem.sizeY, bg="black")
                gauge = Meter(self.window,width=uiElem.sizeX-2, height=uiElem.sizeY-2, bg="black", radius=uiElem.sizeX, start=0, end=uiElem.maxVal, border_width=0,fg="black", text_color="white", start_angle=180, end_angle=-180,text_font="DS-Digital 10", scale_color="white", needle_color="red")
                gauge.set_mark(uiElem.maxVal-20, uiElem.maxVal)
                gauge.set(uiElem.value)
                gauge.place(x=uiElem.posX+1, y=uiElem.posY+1)
                self.uiTKDict[gaugeName] = gauge

            canvas.place(x=uiElem.posX, y=uiElem.posY)
            self.uiTKDict[canvasName] = canvas
            label = tk.Label(bg="black", fg="red", text=uiElem.textContent, anchor=tk.CENTER)
            labelWidth = label.winfo_reqwidth()
            labelPosX = (uiElem.sizeX - labelWidth) / 2
            labelPosX = int(labelPosX+uiElem.posX)
            label.place(x=labelPosX, y=uiElem.posY+uiElem.sizeY+1)

            self.uiTKDict[labelName] = label



    def __init__(self, uiElementList):
        self.uiElementDict = {}
        self.uiTKDict = {}
        for elem in uiElementList:
            self.uiElementDict[elem.name] = elem

        self.window = tk.Tk()
        self.window.geometry("1024x600")

        # Make it borderless
        #self.window.overrideredirect(True)
        self.window.configure(background='black')

        self.createUIElements()


        self.window.update_idletasks()
        self.window.update()

    def updateUIElementGraph(self, name, imageFile, textContent):
        try:
            uiElement = self.uiElementDict[name]
        except Exception as err:
            print("UI Element "+name+" not found....")
            return
        uiElement.setContent(imageFile, textContent)
        self.uiElementDict[name] = uiElement
        self.updateTKUIElementGraph(name)
        self.window.update_idletasks()
        self.window.update()

    def updateUIElementGauge(self, name, value):
        try:
            uiElement = self.uiElementDict[name]
        except Exception as err:
            print("UI Element "+name+" not found....")
            return
        uiElement.setContent(value=value)
        self.uiElementDict[name] = uiElement
        self.updateTKUIElementGauge(name)
        self.window.update_idletasks()
        self.window.update()
