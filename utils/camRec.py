import cv2
import time
secondsSinceEpoch = time.time()
print(str(secondsSinceEpoch)+'cam1.avi')
cam = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(2)
frame_width = int(cam.get(3))
frame_width2 = int(cam2.get(3))
frame_height = int(cam.get(4))
frame_height2 = int(cam2.get(4))
cam.set(14,-8.1)
cam.set(10,-8.1)
cam.set(15,-8.1)
out1 = cv2.VideoWriter(str(secondsSinceEpoch)+'cam1.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
out2 = cv2.VideoWriter(str(secondsSinceEpoch)+'cam2.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width2, frame_height2))
while True:
    check, frame = cam.read()
    check2, frame2 = cam2.read()
    cv2.imshow('cam1', frame)
    cv2.imshow('cam2', frame2)
    out1.write(frame)
    out2.write(frame2)

    key=cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cam2.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
