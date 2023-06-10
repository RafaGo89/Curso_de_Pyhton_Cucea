numero = 21
contador = 0

while numero < 0 or numero > 20:
    numero = int (input ("Ingrese un número: "))
    contador += 1

print (f"\n{numero} está en el rango 0-20")
print (f"Se ingresaron {contador} números")