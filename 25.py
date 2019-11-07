import random
import math

A=random.randint(-1,10)
print("A= " + str(A))
x=A

if x <= 2:
    f= x**2 + 4*x + 5
    print("x <= 2")
    print("f(A)= x**2 + 4*x + 5 = " + str(f))
elif not x <= 2:
    f= 1/(x**2 + 4*x + 5)
    print("x > 2")   
    print("f(A)= 1/(x**2 + 4*x + 5) = " + str(f))
