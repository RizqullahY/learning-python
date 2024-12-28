import RPi.GPIO as GPIO
import time

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Inisialisasi daftar dengan 5 elemen nol
input_list = [0, 0, 0, 0, 0]

def readLine(line):
    GPIO.output(line, GPIO.HIGH)
    inputs = [GPIO.input(C1), GPIO.input(C2), GPIO.input(C3), GPIO.input(C4)]
    GPIO.output(line, GPIO.LOW)
    return inputs

try:
    while True:
        inputs = readLine(L1)
        for input_value in inputs:
            input_list.append(input_value)
            input_list.pop(0)  # Menghapus elemen pertama (indeks 0)
        print(input_list)
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nApplication stopped!")
