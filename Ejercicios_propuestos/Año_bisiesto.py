anno = int (input ("Ingrese un año: "))

if anno % 4 != 0: #no divisible entre 4
	print(f"{anno} no es bisiesto")
 
elif anno % 4 == 0 and anno % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print(f"{anno} es bisiesto")
 
elif anno % 4 == 0 and anno % 100 == 0 and anno % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print(f"{anno} es bisiesto")
 
elif anno % 4 == 0 and anno % 100 == 0 and anno % 400 == 0: #divisible entre 4, 100 y 400
	print(f"{anno} es bisiesto")