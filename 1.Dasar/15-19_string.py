


data = 'ini adalah string dengan single quote'
data = "ini adalah string dengan double quote"

# print("sekarang hari jum'at")       # bisa
# print('sekarang hari jum'at')       # tidak bisa akan error


print('sekarang hari jum\'at')

''' Tanda \ digunakan ketika
pada suatu penulisan string terdapat cara pemanggilan yang
ambigu  '''

# print("C:\user\Hasr")         # error

''' Error karena
tanda (\) yang seharusnya digunakan untuk
membantu sebuah karakter fungsi menjadi string
justru dijadikan string '''


# cara menanggulanginya ialah menambahkan (\) lagi pada (\)

contoh = 'C:\\user\\data'
print(contoh)

# tab 
print('Sini \t Sana ')     # menambahkan tab pada string tanpa harus mengetiknya langsung

# backspace
print('Firman \b Syah')

# new line 
print('baris pertama.\n baris kedua.')
print('baris pertama.\r baris kedua.')
print('baris pertama.\r\n baris kedua.')

#string literal dan raw

print('C:\new folder')

#raw
print(r'C:\new folder')

#multiline literal
print('''
nama = ucup
umur = 35 tahun
''')














