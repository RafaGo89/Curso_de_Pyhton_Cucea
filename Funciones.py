import os

def limpiar ():
    if os.name == "posix":
        os.system ("clear")

    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    
    print ("" .center (40, "x"))

def saludo ():
    print ("Hola, buenos días")
    print ("Espero estén bien")
 