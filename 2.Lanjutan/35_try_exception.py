# menghandling error 
while True:
    try:
        penyebut = int(input('Masukkan angka penyebut\n'))
        pembilang = int(input('Masukkan angka pembilang\n'))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print('anda tidak memasukkan angka')
    except ZeroDivisionError:
        print('anda memasukkan angka nol,pilih yang lain yaa')
print('berhasil! hasilnya adalah',hasil)
