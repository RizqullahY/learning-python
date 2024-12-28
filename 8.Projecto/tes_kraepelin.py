import random

try:
   while True:
      angka1 = random.randint(1,9)
      angka2 = random.randint(1,9)
      jumlah = angka1 + angka2
      print(f"{angka1} dan {angka2} :___")
      if jumlah >= 10:
         if (jumlah - 10) == int(input()) :
            print("Siip")
         else:
            print("Salah")
      elif int(input()) == jumlah:
            print("Oke")
      else:
            print("Try Again")

except ValueError:
   pass
