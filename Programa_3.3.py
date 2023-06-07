precioDeLaManzana = int (input ("¿Cuál es el precio de las manzanas? "))

cantidadDeManzanas = int (input ("¿Cuántas manzanas se compraron? "))

descuento = 0

if cantidadDeManzanas > 10:
    descuento = (precioDeLaManzana * cantidadDeManzanas) * 0.10 
    print (f"Te hicimos un descuento de ${descuento}")

print ("*Las manzanas estan en " + str(precioDeLaManzana))
#print ("*Las manzanas estan en " , precioDeLaManzana)
#print (f"*Las manzanas estan en {precioDeLaManzana}")

print ("*Y fueron " + str(cantidadDeManzanas))

print ("*Vas a pagar " + str(precioDeLaManzana * cantidadDeManzanas - descuento))