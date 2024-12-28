'''            Celcius       Reamur      Fahrenheit     Kelvin

Celcius                      4/5 C       9/5C +32       C+273
Reamur          5/4R                     9/4R +32       5/4R +273
Fahrenheit      5/9(F-32)    4/9(F-32)   
Kelvin          K-273        4/5(K-273)   

'''


# C = Celcius R = Reamur F = Fahrenheit K = Kelvin

from calendar import c


print("Perhitungan Celcius")
print()

C = 89

R = 4/5*C
F = 9/5*C+32
K = C+273
print("Celcius",'=',C)
print("Hasil Dalam Reamur",'=',R)
print("Hasil Dalam Fahrenheit",'=',F)
print("Hasil Dalam Kelvin",'=',K)

print()
print("Perhitungan Reamur")
print()

R = 64

C =  5/4*R
F =  9/4*R+32
K =  5/4*R +273
print("Reamur",'=',R)
print("Hasil Dalam Celcius",'=',C)
print("Hasil Dalam Fahrenheit",'=',F)
print("Hasil Dalam Kelvin",'=',K)


print()
print("Perhitungan Fahrenheit")
print()

F = 176

C = 5/9*(F-32) 
R = 4/9*(F-32) 

print("Fahrenheit",'=',F)
print("Hasil Dalam Celcius",'=',C)
print("Hasil Dalam Reamur",'=',R)


print()
print("Perhitungan Kelvin")
print()

K = 353

C = K-273   
R = 4/5*(K-273) 
print("Kelvin",'=',K)
print("Hasil Dalam Celcius",'=',C)
print("Hasil Dalam Reamur",'=',R)
