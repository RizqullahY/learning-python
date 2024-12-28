input = [100,200,300,400,500]
compared_input = [500,200,400]
x = 0    #jadikan indexnya 0
for elemen in input:     #elemen adalah value di dalam input : akan di beri aksi

    if elemen in compared_input:     #jika 'elemen' ada di dalam compared_input
        input[x] = 0     #maka menjadi 0
        
    x += 1  #bertambah 1 indexnya seiring waktu



print(input)



input = [100,200,300,400,500]
compared_input = [500,200,400]

for i in range(len(input)):
    if input[i] in compared_input:
        input[i] = 0
        
        
print(input)



input = [100,200,300,400,500]
compared_input = [500,200,400]

for index, x in enumerate(input):
    for y in compared_input:
        if x == y:
            input[index] = 0

print(input)




input = [
    {'nama':'budi','gaji':5000},
    {'nama':'dwi','gaji':8000},
    {'nama':'joko','gaji':6000},
]

output = {}

gaji_tertinggi = 0 ;
total_gaji = 0 
nama_karyawan_gaji_tertinggi= '';

for i in range (len(input)):
    if gaji_tertinggi < input [i]['gaji']:
        gaji_tertinggi = input [i]['gaji'] 
        nama_karyawan_gaji_tertinggi = input [i]['nama'] 

    total_gaji += input [i]['gaji']

output['highest_salary'] = nama_karyawan_gaji_tertinggi
output['total_salary'] = total_gaji
print (output)











