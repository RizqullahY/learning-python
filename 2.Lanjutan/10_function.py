# mendefinisikan fungsi
def fungsi():
    print('Ini adalah sebuah fungsi') # isi dari fungsi
    # memanggil fungsi
fungsi()



# fungsi sederhana
def warnabaju():        # membuat fungsi 
    print('Merah')

def hargabaju():        # membuat fungsi lagi
    warnabaju()         # memanggil fungsi didalam fungsi
    print('Harga Baju : 35000')

warnabaju()     # ketika memanggil fungsi yang diawal maka hanya keluar isi fungsi yang awal saja
hargabaju()     # ketika memanggil fungsi yang didalamnya terdapat fungsi
                # yang diawal maka akan memanggil keduanya
 


 # function dan argument
def total_harga_baju(jumlah):       # jumlah adalah sebuah parameter yang berfungsi 
                                               # membuat fungsi menjadi lebih spesifik 
    harga =  35000
    hargaTotal = jumlah * harga
    print('Harga ',jumlah,' Baju adalah',hargaTotal)

total_harga_baju()   


''' parimeter dalam () perlu di isi apabila pada 'def' diberikan parameter 
bila dalam pemanggilan fungsi terdapat parimeter yang tidak diisi
maka akan muncul error '''  