import tkinter as tk
from PIL import ImageTk,Image
# ToDo make this a class and do updates in the main.py
# ToDo make setters for the states
# ToDo Write constructor for initializing stuff
globalWidht=160
globalHeight=160
# ToDo change this var to the state
laneAssistState="1"

laneStateDict = {
  "1": "Ready!",
  "2": "All OK!",
  "3": "Right Fail!"
}
laneImageDict = {
  "1": "images/lane_empty.png",
  "2": "images/lane_left_right_ok.png",
  "3": "images/lane_left_ok.png"
}
# ToDo change this var to the state
SignAssistState="2"

signStateDict = {
  "1": "No Sign",
  "2": "30 KM/h",
  "3": "50 KM/h"
}
signImageDict = {
  "1": "images/sign_failed.png",
  "2": "images/30.png",
  "3": "images/50.png"
}

window = tk.Tk()
infoLabel = tk.Label(bg="black",fg="red",width=int(globalWidht/7),text="Schrottfuchs-vision 1.0")
infoLabel.pack()
laneCanvas = tk.Canvas(width = globalWidht, height = globalHeight,bg="black")
laneCanvas.pack()
imgLane = ImageTk.PhotoImage(Image.open(laneImageDict[laneAssistState]))
laneCanvas.create_image(globalWidht/2,globalHeight/2,anchor=tk.CENTER, image=imgLane)
laneLabel = tk.Label(bg="black",fg="red",width=int(globalWidht/7),text=laneStateDict[laneAssistState])
laneLabel.pack()


signCanvas = tk.Canvas(width = globalWidht, height = globalHeight,bg="black")
signCanvas.pack()
imgSign = ImageTk.PhotoImage(Image.open(signImageDict[SignAssistState]))
signCanvas.create_image(globalWidht/2,globalHeight/2,anchor=tk.CENTER, image=imgSign)
signLabel = tk.Label(bg="black",fg="red",width=int(globalWidht/7),text=signStateDict[SignAssistState])
signLabel.pack()
# ToDo Kill this and write uodate function see https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
window.mainloop()