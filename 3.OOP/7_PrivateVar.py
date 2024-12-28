class Hero():

    # class variable
    jumlah = 0

    def __init__(self,nama,power):
        self.nama = nama
        self.power = power

        # variable intance private menambahkan variable diluar class
        self.__private = 'private'      # bila diawali __ makaa akan tampil 'Hero'  
        self.protect = 'protect'        # ini tidak




Acer = Hero('Acer',65)
# print(Acer.nama)
# print(Acer.__dict__)
print(Acer.protect)     # bisa dirun
print(Acer.__private)   # tidak bisa