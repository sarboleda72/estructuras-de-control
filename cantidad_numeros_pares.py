n1=int(input("Número en el que inicia= "))
n2=int(input("Número en el que termina= "))
c=0
while n1<=n2:
    n1+=2
    c+=1

print(f"La cantidad de números que hay en {n1} y {n2} es de {c}")