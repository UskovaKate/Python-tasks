import random

A=random.randint(1,10)
print ("(A): Box length = " + str(A) + " meters")

B=random.randint(1,10)
print ("(B): Box width = " + str(B) + " meters")

C=random.randint(1,10)
print ("(C): Box height = " + str(C) + " meters \n")

M=random.randint(1,10)
print ("(M): Door height = " + str(M) + " meters")

K=random.randint(1,10)
print ("(K): Door width = " + str(K) + " meters \n")

Sb = B * C
print ("(Sb): Box area  = " + str(Sb) + " meters^2")
Sd = M * K 
print ("(Sd): Door area  = " + str(Sd) + " meters^2 \n")

if Sb <= Sd :
    print ("The box will go through the door")
    
if Sb > Sd :
    print ("The box won't go through the door")
