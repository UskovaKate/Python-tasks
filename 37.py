import random
N=random.randint(1,100)
arr=[random.randint(-10,100) for i in range(N)]
print(arr)

L = sum(arr)
print("Sum arr: " + str(S))

K=0
for i in range(N):
    if arr[i] >= 0:
        K+=1
print("Positive numbers in array: " + str(K))

arr.insert(0, S)
arr.insert(1, K)
print(arr)
