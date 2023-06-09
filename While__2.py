tabla = int  (input ("¿Cuál es la tabla que quieres ver? "))
limite = int (input ("¿Hasta que número quieres que llegue la tabla? "))

contador = 1

while contador <= limite:
    print (f"{tabla} x {contador} = {tabla * contador}")
    contador += 1   