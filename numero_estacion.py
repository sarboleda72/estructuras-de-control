n=int(input("Ingrese número del mes= "))
if n>=1 and n<=3:
    print("Verano")
elif n>=4 and n<=6:
    print("Otoño")
elif n>=7 and n<=9:
    print("Invierno")
elif n>=10 and n<=12:
    print("Primavera")
else:
    print("El número del mes que ingreso no existe")