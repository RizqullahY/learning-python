# ini adalah operasi aritmatika menggunakan def

def jumlah(a,b):
    c = a+b
    return c

hasil=jumlah(5,6)

print(hasil)

# operasi aritmatika menggunakan lambda
 
kali = lambda x,y : x * y       # membuat fungsi , lambda , argumen1 dan 2, aksinya
x = kali(x=3,y=4)       # memasukkan nilai pada fungsi

print(kali(3,5))        # memanggil fungsi secara langsung
print(x)                # memanggil fungsi dengan wakilnya --wkwkwk


'''Urutan lambda bila terdapat data list:
list( map/filter ( lambda x:x aksinya  ,'nama list')) '''


# lambda
tambah = lambda a,b : a+b
hasil = tambah(a=9,b=8)

print(hasil)



# filter
list_umur = [34,39,20,18,13,54]
print('Umur orang kebanyakan ',list_umur)
hasil_filter = list(filter(lambda a:a >= 19 ,list_umur))    # menyeleksi data  yang sesuai dengan tindakan

print('Umur Orang Dewasa ',hasil_filter)


# map
a = [1,2,3,4,5,6,7]

a_kuadrat = list(map(lambda x: x **2, a))       # ya gitulah pokonya
print(a_kuadrat)

