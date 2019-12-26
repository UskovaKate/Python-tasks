import random

N = random.randint(1,100)
arr=[random.randint(0,10) for i in range(N)]
print(arr)

for i in range(N):
    if arr[i] == 0:
        arr[i] = []


print(arr)
