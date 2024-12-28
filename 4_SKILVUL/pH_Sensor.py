# import os
# import serial
# import time
# from firebase import firebase

# arduino = serial.Serial('/dev/ttyACM0',9600)

# firebase = firebase.FirebaseApplication('https://raspi-ph.firebaseio.com/', None)


# def update_firebase():
#     phair = arduino.readline()
#     if data is not None:
#         time.sleep(1)
#         pieces = data.split("sensor= ")
#         ph = pieces
#         print (ph)
#     else:
#         print('Failed to get data. Try Again!')
#         time.sleep(10)

#     data = {"Sensor pH": phair}
#     firebase.post('/sensor/ph', data)


# while True:
#     update_firebase()

#     time.sleep(5) # menunda waktu eksekusi dalam menampilkan data (detik)
#     membaca baris yang tidak tebaca/terdefinisikan oleh port serial
# import RPi.GPIO as GPIO

import os
import serial
import time
import requests


raspberry = serial.Serial('/dev/ttyACM0',9600)

def update_data():
    ph_air = raspberry.readline()
    if data != None:
        time.sleep(1)
        ph = data.split("sensor= ")
        print (ph)
    else:
        print('Terjadi kesalahan, coba lagi')
        time.sleep(10)

    data = {"Sensor pH": ph_air}
    raspberry.post('/sensor/ph', data)


while True:
    update_data()

    time.sleep(5)




