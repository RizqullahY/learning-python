# Bubble Sort

def bubblesort(S):
  n = len(S)
  for i in range(n):
    print(S) # untuk mengetahui proses yang terjadi
    for j in range(n - 1):
      if S[j] > S[j + 1]:
        S[j], S[j + 1] = S[j + 1], S[j]
        
S = [50,30,40,10,20]
print("Sebelum di sortir", S)
bubblesort(S)
print("Setelah di sortir", S)




# Selection Sort

def selectionsort(S):
  n = len(S)
  for i in range(n - 1):
    print(S)
    smallest = i
    for j in range(i + 1,n):
      if S[j] < S[smallest]:
        smallest = j
    S[i], S[smallest] = S[smallest], S[i]

S = [50,30,40,10,20]
print("Sebelum di sortir", S)
selectionsort(S)
print("Setelah di sortir", S)



# Insertion Sort

def insertionsort(S):
  n = len(S)
  for i in range(1, n):
    print(S)
    x = S[i]  
    j = i - 1
    while j >= 0 and S[j] > x:
      S[j + 1] = S[j]
      j -= 1
    S[j + 1] = x
    
S = [50,30,40,10,20]
print("Sebelum di sortir", S)
insertionsort(S)
print("Setelah di sortir", S)




# Merge Sort

def insertionsort(S):
  n = len(S)
  for i in range(1, n):
    print(S)
    x = S[i]  
    j = i - 1
    while j >= 0 and S[j] > x:
      S[j + 1] = S[j]
      j -= 1
    S[j + 1] = x
    
S = [50,30,40,10,20]
print("Sebelum di sortir", S)
insertionsort(S)
print("Setelah di sortir", S)



# Quick Sort

def partition1(S,low,high):
  pivot = S[low]
  left, right = low + 1, high
  while left < right:
    print(S)
    while left <= right and S[left] <= pivot:
      left += 1
    while left <= right and S[right] >= pivot:
      right -= 1
    if left < right:
      S[left],S[right] = S[right],S[left]
  pivotpoint = right
  S[low], S[pivotpoint] = S[pivotpoint], S[low]
  return pivotpoint

def quicksort1(S,low,high):
  if low < high:
    print(S)
    pivotpoint = partition1(S,low,high)
    quicksort1(S,low,pivotpoint - 1)
    quicksort1(S, pivotpoint + 1,high)

S = [25,22,20,15,13,12,10]
quicksort1(S,0,len(S) - 1)
print(S)