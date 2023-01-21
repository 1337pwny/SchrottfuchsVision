from modules.configLoader.configLoader import ConfigLoader
import os

config = ConfigLoader()
workingDir = os.getcwd()

for module in config.modules:
    for root, dirs, files in os.walk(workingDir+"/modules"):
        for file in files:
            if  module in file:
                filepath = os.path.join(root, file)
                print("starting: "+os.path.join(root, file))
                os.system("python3 "+filepath)