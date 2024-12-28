Barang = ['Hp','Guling','Bantal','Selimut',]
print(Barang)


# beberapa method untuk memanipulasi list
# method untuk menambah data ke list

Barang.append('Skincare')       # menambahkan data dalam list
print(Barang)

Barang.extend('Bom')            # menambahkan data per-karakter
print(Barang)

Barang.insert(1,'Gelas')    # menambahkan data beserta posisinya (posisi,data)
print(Barang)


# method untuk menghitung anggota nya

JumlahHP = Barang.count('Hp')       # menghitung jumlah (Hp) dalam list
print('Jumlah Hp di dalam list adalah :',JumlahHP)

# method untuk meremove data dalam list

Barang.remove('Skincare')
print(Barang)

Barang.reverse()            # membalik urutan data
print(Barang)

Bondo = Barang.copy()       # menyalin semua data dari Barang
Bondo.append('Kaca')        # menambahkan data pada list Bondo,tapi tidak menambah data ke list Barang
print(Bondo)








