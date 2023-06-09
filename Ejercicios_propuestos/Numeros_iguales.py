numero1 = int (input ("Ingrese un número: "))
numero2 = int (input ("Ingrese un número: "))
numero3 = int (input ("Ingrese un número: "))

if numero1 == numero2 and numero2 == numero3:
    print ("Los 3 números son iguales")
    
elif numero1 == numero2 or numero2 == numero3 or numero3 == numero1:
    print ("Hay 2 números iguales")
    
else: 
    print ("Los 3 números son distintos")