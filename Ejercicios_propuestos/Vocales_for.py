frase = input ("Ingrese una frase: ")

aContador = eContador = iContador = oContador = uContador = False

print ("\nLas vocales de esa frase son: ")

for vocal in frase: 
    if "a" in vocal.lower() and aContador == False: #si la letra "a" está "vocal (convertido a minúscula)", verdadero or falso
        print ("a")
        aContador = True
    
    elif "e" in vocal.lower() and eContador == False:
        print ("e")
        eContador = True
    
    elif "i" in vocal.lower() and iContador == False:
        print ("i")
        iContador = True
    
    elif "o" in vocal.lower() and oContador == False:
        print ("o")
        oContador = True
        
    elif "u" in vocal.lower() and uContador == False:
        print ("u")
        uContador = True