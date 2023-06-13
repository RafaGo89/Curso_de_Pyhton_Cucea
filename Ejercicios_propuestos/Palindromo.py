frase = input ("Ingrese una frase: ")
fraseInvertida = ""

frase = frase.replace ( " " , "" )

for letra in reversed (frase):
    fraseInvertida += letra

if frase.lower() == fraseInvertida.lower():
    print ("Es un palíndromo")

else:
    print ("No es un palíndromo")