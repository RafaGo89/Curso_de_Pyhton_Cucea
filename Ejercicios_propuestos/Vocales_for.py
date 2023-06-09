frase = input ("Ingrese una frase: ")

aContador = 0
eContador = 0
iContador = 0
oContador = 0
uContador = 0

print ("\nLas vocales de esa frase son: ")

for vocal in frase: 
    if vocal.lower() == "a" and aContador == 0:
        print (vocal)
        aContador += 1
    
    elif vocal.lower() == "e" and eContador == 0:
        print (vocal)
        eContador += 1
    
    elif vocal.lower() == "i" and iContador == 0:
        print (vocal)
        iContador += 1
    
    elif vocal.lower() == "o" and oContador == 0:
        print (vocal)
        oContador += 1
        
    elif vocal.lower() == "u" and uContador == 0:
        print (vocal)
        uContador += 1