# fungsi dengan return value  

def kuadrat(argumen=0):     # apabila saat pemanggilan argument tidak diisi
    hasil = argumen**2
    print('Nilai kuadrat dari',argumen,'adalah',hasil)

kuadrat(3)      # pemanggilan fungsi biasa

a = kuadrat(3)      # memasukkan 'kuadrat()' kedalam a
print(a)            # saat pemanggilan a  yg terjadi adalah none
print()


# cara mengatasinya ialah menggunakan return di nilai akhir dari program tersebut

def kuadrat(argumen=0):     
    hasil = argumen**2
    print('Nilai kuadrat dari',argumen,'adalah',hasil)
    return hasil

kuadrat(2)      # pemanggilan 1

a = kuadrat(3)  # pemanggilan 2
print(a)        # pemanggilan 3
print(kuadrat(4))   # pemanggilan 4 dan 5


# fungsi dengan return value dan multi argument

def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total

a = tambah(4,5)     # mengikuti urutan argumen fungsi // a hanya mengambil hasil / nilai akhir
kali(2,a)           # bisa memasukkan a tersebut yang berupa nilai akhir ke pemanggilan  sebuah fungsi lain




