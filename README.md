# ReconSign
## UwU Whats Dis?
Some time ago I decided, that it would be great if my old car could detect streetsigns. So I tried to cobble a thing together, that somehow works.
I use OpenCV for image recognition and rely on pattern matching for the first try. Maybe I will be switching to neural networks in the future (Big maybe atm.)
I talked about this in a presentation at Kassel IT-Sec Meetup a while ago, you can find the slides here (TODO: Add link).
Recently I got some time to sort things out an hope that I can focus on this Project more.

## Current status
After just some ours of beer, cigarettes and music I rewrote a whole lot of stuff and its now object oriented.
The old script can be found in the reconSign_old.py
Now its time to add multithreading to the shit. And the it will hopefully run fast anough to use a pi4 as computer.

## What you need 
you need to install python3, numpy, imlib and opencv
pip3 install numpy imlib opencv-python

## Hardware
Currently an old Hitachi BW CCD Highspeed shutter camera, which is typically used in sorting maschines and industrial applications, for the camera part. Since i only got an analog signal, I use a cheap capture card to gather the footage.
