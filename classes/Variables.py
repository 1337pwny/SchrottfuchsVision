from classes.UiElement import UiElement
import yaml
class Variables:
    # This returns the ui element by name. Since we only want one element we only use the first element. Kinda Hacky but works
    def getUiElementByName(self, name):
        return list(filter(lambda element: element.elementName == name, self.uiElements))[0]

    def loadConfig(self):
        with open("config.yaml", "r") as stream:
            try:
                config = yaml.safe_load(stream)
                uiElements = config['uiElements']
                system =  config['System']
                camera = config['Camera']
                # Reading UI Elements from Config
                for uiElement in uiElements:
                    self.uiElements.append(UiElement(uiElement[0], uiElement[1], uiElement[2], uiElement[3]))
                #getting system config
                self.audio = system["audio"]
                self.useSingleCam = system["useSingleCam"]
                self.filebaseMode = system["filebaseMode"]
                self.videoFileSigleCam = system["videoFileSigleCam"]
                self.singleCam = camera["camSingle"]
                self.laneCamCropXStart = camera["laneCamCropXStart"]
                self.laneCamCropYStart = camera["laneCamCropYStart"]
                self.laneCamCropXStop = camera["laneCamCropXStop"]
                self.laneCamCropYStop = camera["laneCamCropYStop"]
                self.signCamCropXStart = camera["signCamCropXStart"]
                self.signCamCropYStart = camera["signCamCropYStart"]
                self.signCamCropXStop = camera["signCamCropXStop"]
                self.signCamCropYStop = camera["signCamCropYStop"]

            except yaml.YAMLError as exc:
                print(exc)

    def __init__(self):
        self.version = "1.0"
        self.uiElements=[]
        self.audio = "false"
        self.useSingleCam = "true"
        self.filebaseMode = "true"
        self.videoFileSigleCam = "None"
        self.singleCam = "None"
        self.laneCamCropXStart = "None"
        self.laneCamCropYStart = "None"
        self.laneCamCropXStop = "None"
        self.laneCamCropYStop = "None"
        self.signCamCropXStart = "None"
        self.signCamCropYStart = "None"
        self.signCamCropXStop = "None"
        self.signCamCropYStop = "None"


        self.loadConfig()

