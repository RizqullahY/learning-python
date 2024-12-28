class Hero():
    def __init__(self,name,health,power):       # fungi self dari class hero
        self.__name = name
        self.__health = health
        self.__power = power

    def getName(self):          # fungsi ini berfungsi untuk melindungi parameter self agar tidak dapat diubah kedepannya
        return self.__name

    def getHealth(self):
        return self.__health

    def diSerang(self,damageLawan):
        self.__health -= damageLawan


# awal dari game
earthshaker = Hero('earthshaker',560,230)

# print(earthshaker.name)       # tidak bisa memanggil langsung
# print(earthshaker.getName())    # hanya bisa dipanggil dengan fungsi 

''' contoh value yang diganti 
semisal parameter tidak dimasukkan kedalam fungsi'''

# earthshaker.__power = 247
# print(earthshaker.__power)

print(earthshaker.getHealth())      # nilai awal
earthshaker.diSerang(81)
print(earthshaker.getHealth())      # nilai akhir

