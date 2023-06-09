anno = int (input ("Ingrese un año: "))

if anno % 4 == 0:
    if anno % 100 != 0:
        print (f"{anno} es un año bisiesto")

    elif anno % 400 == 0:
        print (f"{anno} es un año bisiesto")
    
else:
    print (f"{anno} no es un año bisiesto")