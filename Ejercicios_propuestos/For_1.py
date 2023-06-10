numero1 = int (input ("Ingrese un número: "))
numero2 = int (input ("Ingrese un número: "))

if numero1 > numero2:
    max = numero1
    min = numero2

else:
    max = numero2
    min = numero1

rango = range (min, max + 1)

print (f"Número pares del rango {min}-{max}: ")
for i in rango:
    if i % 2 == 0:
        print (i)
        
print (f"Número impares del rango {min}-{max}: ")
for i in rango:
    if i % 2 != 0:
        print (i)