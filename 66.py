import random
M = random.randint(1,100)
arr = [random.randint(1,10) for i in range(M)]
n = 1
m = 0
N = 76329
for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[i]) > 0:
        n += 1
    if int(arr[i]) < 0:
        m += 1
    if int(arr[i]) == 76329 :
        break
print("Процент положительных чисел: " + str(100 / len(arr) * n ))
print("Процент отрицательных чисел: " + str(100 / len(arr) * m ))
