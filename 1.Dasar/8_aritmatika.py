
#'' untuk simbol
#"" untuk huruf dan angka

# operasi aritmatika

a = 10
b = 5
c = 3

# pertambahan (+)
hasil = a+b
print (a,'+',b,'=',hasil)


# pengurangan (-)
hasil = a-b
print (a,'-',b,'=',hasil)


# perkalian (*) 
hasil = a*b
print (a,'*',b,'=',hasil)


# pembagian (/)  
hasil = a/b
print(a,'/',b,'=',hasil) #bisa habis (tidak bersisa)

hasil = a/c
print(a,'/',c,'+',hasil) #tdk bisa habis (bersisa)

# perpangkatan (**)
hasil =  a**b 
print(a,'**',b,'=',hasil)



# modulus  (%) = "sisa dari sebuah pembagian yang tidak habis,
# bila dalam suatu pembagian bisa habis
# maka modulus tidak akan menampilkan data "

# modulus pembagian yang bisa habis
hasil = a%b
print(a,'%',b,'=',hasil)

# modulus pembagian yang tidak bisa habis (bersisa)

hasil= a%c 
print(a,'%',c,'=',hasil)


# floor division (//) ="membulatkan pembagian yang tdk bisa habis"
hasil= a//c
print(a,'//',c,'=',hasil)

# prioritas operasi , operational precedence
# mendahulukan perhitungan sesuai kedudukannya
#()     **     *,/     +,-

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print ( x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print  (x,'+',y,'*',z,'=',hasil)


# perhitungan dalam tanda kurung akan mengambil langkah awal
# seperti inilah bentuk penulisan nya

hasil = (x + y) * z
print ('(',x,'+',y,')*',z,'=',hasil)


