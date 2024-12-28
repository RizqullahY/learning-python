# fungsi sederahana menggunakan argument

def siswa(nama): 
    print('Siswa ini bernama : ',nama)

siswa('agus')
print()

# fungsi menggunakan keyword argument

def guru(nama,pelajaran):

    print(f'Guru ini bernama {nama} dan dia mengajar {pelajaran}')

guru(nama='Bayu',pelajaran='Otomotif')
guru(pelajaran='Bela Diri',nama='Roni')     # meskipun keywords argument tidak sama 
                                            # dengan yang ada di fungsi dia akan tetap urut 
                                            # seperti yang di fungsi
guru('Ipa','Ihan')      # ini adalah contoh yang salah
print()

# fungsi menggunakan default argument
# guna memberikan data apa bila  argument pada pemanggilan tidak ada isinya

def penjaga(nama='misterius',umur='tidak diketahui',shift='sewaktu-waktu'):
    print(f'Penjaga ini Namanya {nama} umurnya {umur} shiftnya {shift}')

penjaga()          

'''Tidak akan muncul error apabila mengosongkan () disaat argument pada fungsi
berisi karena telah ditambahkan (semacam) alternatif yaitu default argument '''


penjaga(nama='Pak Agus',umur=50,shift='setiap hari')

# bisa saja jika ingin memasukkan datanya kedalam argument
# asal jangan lupa ','-"PENGGUNAAN KOMA"
# apa bila suatu argument di fungsi tidak ada isi maka sewaktu pemanggilan 
# perlu di isi 
