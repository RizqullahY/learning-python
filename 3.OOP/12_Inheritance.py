class Hero():
    def __init__(self,name,health):
        self.name = name
        self.health = health
class Hero_Strenght(Hero):
    pass

Axe = Hero('Axe',500)
Tech = Hero_Strenght('Tech',1690)
print(Axe.__dict__)
print(Tech.__dict__)
