import random

N = random.randint(1,100)
arr=[random.randint(-10,10) for i in range(N)]
print(arr)

L = random.randint(1,10)
print("L= " + str(L))
K = random.randint(1,10)
print("K= " + str(K))

arr[L:L+K]=[]
print(arr)
