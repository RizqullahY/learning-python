# set,himpunan : 

superhero = {'wiro sableng','gundala','gatot kaca',}

superhero.add('mak lampir')     # bila menambah data secara acak ururtannya
superhero.add('gundala')        # bila menambah data yang sama dalam set,tidak akan menambah jumlahnya

for i in  superhero:
    print(i)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,}
prima = {2,3,5,7}

a = ganjil.union(genap)     # menyatukan kedua masing data
print(a)
b =  ganjil.intersection(prima)     # menampilkan data sama yang berada dalam 2 set berbeda
print(b)




