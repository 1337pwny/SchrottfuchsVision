import serial
from time import sleep
from modules.restClient.restClient import RestClient

ser = serial.Serial(
    port='/dev/ttyUSB3',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
def trigger():
   # Trigger 5A 04 04 62
    packet = bytearray()
    packet.append(0x5A)
    packet.append(0x04)
    packet.append(0x04)
    packet.append(0x62)

    ser.write(packet)
def initializeTFMini():
    # Code for pixhawk 5A 05 05 02 66
    # setting for plaintext output
    packet = bytearray()
    packet.append(0x5A)
    packet.append(0x05)
    packet.append(0x05)
    packet.append(0x02)
    packet.append(0x66)

    ser.write(packet)

    # Framerate 0: 5A 06 03 LL HH
    # Setting framrate to zero to only get data wenn triggered
    packet = bytearray()
    packet.append(0x5A)
    packet.append(0x06)
    packet.append(0x03)
    packet.append(0x00)
    packet.append(0x00)
    packet.append(0x63)

    ser.write(packet)
    trigger()
    buff = ser.readall()
count = 0
initializeTFMini()
print("garbage done")
restClient = RestClient()
while True:
    trigger()
    buff = ser.readall()
    sleep(0.5)
    # discarding first 3 dataframes
    if count > 3:
        meters = chr(buff[0])+chr(buff[1])+chr(buff[2])+chr(buff[3])
        restClient.setDistance(meters)
        print(meters+"m")
    else:
        count = count + 1

ser.close()