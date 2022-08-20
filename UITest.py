from classes.ui import UIClass
import time
from classes.Variables import Variables

vars=Variables()
ui = UIClass(160, 160, vars)

while(1):
    time.sleep(2)
    ui.updateLaneState("lane_ok")
    time.sleep(2)
    ui.updateLaneState("lane_rightFail")
    time.sleep(2)
    ui.updateSignState("sign_50")
    time.sleep(2)
    ui.updateSignState("sign_30")
    time.sleep(2)
    ui.updateAdditionalSignState("sign_failed")
    time.sleep(2)
    ui.updateAdditionalSignState("sign_noOvertaking")
    time.sleep(2)
    ui.updateDistanceState("distance_no")
    time.sleep(2)
    ui.updateDistanceState("distance_ok")
    time.sleep(2)
    ui.updateDistanceState("distance_toClose")