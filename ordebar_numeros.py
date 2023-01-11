n1=float(input("Ingrese el primer número= "))
n2=float(input("Ingrese el Segundo número= "))
n3=float(input("Ingrese el Tercer número= "))
if n1>n2 and n1>n3:
    mayor=n1
    if n2>n3:
        medio=n2
        menor=n3
    else:
        medio=n3
        menor=n2
elif n2>n1 and n2>n3:
    mayor=n2
    if n1>n3:
        medio=n1
        menor=n3
    else:
        medio=n3
        menor=n1
elif n3>n1 and n3>n2:
    mayor=n3
    if n1>n2:
        medio=n1
        menor=n2
    else:
        medio=n2
        menor=n1

print(f"Le número mayor es {mayor}, el número intermedio es {medio}, el número menor es {menor}")