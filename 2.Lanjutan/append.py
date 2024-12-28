# x = [[1,2,3],[2,3,4],[3,4,5]]

# val = []          # bakal jadi data akhir

# for f in x:         #f = [1,2,3] [2,3,4] [3,4,5]
#     nilai = 0
#     for z in f:         #z = 1 2 3 2 3 4 3 4 5
        
#         nilai = z + nilai

#     val.append(nilai)

# print(val)


c = [[9,8,7],[6,5,4],[3,2,1]]

d =[]

for b in c:
    
    nilai = 0
    for a in b:
        nilai = a + nilai
    
    d.append(nilai)
print(d)