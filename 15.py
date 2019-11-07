import random
A=random.randint(5,73)
print("Seat number: " + str(A))
if A % 2 == 0:
    print("Upper seat")
    
if A % 2 == 1:
    print("lower seat")
    
if A > 36 :
    print("Side seat")
    
if A <= 36 :
    print("A place in the coupe")
