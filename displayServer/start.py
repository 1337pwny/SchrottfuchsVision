from displayUI import DisplayUI
from displayUI import UIElement
import time
import playsound


def playAudio(self, filename):
    if self.variables.audio == "true" and filename != "None":
        print("playing Sound")
        playsound.playsound(filename)


uiElements=[]
uiElements.append(UIElement("speed",10,0,145,120,textContent="Speed",contentType="gauge", maxVal=10))
uiElements.append(UIElement("load",170,0,145,120,textContent="Load",contentType="gauge", maxVal=10))
uiElements.append(UIElement("turbo",350,0,145,120,textContent="Turbo",contentType="gauge", maxVal=10))
uiElements.append(UIElement("voltage",510,0,145,120,textContent="Voltage",contentType="gauge", maxVal=10))
uiElements.append(UIElement("logo",690,0,300,120,imageFile="../ui/images/logo.png",textContent="Info",contentType="graph"))
uiElements.append(UIElement("lane",690,156,145,120,imageFile="../ui/images/lane_failed.png",textContent="No Laneassist",contentType="graph"))
uiElements.append(UIElement("distance",845,156,145,120,imageFile="../ui/images/distance_no.png",textContent="No Distance",contentType="graph"))

uiElements.append(UIElement("sign1",690,311,145,120,imageFile="../ui/images/sign_failed.png",textContent="No Sign",contentType="graph"))
uiElements.append(UIElement("sign2",845,311,145,120,imageFile="../ui/images/30.png",textContent="30 kmH",contentType="graph"))

uiElements.append(UIElement("nav",10,156,645,400,imageFile="../ui/images/nav.jpg",textContent="NAV View",contentType="graph"))
#Canvas is 20 px highr
#uiElements.append(UIElement("speed",150,0,120,120,textContent="Speed",contentType="gauge"))

ui = DisplayUI(uiElements)

time.sleep(5)

ui.updateUIElementGraph("lane", "../ui/images/lane_empty.png","AAAH")
#ui.updateUIElementGauge("distance",20)

time.sleep(5)