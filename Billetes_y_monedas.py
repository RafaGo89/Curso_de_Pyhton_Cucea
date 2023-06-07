cantidad = int (input ("Ingrese una cantidad en pesos: "))

print (f"Cantidad = {cantidad}")

print (f"{cantidad // 1000} billetes de $1000")
cantidad %= 1000

print (f"{cantidad // 500} billetes de $500")
cantidad %= 500

print (f"{cantidad // 200} billetes de $200")
cantidad %= 200

print (f"{cantidad // 100} billetes de $100")
cantidad %= 100

print (f"{cantidad // 50} billetes de $50")
cantidad %= 50

print (f"{cantidad // 20} billetes de $20")
cantidad %= 20

print (f"{cantidad // 10} billetes de $10")
cantidad %= 10

print (f"{cantidad // 5} billetes de $5")
cantidad %= 5

print (f"{cantidad // 2} billetes de $2")
cantidad %= 2

print (f"{cantidad // 1} billetes de $1")
cantidad %= 1