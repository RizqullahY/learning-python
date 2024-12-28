# lastid = '22-0011'

# tahun = lastid[0:2]


# nomer = lastid[3:7]
# nomer = int(nomer) + 1

# nomer= str(int(lastid[3:7])+1)

# print('Id terakhir : ',lastid)
# print('Tahun 20'+tahun)
# print('No. Pendaftaran:' + lastid[0:5] + str(nomer))


# angka1_ = input('Masukkan angka pertama: ')
# angka2_ = input('Masukkan angka kedua: ')
# operasi = input('Masukkan operasi yang anda ingin kan:')

# if operasi == 'Pertambahan':
#     hasil = int(angka1_) + int(angka2_)
#     print(hasil)

# if operasi == 'Pengurangan':
#     hasil = int(angka1_) - int(angka2_)
#     print(hasil)

# if operasi == 'Perkalian':
#     hasil = int(angka1_) * int(int(angka2_))
#     print (hasil)

# if operasi == 'Pembagian':
#     hasil = int(angka1_) / int(angka2_)
#     print(hasil)


# COBA LAGI__

angka1_ = int(input('Masukkan angka pertama: '))
angka2_ = int(input('Masukkan angka kedua: '))
operasi = input('Masukkan operasi yang anda ingin kan:')

if operasi == 'Pertambahan':
    hasil = (angka1_) + (angka2_)
    print('Hasil Dari',angka1_,'Ditambah',angka2_,'=', hasil)

elif operasi == 'Pengurangan':
    hasil = (angka1_) - (angka2_)
    print('Hasil Dari',angka1_,'Dikurangi',angka2_,'=', hasil)

elif operasi == 'Perkalian':
    hasil = (angka1_) * (angka2_)
    print('Hasil Dari',angka1_,'Dikali',angka2_,'=', hasil)

elif operasi == 'Pembagian':
    hasil = (angka1_) / (angka2_)
    print('Hasil Dari',angka1_,'Dibagi',angka2_,'=' ,hasil)
else:
    print('Ada yang salah')


buah =['mengkudu','mangga','pisang','apel','jeruk','jambu']
angka =[12,34,56,78,90,19]

# def cek_apel(x):
#     if(x=='apel'):
#         return True
#     else:
#         return False
    
# apel = filter(cek_apel,buah)
# print(list(apel))

# apel = filter(lambda x : x =="apel",buah)
# print(list(apel))



# huruf_m= filter(lambda x : x[-1] =="u",buah)
# print(list(huruf_m))

# menambahkan string Buah
nambahBuah = map(lambda x,y: str(y)+' Buah '+x,buah,angka)
print(list(nambahBuah))