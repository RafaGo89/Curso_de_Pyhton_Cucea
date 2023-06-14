#verifique si una palabra se encuentra contenida en otra, al derecho y al reves e imprima un si,
#si se encuentra contenida, y un no si no se encuentra contenida

palabra1 = input ("Ingrese una palabra: ")

palabra2 = input ("Ingrese una palabra: ")
palabra2Invertida = ""

if palabra1.lower() in palabra2.lower():
    print ("Sí")

else:
    for letra in reversed (palabra2):
        palabra2Invertida += letra
    
    if palabra1.lower() in palabra2Invertida.lower():
        print ("Sí")
    
    else:
        print ("No")
