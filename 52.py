import random
K = random.randint(1,100)
arr = [random.randint(1,10) for i in range(K)]

for i in range(K):
    arr[i] = input()
print(arr)
b = arr[0]

for i in range(1 , K):
    b = str(b) + " " + arr[i]
print(b)
