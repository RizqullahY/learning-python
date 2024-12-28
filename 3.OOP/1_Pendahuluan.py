# class Hero():   # template
#     pass

# hero1 = Hero()  # object / instance
# hero2 = Hero()
# hero3 = Hero();

# hero1.name = 'Perav'
# hero1.health = 320

# hero2.name = 'Youn'
# hero2.health = 150

# hero3.name = 'Rougter'
# hero3.health = 100

# print(hero1)            # akan muncul<__main__.Hero object at 0x000002A9506B7D60>
# print(hero2.name)       # akan muncul Youn
# print(hero3.__dict__)   # akan muncul {'name': 'Rougter', 'health': 100}

class Hero():
    jumlah =  0

    def __init__(self,InputName,InputAttack,InputHealth):
        self.name = InputName
        self.attack = InputAttack
        self.health = InputHealth
        Hero.jumlah += 1
        print('program was summon '+ InputName)

    def who(self):      # void fuction method tanpa return
        print("npc's name is " + self.name)
    def Healing():
        print()

hero1 = Hero('Miren',65,970)
print(Hero.jumlah)
hero1.who()
# print(hero1.name,hero1.attack,hero1.health)
hero2 = Hero('Ruin',8,35)
print(Hero.jumlah)

class Villain():
    def __init__(self,InputName,InputAttack,InputHealth):
        self.name = InputName
        self.attack = InputAttack
        self.health = InputHealth

# villain1 = Villain('Outex',56,1070)
# print(villain1.name,villain1.attack,villain1.health)
# print(Hero.__dict__)        # menampilkan variabel statik
