import time
import requests
import ultrasonic
from servo import pakan
import getdata_ubi as ubi
import datetime
#import lcd_x_button

TOKEN = "BBFF-P9kmWskDVbZ7MkqpZeJlJP65gmJ1uU"  # Put your TOKEN here
DEVICE_LABEL = "aquathings"  # Put your device label here 
VARIABLE_LABEL_1 = "jarak"  # Put your first variable label here
VARIABLE_LABEL_2 = "input_button"
VARIABLE_LABEL_3 = "jam1"
VARIABLE_LABEL_4 = "menit1"



def build_payload(variable_1, variable_2,
                  variable_3,variable_4):
    
    value_1 = int(ultrasonic.distance())
    value_2 = [0,1,2,3,4,5]
    value_3 = ubi.jam1
    value_4 = ubi.menit1
    

    # Creates a random gps coordinates
    payload = {variable_1: value_1,
               variable_2: value_2,
               variable_3: value_3,
               variable_4: value_4,
               }

    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
           your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

def get_request(buka,varjam,varmenit):
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}/{}/lv".format(url, DEVICE_LABEL, varjam)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.get(url=url, headers=headers)
        status = req.status_code
        attempts += 1
        if status != 200:
            time.sleep(1)
            
    #jam_1 = int(float(req.text))
            
    jam_1 = int(float(ubi.jam1))
        
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}/{}/lv".format(url, DEVICE_LABEL, varmenit)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.get(url=url, headers=headers)
        status = req.status_code
        attempts += 1
        if status != 200:
            time.sleep(1)
            
    #menit_1=int(float(req.text))
    menit_1 = int(float(ubi.menit1))
    
    
#     jamsekarang1 = int(time.strftime("%H"))
#     menitsekarang1= int(time.strftime("%M"))
    sekarang = datetime.datetime.now()
     
    jamsekarang1 = sekarang.hour
    menitsekarang1 = sekarang.minute
    


    if jamsekarang1 == jam_1 and menitsekarang1 == menit_1:
        if buka < 1:
            pakan(0.3)
            print("Buka Pakan")
        buka+=1
    else:
        buka=0
    return buka



def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2,
        VARIABLE_LABEL_3,VARIABLE_LABEL_4)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print ("Jarak Sensor-Air = ",int(ultrasonic.distance()),"cm")
#    print (f"jam1 = {ubi.jam1}, menit1 = {ubi.menit1}")
    print("[INFO] finished")


if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
