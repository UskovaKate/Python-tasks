import random
import math

X=random.randint(2,2000)
print("X= " + str(X))
Y=random.randint(2,2000)
print("Y= " + str(Y))

if X > Y:
    Z=math.sqrt(X*Y)
    print("true")
    print("Z= " + str(Z))
elif X <= Y:
    Z=math.log(X + Y)
    print("false")
    print("Z= " + str(Z))
