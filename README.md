# ReconSign
## <img src="https://comm.network/system/custom_emojis/images/000/051/688/original/3c1ac22f90331b1f.png" alt="UwU" height="32" width="32"  /> Whats Dis?
Some time ago I decided, that it would be great if my old car could detect street signs. So I tried to cobble a thing together which now somehow works.
I use OpenCV for image recognition and rely on pattern matching for the first version. Maybe I will be switching to neural networks in the future (Big maybe atm.)

I talked about this in a presentation at Kassel IT-Sec Meetup a while ago, you can find the slides here (TODO: Add link).

Recently I got some time to sort things out and hope that I can focus on this Project more.

## Current status
After just some hours of beer, cigarettes and music I rewrote a whole lot of stuff and the code is now object oriented.
The old script can be found in the `reconSign_old.py` file.
Now its time to add multithreading so it will hopefully run fast anough to use a RaspberryPi 4 as processing unit.

## What you need 
You'll need to install `python3`, `numpy`, `imlib`, `imutils` and `opencv`.

This can be done by running:
```
pip3 install -r requirements.txt
```

## Running
Basically you just need to put your assets (a `.jpg` of a streetsign, a `.jpg` of the shape of the sign and an `.mp4` video of the driving) into the asset folder and configure the paths in `main.py`

You can then simply run the `main.py` file. 
You may also want to change the threshold parameters in `main.py` depending on your assets.

## Hardware
Currently an old Hitachi BW CCD high speed shutter camera, which is typically used in sorting machines and industrial applications, for the camera part. Since I only got an analog signal, I use a cheap capture card to gather the footage.
