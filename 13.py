import random
import math
D = random.randint(1,10)
print("(D) The cross-sectional diameter = " + str(D))

A = random.randint(1,10)
print("(A) Square bar width = " + str(A))

d = A * math.sqrt(2)
print("(d) Diagonal bar = " + str(d))

if D >= d :
    print("It is possible from a log to saw a square bar")
    
if D < d :
    print("It is impossible to saw from a log a square bar")
