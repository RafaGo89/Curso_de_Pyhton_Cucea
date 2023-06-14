class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  #el guion bajo es para hacerlo privado
        self._edad = edad
        
    @property
    def edad(self):
        return f"{self._edad} años"
    
    @edad.setter
        def edad (self, edad):
            self._edad = edad
        
    def saludo (self):
        print (f"Hola, mi nombre es {self._nombre} y mi edad es {self._edad}")

persona1 = Persona ("Rafa", 19)
persona2 = Persona ("Joaquín", 15)

persona1.saludo ()
persona2.saludo ()