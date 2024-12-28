# Pembuat Password Acak

# import random
# import string

# huruf = string.ascii_letters
# nomor = '0123456789'
# simbol = '-+*%&$!'
# kombinasi =  huruf + nomor + simbol

# len = int(input('Masukkan Jumlah Karakter Password : '))

# password = ''.join(random.sample(kombinasi, len))
# ''' Fungsi join adalah untuk memasukkan data ke dalam ('')'''

# print(password)


# Kumpulan Karakter Acak

import random

nama = 'rafly rizqullah yusuf'
len = int(input('masukkan jumlah karakternya :'))

jadinya =''.join(random.sample(nama,len))
print(jadinya)