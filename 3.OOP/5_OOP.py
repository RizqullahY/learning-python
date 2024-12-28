class Hero():
    def __init__(self,nama,darah,power):
        self.nama = nama
        self.darah = darah
        self.power = power

    def serang(self,lawan):
        print(self.nama + ' menyerang ' + lawan.nama)
        lawan.diserang(self,self.power)                            

    def diserang(self,lawan,power_lawan):           # fungsi dibawah ditaruh di atas agar efektif cukuf memanggil fungsi yang diatas
        print(self.nama + ' diserang ' + lawan.nama)
        attack_diterima = power_lawan
        print('serangan yang diterima :' + str(attack_diterima))
        self.darah -= attack_diterima
        print('darah '+self.nama + ' tersisa :'+str(self.darah))

Blane = Hero('Blane',500,45)
Zorn = Hero('Zorn',350,95)
# print(Blane.nama,Blane.darah,Blane.power)

Zorn.serang(Blane)      # pd fungsi self menggantikan blane
# Zorn.diserang()       # pemanggilan fungsi menjadi otomatis,ditaruh di fungsi serang agar sekalian