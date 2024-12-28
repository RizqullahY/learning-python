import RPi.GPIO as GPIO
import time
import LCD1602

BUTTON_PIN_1 = 16
BUTTON_PIN_2 = 20
BUTTON_PIN_3 = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LCD1602.init(0x27, 1)

number = 0
my_list = [0, 0, 0, 0, 0]  # Renamed 'list' to 'my_list' to avoid conflicts with the built-in 'list' type.


try:
    while True:
        time.sleep(0.2)
        button_1_state = GPIO.input(BUTTON_PIN_1)
        button_2_state = GPIO.input(BUTTON_PIN_2)
        button_3_state = GPIO.input(BUTTON_PIN_3)
        # tombol 1
        if button_1_state == GPIO.LOW:
            number += 1
            if number > 9:
                number = 0
            LCD1602.clear()
            LCD1602.write(0, 0, f" Pilih_Angka :{number}")
            LCD1602.write(0, 1, f" {my_list}")
            print("tombol 1 masukkan angka yang tepat :", number, "listnya", my_list)

            # tombol 2
        if button_2_state == GPIO.LOW:
            my_list.pop(0)
            my_list.insert(4, number)
            print("tombol 2", my_list)
            number = 0
            LCD1602.clear()
            LCD1602.write(0, 0, f"Angka_DiMasukkan")
            LCD1602.write(0, 1, f"{my_list}")

            # tombol 3
        if button_3_state == GPIO.LOW:
            print("sudah", my_list)
            LCD1602.write(0, 0, f" Angka_Dimputkan")
            LCD1602.write(0, 1, f"{my_list}")
            LCD1602.clear()
        
            toInt = [int(item) for item in my_list]
            print(toInt)
            



except KeyboardInterrupt:
    GPIO.cleanup()

print("Final list:",toInt)
time.sleep(2)

