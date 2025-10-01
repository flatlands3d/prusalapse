import os
import serial.tools.list_ports

def validateInput(min, max, message):
    while (True):
        userInput = input(message)
        try:
            userInput = int(userInput)
            if userInput < min or userInput > max:
                print("Error: Invalid input")
            elif userInput == 'e' or userInput == 'E':
                exit()
            else:
                break
        except:
            print("Error: Invalid input")
    return userInput

def discoverUSB():
    print("-----------------------------------------")
    print("Avaliable Ports")
    count = 1
    portsArr = []
    ports = serial.tools.list_ports.comports()
    for port in ports:
        portsArr.append(str(port))
        print(count, "-", str(port))
        count += 1
    return portsArr

def createTimelapse(directory):
    images = [img for img in os.listdir(directory) if img.endswith(".png")]
    images.sort()