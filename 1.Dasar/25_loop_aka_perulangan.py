



print("LOOP MENGGUNAKAN LIST")
#Loop menggunakan list 
angka_list = [2,3,4,5,6]
for i in angka_list :
    print(i)


print("LOOP MENGGUNAKAN RANGE")
#Loop menggunakana Range
#penulisan range : (x,y,z)
# X = angka pertama dari sebuah loop
# Y = angka terakhir - 1 (y-1) / apa bila menulis sebuah y 
# maka loop akan berhenti di satu angka sebelumnya 
# contoh :(1,4) maka akan jadi : 1,2,3

# Z = beda


angka_range = range(1,4)

for i in angka_range :
    print(i)


print('LOOP MENGGUNAKAN WHILE')
# While loop 
Pertama = 0     # buat data
while Pertama < 5 :     # jika data (pertama) masih dibawah 5
    Pertama += 1        # setiap loop ditambah satu
    print (f'Sekarang angka :{Pertama}')