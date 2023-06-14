class persona:
    nombre:str
    edad:int
    
    def saludos ():
        print (f"Hola mi nombre es")
    
persona1 = persona   #persona1:persona  
persona1.nombre = "Rafa"
persona1.edad = 19


print (persona1.nombre)
persona1.saludo ()
print (persona1.edad)