n1=float(input("Ingrese el número 1= "))
n2=float(input("Ingrese el número 2= "))
n3=float(input("Ingrese el número 3= "))
if n1>n2 and n1>n3:
    print(f"El número {n1} es mayor")
elif n2>n1 and n2>n3:
    print(f"El número {n2} es mayor")
elif n3>n1 and n3>n2:
    print(f"El número {n3} es mayor")
else:
    print(f"Los número son iguales")