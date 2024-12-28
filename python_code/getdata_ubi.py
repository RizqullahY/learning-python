import requests
import random
import time

TOKEN = "BBFF-P9kmWskDVbZ7MkqpZeJlJP65gmJ1uU" # Assign your Ubidots Token
DEVICE = "aquathings" # Assign the device label to obtain the variable
VARIABLE_1 = "jam1"
VARIABLE_2 = "menit1" # Assign the variable label to obtain the variable value
#DELAY = 1  # Delay in seconds

def get_jam(device,variable):
    try:
        url = "http://industrial.api.ubidots.com/"
        url = url + \
            "api/v1.6/devices/{0}/{1}/".format(device,variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        return req.json()['last_value']['value']
    except:
        pass
    
def get_menit(device,variable):
    try:
        url = "http://industrial.api.ubidots.com/"
        url = url + \
            "api/v1.6/devices/{0}/{1}/".format(device,variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        req = requests.get(url=url, headers=headers)
        return req.json()['last_value']['value']
    except:
        pass
    
jam1 = get_jam(DEVICE,VARIABLE_1)  
menit1 = get_menit(DEVICE,VARIABLE_2)


if __name__ == "__main__":
    while True: 
        print("jam1 =", jam1)
        print("menit1 =", menit1)
        #time.sleep(DELAY)