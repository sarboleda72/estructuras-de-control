ni=int(input("Ingrese número inicial= "))
nf=int(input("Ingrese número final= "))
m=int(input("Ingrese número Multiplo= "))
r=0
for i in range(ni,nf+1):
    if i%m==0:
        r+=1    

print(f"La cantidad de multiplos de {m} en el rango {ni} a {nf} es {r}")


