n1=int(input("Ingrese número 1= "))
n2=int(input("Ingrese número 2= "))
r1=0
r2=0
for i in range(1,n1):
    if n1%i==0:
        r1+=i

for i in range(1,n2):
    if n1%i==0:
        r2+=i 

if r1==r2:
    print("Los números son amigos")
else:
    print("Los números no son amigos")
