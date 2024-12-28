from collections import deque
# stack = seperti tumpukan buku yang diambil atasnya
# queue = seperti antrian , yang dilayani pertama terlebih 

tumpukan = [1,2,3,4,5,6]
tumpukan.append(7)          # menambahkan data '7'
print(tumpukan)

tumpukan.pop()
''' menghilangkan data yang berada di belakang , () juga dapat membantu untuk 
menentukan posisi misal () menghilangkan data paling belakang,(0): data pertama dari depan
(1): data kedua dari depan ,(-1): data kedua dari belakang '''

print(tumpukan)
print()



# antrian_
antrian = deque([1,2,3,4,5])
print(antrian)

# data masuk
antrian.append(6)
print('Data Masuk',6)
print('Data Sekarang',antrian)

# data keluar
out = antrian.popleft()         # sama seperti .pop bedanya == .popleft dari kiri ke kanan
                                # sedangkan .pop dari kanan ke kiri
print('Data Keluar', out)
print('Data Sekarang',antrian)

out = antrian.popleft()         # akan melanjutkan fungsi sebelumnya

print('Data Keluar', out)
print('Data Sekarang',antrian)









