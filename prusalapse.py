# PrusaLapse v0.1
# Flatlands3D - Ethan Doerksen
# 10/01/25

import cv2
import serial
from filemanagement import validateInput, discoverUSB

print("PrusaLapse v0.1")
print("Created by Flatlands3D")

imageCount = 1

serialInst = serial.Serial()

portsArr = discoverUSB()
portNum = validateInput(1, len(portsArr), "Enter your printer's port: ")
baud = validateInput(9600, 115200, "Enter your printer's baudrate: ")
timeout = validateInput(1, 30, "Enter your timeout period in seconds: ")

# port = str(portsArr[portNum - 1]).split(" ", 1)
# port = port[0]
# print("Connecting to printer on", port)
# serialInst.port = port
# serialInst.baudrate = baud
# serialInst.timeout = timeout
# serialInst.open()

# print("-----------------------------------------")
# print("Waiting for data...")

# try:
#     while(True):
#         data = str(serialInst.readline().decode("utf-8"))
#         print(data)
# except:
#     print("Error: Lost connection or no data recieved within", timeout, "seconds")
#     serialInst.close()
#     exit()

cam = cv2.VideoCapture(0)

ret, frame = cam.read()

if ret:
    imageName = str(imageCount) + ".png"
    cv2.imwrite(imageName, frame)
else:
    print("Error: Failed to capture image")

cam.release()