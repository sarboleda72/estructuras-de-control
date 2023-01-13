n=int(input("Ingrese número= "))
r=0
for i in range(1,n):
    if n%i==0:
        r+=i    
if r==n:
    print("Es un número perfecto")
else:
    print("No es un número perfecto")

