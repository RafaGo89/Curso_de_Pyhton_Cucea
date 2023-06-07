precioDeLaManzana = int (input ("¿Cuál es el precio de las manzanas? "))

cantidadDeManzanas = int (input ("¿Cuántas manzanas se compraron? "))

descuento = 0

if cantidadDeManzanas > 10:
    descuento = (precioDeLaManzana * cantidadDeManzanas) * 0.10 

print ("*Las manzanas estan en " + str(precioDeLaManzana))

print (f"*Y fueron {cantidadDeManzanas}")

if descuento > 0: 
    print (f"Pagarías {precioDeLaManzana * cantidadDeManzanas} pero te hicimos un descuento de ${descuento} entonces\n")

print (f"*Vas a pagar {precioDeLaManzana * cantidadDeManzanas - descuento}")