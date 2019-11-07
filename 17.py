import random
import math

A=random.randint(1,100)
Cube=A**3
print("V Cube = " + str(Cube))

H=random.randint(1,100)
R=random.randint(1,100)
pi=math.pi
Cylinder=pi*R**2*H
print("V Cylinder = " + str(Cylinder))

M=random.randint(1,100)
print("V Woter = " + str(M))

if Cube >= M:
    print("Water will fit in to the cube,")
elif Cube < M:
    print("Water will not fit in the cube,")

if Cylinder >= M:
    print("Water will fit in to the cylinder,")
elif Cylinder < M:
    print("Water will not fit in the cylinder,")
    
if Cube >= M:
    if Cylinder >= M:
        print("Water will fit into the cube and cylinder.")
elif Cylinder < M:
    if Cube < M:
        print("Water will not fit into the cube and cylinder.")
