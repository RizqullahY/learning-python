# not , or , and , xor

a = True
b = False
c = not a

print ('Data a =',a)
print ('----------NOT')
print ('Data c =',c)
print()

# Or = jika salah satu adalah true maka hasilnya true

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c) 

a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
print()


# AND = jika ada dua buah nilai True maka hasilnya true

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

a = False
b = False
c = a and b
print(a,'AND',b,'=',c) 

a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
print()


# XOR jika salah satu saja yang true makan hasilnya true sisanya false
# jika semuanya true makan hasilnya akan false


print('--XOR--')
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c) 

a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
print()


