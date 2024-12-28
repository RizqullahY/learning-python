from ast import Return


class Hero():
    def __init__(self,nama,darah,power):
        self.nama = nama
        self.__darah = darah
        self.__power = power
        # self.info = " nama : {}\n darah : {}\n power : {}".format(self.__nama,self.__darah,self.__power)

    @property
    def info(self):
        return "nama : {}\n darah : {}\n power : {}".format(self.nama,self.__darah,self.__power)

Eijat = Hero('Eijat',40,16,)
print(Eijat.info)
Eijat.nama = 'Badang'
print(Eijat.info)