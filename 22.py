import random
A=random.randint(-10,10)
print("A= " + str(A))
B=random.randint(-10,10)
print("B= " + str(B))
C=random.randint(-10,10)
print("C= " + str(C) + "\n")
print("A < B < C   and   A > B > C""\n")

if A<B and B<C:
    print("The first inequality is true")
elif A>B or B>C:
    print("The first inequality is fals")
    
if A>B and B>C:
    print("The second inequality is true")
elif A<B or B<C:
    print("The second inequality is false")
