mm1 = ['adam', 'irsyad', 'farhan', 'hammas']
mm2 = ['jovan', 'fahri', 'nabil']
tkj = ['rinto', 'ardika', 'rafly', 'arip']
otr = ['ahmad', 'faiz', 'rizal', 'uda']
tkr1 = ['rafa', 'aldo', 'fahmi']
tsm = ['haikal', 'mahesa']
boga = ["erick"]

masukPagi = [mm2, otr, tsm, boga]
masukSiang = [mm1, tkj, tkr1]


# Fungsi untuk menampilkan seluruh data dalam masukPagi dan masukSiang
def tampilkan_semua_data():
   semua_data = masukPagi + masukSiang
   return semua_data


# Fungsi untuk menampilkan seluruh data pada variabel paling atas
def tampilkan_variabel_paling_atas():
   data_variabel_paling_atas = [mm1, mm2, tkj, otr, tkr1, tsm, boga]
   return data_variabel_paling_atas





# Memanggil fungsi-fungsi tersebut
semua_data = tampilkan_semua_data()
variabel_paling_atas = tampilkan_variabel_paling_atas()

# Menampilkan hasil
print("1. Seluruh data pada masukPagi dan masukSiang:")
print(semua_data)
print("\n2. Data pada variabel paling atas:")
for var in variabel_paling_atas:
   print(var)
