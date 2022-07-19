from classes.ui import UIClass
import time

ui = UIClass(160,160)

while(1):
    time.sleep(2)
    ui.updateLaneState("2")
    time.sleep(2)
    ui.updateLaneState("3")
    time.sleep(2)
    ui.updateSignState("3")
    time.sleep(2)
    ui.updateSignState("2")
    time.sleep(2)
    ui.updateAdditionalSignState("1")
    time.sleep(2)
    ui.updateAdditionalSignState("2")
    time.sleep(2)
    ui.updateDistanceState("1")
    time.sleep(2)
    ui.updateDistanceState("2")
    time.sleep(2)
    ui.updateDistanceState("3")