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
                # Reading UI Elements from Config
                for uiElement in uiElements:
                    self.uiElements.append(UiElement(uiElement[0], uiElement[1], uiElement[2], uiElement[3]))
                #getting system config
                self.audio = system["audio"]
            except yaml.YAMLError as exc:
                print(exc)

    def __init__(self):
        self.version = "1.0"
        self.uiElements=[]
        self.audio = "false"


        self.loadConfig()

