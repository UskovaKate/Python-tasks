import random

N = random.randint(1,100)
arr = [random.randint(-10,10) for i in range(N)]
print(arr)
K = random.randint(1,100)
print("K= " + str(K))
L = random.randint(1,100)
print("L= " + str(L))

arr[K : L] = []
print(arr)
