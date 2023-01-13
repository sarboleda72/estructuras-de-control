s0=[]
s1=[]
s2=[]
for i in range(0,12):
    if i<4:
        n=float(input(f"Ingrese el numero {i+1} de la lista 1 = "))
        s0.append(n)
    if i>3 and i<8:
        n=float(input(f"Ingrese el numero {i-3} de la lista 2 = "))
        s1.append(n)
    if i>7 and i<12:
        n=float(input(f"Ingrese el numero {i-7} de la lista 3 = "))
        s2.append(n)
    
print("La suma de los elementos de la lista 1 es=",sum(s0))
print("La suma de los elementos de la lista 2 es=",sum(s1))
print("La suma de los elementos de la lista 3 es=",sum(s2))