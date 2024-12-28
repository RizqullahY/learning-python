# scope variable local

namaAyam = 'Jager'

def rubahNamaAyam(namaBaru):
    namaAyam = namaBaru
    print('Saya rubah nama ayam menjadi',namaAyam)

rubahNamaAyam('Kutuk')
print('Nama ayam yang dulu :',namaAyam)

# scope variable global
print()

namaAyam = 'Jager'
makananAyam = 'Jagung'

def rubahNamaAyam(namaBaru):
    global namaAyam
    namaAyam = namaBaru         # global
    nama = namaBaru             # local
    print('Saya rubah nama ayam menjadi',namaAyam)

def kasihMakanAyam(makanan,nama):
    global namaAyam,makananAyam
    namaAyam = nama
    makananAyam = makanan

rubahNamaAyam('Sartle')
kasihMakanAyam('Beras','Roi')
print('Nama ayam yang dulu :',namaAyam,'dan makan ',makananAyam)
