from gpiozero import Servo
from time import sleep


def pakan(lama):
    servo = Servo(15)
    servo.mid()
    sleep(1)

    servo.max()
    sleep(lama)

    servo.mid()
    sleep(1)
    servo.value = None;

pakan(0.2)