class Persona:
    def __init__(self, nombre, edad, status, carrera, codigo):
        self._nombre = nombre  #el guion bajo es para hacerlo privado
        self._edad = edad
        self._status = status
        self._carrera = carrera
        self._codigo = codigo
        
    def __str__(self):
        return f"hola mi nombre es {self._nombre} y mi edad es {self._edad} persona"
    
class Estudiante (Persona):
    def __init__ (self, nombre, edad, status, carrera, codigo, promedio, semestre):
        super().__init__(nombre, edad, status, carrera, codigo)
        self._promedio = promedio
        self._semestre = semestre

    def __str__(self):
        return f"Hola, mi nombre es {self._nombre} y mi edad es {self._edad} alumno"

persona1 = Persona('raul',19, 'activo', 'licenciatura', 1234)
alumno1 = Estudiante('raul2', 29, 'activo', 'licenciatura', 890, 89, 9)

print(f'{persona1._codigo} {persona1._nombre}')
print(f'{alumno1._codigo} {alumno1._nombre}')

print(f'{persona1}')
print(f'{alumno1}')