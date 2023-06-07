dia = input ("Ingresa el día de la semana: ")

if dia.lower() == "lunes" or dia.lower() == "miercoles":
    print ("Toca curso")
    
elif dia.lower() == "viernes":
    print ("Toca curso")
    print ("Toca peda")
    
elif dia.lower() == "sabado":
    print ("Toca más peda")
    
elif dia.lower() == "domingo":
    print ("Toca ir a misa")
     
else:
   print ("No toca curso") 