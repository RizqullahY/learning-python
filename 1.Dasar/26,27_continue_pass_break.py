angka = 0
while angka < 10 :
    angka += 1 
    if angka ==  3:
        print('Nyantol') # saat dia angka 3 dia akan memberikan aksi 
                         # lalu dilanjut dengan angka tiga lagi

    elif angka > 6:
        print('Besar')
        continue # membuat sebuah loop meloncat ke step selanjutnya
                 # men skip aksi yang ada di bawahnya
    print(angka)