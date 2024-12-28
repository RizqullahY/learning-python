# membuat gabungan rentang angka 

# ----- 0 +++++ 5 ------ 8 +++++ 11 -----





inputUser = float(input("Masukkan angka yang berada diantara  0 Sampai 5 atau 8 Sampai 11 : "))
KosongAtas = (inputUser > 0)
LimaBawah = (inputUser < 5 )
print('Diantara 0 - 5 :',KosongAtas and LimaBawah)
DlapanBawah = (inputUser > 8)
LasBawah = (inputUser < 11)
print('Diantara 8 - 11 : ',DlapanBawah and LasBawah)
print()

isCorrect = KosongAtas and LimaBawah or DlapanBawah and LasBawah
print("Angka yang anda masukkan : ",isCorrect)




# +++++ 0 ----- 5 ++++++ 8 ----- 11 +++++
print()

AnsUser =  float(input('Masukkan angka dibawah 0 atau antara 5 sampai 8 atau diatas 11'))
print()

Kenol = AnsUser <= 0
print('Angka Dibawah 0 :',Kenol)
Alima = AnsUser > 5
Kelapan = AnsUser < 8
print('Angka Antara 5 ampai 8 : ',Alima and Kelapan)
Atalas = AnsUser > 11 
print('Angka Diatas Sebelas : ',Atalas)

Kesimpulan = Kenol or Alima and Kelapan or Atalas
print()

print('Angka Yang Anda Masukkan : ',Kesimpulan)
























