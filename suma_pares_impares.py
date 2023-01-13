n=int(input("Ingrese número= "))
sp=0
si=0
for i in range(n+1):
    if i%2==0:
        sp+=i
    else:
        si+=i

print(f"La suma de los pares es {sp} y la de los impares es {si}")
