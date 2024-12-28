#data integer : angka satuan yang gak ada komanya

from ctypes import c_double


data_integer = 13
print("data :",data_integer)
print("bertipe :", type(data_integer))


#data float : angka satuan yang memilki koma

data_float = 1.3
print("data :",data_float)
print("bertipe :", type(data_float))


#data string : kumpulan karakter

data_string = "Malam"
print("data :",data_string)
print("bertipe :", type(data_string))


#data boolean : biner (true/false)

data_bool= False
print("data :",data_bool)
print("bertipe :", type(data_bool))


#data kompleks

data_complex =complex(5,6)
print("data :",data_complex)
print("bertipe :", type(data_complex))


#data dari bahasa C

data_C_double = c_double(10.5)
print("data :",data_C_double)
print("bertipe :", type(data_C_double))

#list
data_list = [1,2,3,4]
print("data :",data_list)
print("bertipe :", type(data_list))

#tuple
data_tuple = (1,2,3,4)
print("data :",data_tuple)
print("bertipe :", type(data_tuple))

#CASTING DATA : merubah 1 tipe data ke tipe data yang lain

