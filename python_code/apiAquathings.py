#http://aquaapi.smkmutumalang.sch.id/aquadata/daftar
import requests
import time

def build_payload('token'):
       
    payload = {'token' : 1234}
    
    return payload

def post_request(payload):
    url = "http://aquaapi.smkmutumalang.sch.id/aquadata/daftar"
    headers = {"Content-Type": "application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, json=payload)
        status = req.status_code
        attempts += 1
        if status != 200:
            time.sleep(1)
    
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
           your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True
            
def main():
    #payload = build_payload("token")
    post_request({'token': 12345})

if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)