cantidadDeManzanas = 1

while cantidadDeManzanas != 0:

    cantidadDeManzanas = int (input ("\n¿Cuántas manzanas se compraron? "))
    
    if cantidadDeManzanas == 0:
        break
    
    precioDeLaManzana = int (input ("¿Cuál es el precio de las manzanas? "))
    
    nombre = input ("¿Cuál es tu nombre? ")

    descuento = 0

    if nombre.lower() == "rafael" or cantidadDeManzanas == 18:
        descuento = (precioDeLaManzana * cantidadDeManzanas) * 0.20
        descuentoTipo = "%20"

    elif cantidadDeManzanas >= 10:
        descuento = (precioDeLaManzana * cantidadDeManzanas) * 0.10 
        descuentoTipo = "%10"
        
    print ("Nota de venta" .center(50,"x"))

    print (f"*Las manzanas estan en {precioDeLaManzana}")

    print (f"*Y fueron {cantidadDeManzanas}")

    if descuento > 0: 
        print (f"Pagarías ${precioDeLaManzana * cantidadDeManzanas} pero te hicimos un descuento del {descuentoTipo} entonces")

    print (f"*Vas a pagar {precioDeLaManzana * cantidadDeManzanas - descuento}")

print ("\n\nGracias por vender manzanas, adios :)")