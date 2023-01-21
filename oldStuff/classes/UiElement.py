class UiElement:
    def __init__(self, elementName, elementImage, elementText, elementSound):
        self.elementImage = elementImage
        self.elementText = elementText
        self.elementSound = elementSound
        self.elementName = elementName

    def __str__(self):
        return "Name: "+self.elementName+" Text: "+self.elementText+" Image: "+self.elementImage+" Sound: "+self.elementSound
