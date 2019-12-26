import random

M = random.randint(1,100)
K = random.randint(1,10)
P = random.randint(1,190)
N = random.randint(1,4)

arr = [random.randint(1,100) for i in range(N)]
print("N= " + str(N))
print("K= " + str(K))
print("P= " + str(P))
print("M= " + str(M))
print(arr)

arr[K : M + K + 1] , arr[P : M+P+1] = arr[P : M+P+1] , arr[K : M+K+1]
print(arr)
