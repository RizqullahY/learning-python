print('----Kotak----')
# Kotak

for i in range(0,5):            # panjang ke bawah
    for j in range(0,5):        # panjang ke samping
        print('X',end='')
    print()


print('----Kotak Bolong----')
# Kotak Bolong

ukuran = 5
for i in range(ukuran):
    for j in range(ukuran):

        if i == 0 or i== ukuran - 1 or j == 0 or j == ukuran - 1:
            print('x',end=' ')
        else:
            print(' ',end=' ')
    print()

print('----Pakai While Loop(Kotak Bolong)----')
# Pakai While Loop

row = 1
lengths = 5 


while (row <= lengths):
    column = 1
    while(column <=lengths):
        if(row == 1 or row == lengths or column == 1 or column == lengths):
            print('x',end=' ')
        else:
            print(' ',end=' ')
        column = column + 1
    row = row + 1
    print()


print('----Segitiga Siku Kiri----')
# Segitiga Siku Kiri
n =  5
for i in range (1,n+1):
    for k in range (1,i+1):
        print('x',end=' ')
    print()



print('----Segitiga Siku Kanan----')
# Segitiga Siku Kanan
n =  5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if(j <= n - i):
            print(' ', end = ' ')
        else:
            print('x', end = ' ')
    print()



print('----Segitiga Siku Kiri Bolong----')
# Segitiga Siku Kiri Bolong

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if i == 1 or i == rows or j == 1 or j == i:
            print('x ', end = '')
        else:
            print(' ', end = '')
    print()

print('----Segitiga Siku Kiri Kebawah----')
# Segitiga Siku Kiri Kebawah

rows = 5
i = rows
while(i > 0):
    j = i
    while(j > 0):      
        print('x', end = '  ')
        j = j - 1
    i = i - 1
    print()



print('----Pyramid----')
# Pyramid

rows = 5
for i in range(1, rows + 1):
    for j in range(rows, i, -1):
        print(end = ' ')
    for k in range(1, i + 1):
        print('x', end = ' ')
    print()


print('----Pyramid Terbalik----')
# Pyramid Terbalik

rows = 5
i = rows
while(i >= 1):
    j = 0
    while(j <= rows - i):
        print(end = ' ')
        j = j + 1
    k = 0
    while(k < i):
        print('x', end = ' ')
        k = k + 1
    i = i - 1
    print()

print('----Diamond----')
# Diamond
rows =5
k = 0
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end = ' ')
    while k != 2 * i - 1:
        print('x', end = '')
        k = k + 1
    k = 0
    print()

k = 2
l = 1
for i in range(1, rows):
    for j in range(1, k):
        print(end = ' ')
    k = k + 1
    while l <= (2 * (rows - i) - 1):
        print('x', end = '')
        l = l + 1
    l = 1
    print()
 