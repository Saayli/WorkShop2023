# Python code for connecting Arduino to Python
# That's Engineering
# 29/04/2020

import serial
import time
import requests


while True:
    arduino = serial.Serial('com3', 9600)
    arduino_data = arduino.readline()

    # print(arduino_data)

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    values = eval(decoded_values)

    requests.post(url = "http://127.0.0.1:5000/set-water", data = {"temp": values[0]})
    requests.post(url = "http://127.0.0.1:5000/set-air", data = {"temp": values[1]})

    print(values)

    list_values = decoded_values.split('x')

    arduino_data = 0
    list_values.clear()
    arduino.close()
    time.sleep(60)