n1=float(input("Ingrese número 1= "))
n2=float(input("Ingrese número 2= "))
op=input("Ingrese operador +, -, *, /= ")
if op=="+":
    r=n1+n2
elif op=="-":
    r=n1-n2
elif op=="*":
    r=n1*n2
elif op=="/":
    if n2==0:
        r=0
    else:
        r=n1/n2
else:
    print("No ingreso un operador correcto")
print("-"*25)
print(f"El resultado de la operación {n1}{op}{n2} es= {r}")