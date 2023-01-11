n=int(input("Ingrese un número= "))
c=0
while n!=0:
    n=int(n/10)
    c+=1
print(f"Tiene {c} digitos")