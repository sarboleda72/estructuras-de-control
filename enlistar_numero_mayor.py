lis=[]
for i in range(0,6):
    n=float(input(f"Ingrese el numero en la posicion {i+1}= "))
    lis.append(n)
print("El numero menor ingresado es=",min(lis))
print("El numero mayor ingresado es=",max(lis))