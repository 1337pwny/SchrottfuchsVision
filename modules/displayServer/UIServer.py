from modules.displayServer.displayUI import DisplayUI
from modules.displayServer.displayUI import UIElement
from http.server import HTTPServer, BaseHTTPRequestHandler
from modules.configLoader.configLoader import ConfigLoader
import playsound

class GlobalVars:
    def __init__(self):
        self.distance = 0
        self.speed = 0
################ Internal states
globalVars = GlobalVars()
############# Initialize UI #########################################

uiElements=[]
uiElements.append(UIElement("speed",10,0,145,120,textContent="Speed",contentType="gauge", maxVal=10))
uiElements.append(UIElement("load",170,0,145,120,textContent="Load",contentType="gauge", maxVal=10))
uiElements.append(UIElement("turbo",350,0,145,120,textContent="Turbo",contentType="gauge", maxVal=10))
uiElements.append(UIElement("voltage",510,0,145,120,textContent="Voltage",contentType="gauge", maxVal=10))
uiElements.append(UIElement("logo",690,0,300,120,imageFile="ui/images/logo.png",textContent="Info",contentType="graph"))
uiElements.append(UIElement("lane",690,156,145,120,imageFile="ui/images/lane_failed.png",textContent="No Laneassist",contentType="graph"))
uiElements.append(UIElement("distance",845,156,145,120,imageFile="ui/images/distance_no.png",textContent="No Distance",contentType="graph"))

uiElements.append(UIElement("sign1",690,311,145,120,imageFile="ui/images/sign_failed.png",textContent="No Sign",contentType="graph"))
uiElements.append(UIElement("sign2",845,311,145,120,imageFile="ui/images/30.png",textContent="30 kmH",contentType="graph"))

uiElements.append(UIElement("nav",10,156,645,400,imageFile="ui/images/nav.jpg",textContent="NAV View",contentType="graph"))


ui = DisplayUI(uiElements)
config = ConfigLoader()
########## UI Funcztions #############################################
def playAudio(self, filename):
    if self.variables.audio == "true" and filename != "None":
        print("playing Sound")
        playsound.playsound(filename)

################## UI Business Logic ###################################
def handleDistanceChange(value):
    globalVars.distance = float(value)
    if globalVars.speed > config.distanceSlowThreshold:
        threshold = config.distanceThresholdFast

    else:
        threshold = config.distanceTresholdSlow
    print(threshold)
    if globalVars.distance > threshold:
        ui.updateUIElementGraph("distance", "ui/images/distance_ok.png", value+"M")
    else:
        ui.updateUIElementGraph("distance", "ui/images/distance_to_close.png", value + "M")


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "graph" in self.path:
            params=self.path.split('?')[1]
            name=params.split(',')[0].split('=')[1]
            value = params.split(',')[1].split('=')[1]
            if name == "distance":
                handleDistanceChange(value)

        self.send_response(200)

httpd = HTTPServer(('localhost', 5000), MyHandler)
httpd.serve_forever()

#time.sleep(5)

#ui.updateUIElementGraph("lane", "../ui/images/lane_empty.png","AAAH")
#ui.updateUIElementGauge("distance",20)

#time.sleep(5)