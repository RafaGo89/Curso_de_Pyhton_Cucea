import string

contador = 0

frase = input ("Ingrese una frase: ")

for letra in list(string.ascii_lowercase):  #guardo el abecedario en minúsculas con esa list
    if letra in frase.lower():
        contador += 1
        
if contador == 26:
    print ("Es un pangrama")

else:
    print ("No es un pangrama")