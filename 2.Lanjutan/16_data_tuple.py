import sys
import timeit

Ganjil = [1,3,5,7,9]        # list data menggunakan []
Genap = (2,4,4,4,4,6,8,10)        # tuple data menggunakan () 

'''Tuple adalah tipe data yang tidak bisa diubah datanya'''
# misal

Ganjil[1] = 97      # merubah data list urutan ke 1(2) menjadi 97
Ganjil.append(2)    # menambah data 
print(Ganjil)       #   BISA___

# Genap[1] = 97      # merubah data tuple urutan ke 1(2) menjadi 97
# Genap.append(2)    # menambah data dibelakang
# print(Genap)       #    ERROR___TIDAK_BISA
print()

# dir digunakan untuk melihat apa saja yang dapat digunakan pada sebuah data 
# print(dir(Ganjil))      # yang terdapat dalam terminal ialah yang bisa digunkan data tersebut
# print()
# print(dir(Genap))       # count dan index yang bisa digunkan tuple

print(Genap.count(4))       # menghitung data
print(Genap.index(8))       # mencari posisi data
print()


'''Mengetes data tuple dan list // import sys'''

data_list = [1,2,3,4,5,'Jam','Helm',False,3,14]
data_tuple = (1,2,3,4,5,'Jam','Helm',False,3,14)

print(data_list)
print(data_tuple)


#   == besar data ==

besar_datalist = sys.getsizeof(data_list)
besar_datatuple = sys.getsizeof(data_tuple)

print()

print(besar_datalist)
print(besar_datatuple)          # data tuple lebih kecil dibanding list meski isinya sama

'''Data pada tuple lebih kecil memakan memory
kerana tidak banyak fungsi yang dapat kita pakai 
didalam tuple'''


'''Waktu untuk memproses data // import timeit'''

data_list = timeit.timeit(stmt='[1,2,3,4,5,6,7,8,9]',number=100000)
data_tuple = timeit.timeit(stmt='(1,2,3,4,5,6,7,8,9)',number=100000)

print(data_list)
print(data_tuple)               # memproses data tuple lebih cepat dibanding list




















