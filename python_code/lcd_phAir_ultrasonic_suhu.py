import RPi.GPIO as GPIO
import time
import board
import busio
import sys
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import os
import glob
import LCD1602
# Ultrasonic Sensor Configuration
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# ADS1115 pH Sensor Configuration
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)

LCD1602.init(0x27, 1)
# Temperature Sensor Configuration
def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def readSuhu(ds18b20):
    temperature = 0.0
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    if(len(text) >  0):
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    fahrenheit = (celsius * 1.8) + 32
    return celsius

def read_voltage(channel):
    buf = []
    for i in range(10):  # Take 10 samples
        buf.append(channel.voltage)
    buf.sort()  # Sort samples and discard highest and lowest
    buf = buf[2:-2]
    avg = (sum(map(float, buf)) / 6)  # Get average value from remaining 6
    ph = avg * 3.5
    return avg, ph
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance

def main():
    try:
        ds18b20 = sensor()
        channel = AnalogIn(ads, ADS.P0)
        
        while True:
            dist = distance()
            avg_voltage, ph_value = read_voltage(channel)
            temperature = readSuhu(ds18b20)
            
            print(f"Ultrasonic Distance: {dist:.1f} cm")
            LCD1602.clear()
            LCD1602.write(0, 0, "Ketinggian Air")
            LCD1602.write(0, 1, f"{dist:.2f}cm")
            time.sleep(3)
            print(f"pH Value: {ph_value:.2f}")
            LCD1602.clear()
            LCD1602.write(0, 0, "PH Air")
            LCD1602.write(0, 1, f"{ph_value:.1f}")
            time.sleep(3)
            print(f"Temperature: {temperature:.2f}°C\n")
            LCD1602.clear()
            LCD1602.write(0, 0, "Suhu Air")
            LCD1602.write(0, 1, f"{temperature:.1f}C")
            time.sleep(3)
            
            
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

if __name__ == '__main__':
    main()
