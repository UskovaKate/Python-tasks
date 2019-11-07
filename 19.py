import random
import math
X=random.randint(-10,10)
print("X = " + str(X))

Y=random.randint(-20,10)
print("Y = " + str(Y))

Z=random.randint(2,80)
print("Z = " + str(Z))

if X > 0 and Y > 0 and Z > 0:
    print("Triangle exists")
    A=max(X,Y,Z)
    B=math.sqrt(X**2 + Y**2 + Z**2 - A**2)
    if A == B:
        print("Right triangle")
    elif A != B:
        print("Not right triangle")
elif X <=0 or Y <= 0 or Z <= 0:
    print("Triangle not exists")
