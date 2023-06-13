import statistics

def capturarCalificaciones (calificaciones):
    for i in range (0, 10):
        valor = int  (input (f"Ingrese la calificación del alumno {i + 1}: "))
        calificaciones.append (valor)

calificaciones = []

capturarCalificaciones (calificaciones) 

promedio = statistics.mean(calificaciones)  #calcula el promedio de los valores de la lista

print (f"El promedio de la clase es de: {promedio}")