# membuat gabungan rentang angka 

# ++++ 3 ---- 10 ++++

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10 : "))

# Memeriksa angka kurang dari 3

isKurangDari =  (inputUser < 3)
print ("Kurang dari 3 : ",isKurangDari)

# Memeriksa angka lebih dari 10

isLebihDari =  (inputUser > 10)
print ("Lebih Dari 10 : ",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan : ",isCorrect)
print()


#Kasus Irisan 
#----- 3 +++++ 10 -----

inputUser = float(input("Masukkan angka yang bernilai lebih  dari 3 dan kurang dari 10 : "))

# Memeriksa angka lebih dari 3

isLebihDari =  (inputUser > 3)
print ("Lebih dari 3 : ",isLebihDari)

# Memeriksa angka kurang  dari 10

isKurangDari =  (inputUser < 10)
print ("Kurang Dari 10 : ",isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan : ",isCorrect)












