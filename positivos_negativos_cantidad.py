n1=int(input("Ingrese número 1= "))
n2=int(input("Ingrese número 2= "))
cp=0
cn=0
for i in range(n1,n2+1):
    if i>0:
        cp+=1
    elif i<0:
        cn+=1
print(f"La cantidad de positivos son {cp} y de negativos {cn}")