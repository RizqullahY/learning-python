

# '''Menggunakan Selection Sort'''

# def selectionsort(laci_obat_tercecer):
#   n = len(laci_obat_tercecer)
#   for i in range(n - 1):

#     # print(laci_obat_tercecer)     # melihat proses
#     smallest = i
#     for j in range(i + 1,n):
#       if laci_obat_tercecer[j] < laci_obat_tercecer[smallest]:
#         smallest = j
#     laci_obat_tercecer[i], laci_obat_tercecer[smallest] = laci_obat_tercecer[smallest], laci_obat_tercecer[i]

# laci_obat_tercecer = ['VitPlus','Cucubima','Paracetamol','Amoxilin','Rexodon','TolakAngin','Gliserol','Dulcolax','Ibuprofen']
# selectionsort(laci_obat_tercecer)
# print(laci_obat_tercecer)
# print(laci_obat_tercecer[7])




# '''Menggunakan Bubble Sort'''

# def bubblesort(S):
#   n = len(S)
#   for i in range(n):

#     # print(S) # untuk mengetahui proses yang terjadi
#     for j in range(n - 1):
#       if S[j] > S[j + 1]:       # bila item lebih besar dari item + 1
#         S[j], S[j + 1] = S[j + 1], S[j]     # maka ditukar posisinya
        













# def selectionsort(S):
#   n = len(S)
#   for i in range(n - 1):
#     print(S)
#     smallest = i
#     for j in range(i + 1,n):
#       if S[j] < S[smallest]:
#         smallest = j
#     S[i], S[smallest] = S[smallest], S[i]


# rak_produk = ['susu moli','minyak bumoli','coco tok aba','mie goreng enak',
#               'minyak bumoli','mi rebus enak','coco tok aba','susu ibu sehat',
#               'susu moli','mi goreng enak']
# print("Sebelum di sortir", rak_produk)
# selectionsort(rak_produk)
# print("Setelah di sortir", rak_produk)




searching = str(input('Barang Apa'))
rak_produk = ['susu moli','minyak bumoli','coco tok aba','mie goreng enak',
              'minyak bumoli','mi rebus enak','coco tok aba','susu ibu sehat',
              'susu moli','mi goreng enak']

def selectionsort(S):
  n = len(S)
  for i in range(n - 1):
    smallest = i
    for j in range(i + 1,n):
      if S[j] < S[smallest]:
        smallest = j
    S[i], S[smallest] = S[smallest], S[i]

selectionsort(rak_produk)

index = 1
for i in rak_produk:
        i = rak_produk.index(searching)
print('produk yang anda cari ada di rak',i)

# '''Cara 2 ON GOING'''

# x = 'coco tok aba'

# def search(list,x):
#     for idx, i in enumerate(list):
#         if x == i:
#             print(f'produk{x}ada di baris {idx}')
        
# search(list=rak_produk,)