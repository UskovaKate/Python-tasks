import random

X=random.randint(-10,10)
print("X= " +str(X))
a=random.randint(-10,10)
b=random.randint(-10,10)
if b>a:
    print("[a,b]= " + "[" + str(a) + "," + str(b) + "]")
    if a <= X and X <= b:
        print("The number belongs to the span")
    elif a > X or X > b:
        print("The number not belongs to the span")
elif a>b:
    print("ERROR")
