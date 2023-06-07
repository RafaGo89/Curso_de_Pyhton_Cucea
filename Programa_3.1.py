#si mes es julio y tengo más de 1000 pesos y que sea mayor de edad, me voy a la playa
mes = input ("¿En qué mes estamos? ")

dinero = int (input ("¿Cuánto dinero tienes? "))

edad = int (input ("¿Cuál es tu edad? "))

if (mes.lower() == "julio" and dinero > 1000) and edad >= 18:
    print ("¡Nos vamos a la playa!")