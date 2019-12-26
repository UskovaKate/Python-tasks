import random

N = random.randint(1,100)
arr = [random.randint(-10,10) for i in range(N)]
print(arr)
T = random.randint(1,10)
print("T= " + str(T))

for i in range(N):
    if arr[i] > 0:
        t = arr[i] / T
        arr[i] = t
print(arr)
