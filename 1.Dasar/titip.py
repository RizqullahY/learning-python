# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return(fibo(n-1)+fibo(n-2))

# jumlah_angka = 10

# if jumlah_angka <= 0:
#     print('please enter a positive number')
# else:
#     print('Fibonacci Sequence')
#     for i in range(jumlah_angka):
#         print(fibo(i))




# from tkinter import Button
# import pyautogui

# while True:
#     a = pyautogui.confirm('Apa kamu orang gila ?',Button['yes','no'])
#     if a == 'yes': break


# Game = 1

# while Game <=10:
#     AskFirst = int(input('MAU MAIN ?  1 = IYA 2 = TIDAK'))
#     jwb = 0 
#     if AskFirst == 1:
#         print('oke')
#     elif AskFirst == 2:
#         print('dak jadi ya')
#     else:
#         print('salah nomor')


# Game = Game + 1   


AskFirst = int(input('MAU MAIN ?  1 = IYA 2 = TIDAK : '))
print(AskFirst)
if AskFirst == 1 :
    print('oke')
elif AskFirst == 2 : 
    break
else :
    print('salah nomor')
