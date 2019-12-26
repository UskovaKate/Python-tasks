import random

N = random.randint(1,100)
arr=[random.randint(-10,10) for i in range(N)]
print(arr)

arrK = []
arrN = []

for i in range(N):
    if arr[i] < 0:
        arrN.append(arr[i])
    if arr[i] > 0:
        arrK.append(arr[i])
    
print(arrN)
print(arrK)
