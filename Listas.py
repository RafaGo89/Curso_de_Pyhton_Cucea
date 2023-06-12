miLista = [4, 6, 12, 3, 5, 19, 24]

print (miLista)

print (miLista [5])

print (len (miLista))

miLista.append (13)  #añade al final de la lista
print (miLista)

miLista.pop () #eliminar el útimo valor
print (miLista)

miLista.remove (24)
print (miLista)

miLista.sort() #acomodarla

#lista2 = miLista.copy


for contador, elemento in enumerate (miLista):
    print (f"Contador {contador} elemento {elemento}")
    
if 6 in miLista:
    print ("El 6 sí está")
    print (miLista.index(6))  #posición en la lista