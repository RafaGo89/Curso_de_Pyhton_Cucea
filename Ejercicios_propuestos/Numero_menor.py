numero1 = int (input ("Ingrese un número: "))
numero2 = int (input ("Ingrese otro número: "))

if numero1 == numero2:
    print ("Ambos números son iguales")

elif numero1 < numero2:
    print (f"El {numero1} es el número menor")

else:
    print (f"El {numero2} es el número menor")