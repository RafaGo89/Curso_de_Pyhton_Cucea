cantidad = int (input ("Ingrese una cantidad en segundos: "))

print (f"\n{cantidad} segundos son\n\n {cantidad // 3600} hora(S)\n {(cantidad % 3600) // 60} minuto(s)\n {(cantidad % 3600) % 60} segundo(s)")