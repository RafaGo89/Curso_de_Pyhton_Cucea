frase = input ("Ingrese una frase: ")

aContador = eContador = iContador = oContador = uContador = False

print ("\nLas vocales de esa frase son: ")

for vocal in frase: 
    if vocal.lower() == "a" and aContador == False:
        print (vocal)
        aContador = True
    
    elif vocal.lower() == "e" and eContador == False:
        print (vocal)
        eContador = True
    
    elif vocal.lower() == "i" and iContador == False:
        print (vocal)
        iContador = True
    
    elif vocal.lower() == "o" and oContador == False:
        print (vocal)
        oContador = True
        
    elif vocal.lower() == "u" and uContador == False:
        print (vocal)
        uContador = True
