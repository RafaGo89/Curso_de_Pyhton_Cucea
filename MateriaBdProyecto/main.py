import Menu
import MateriaDAO
import BorrarPantalla

continuar = True

while continuar == True:
    Menu.menuPrincipal()

    opcion = int (input ("Ingresa una opción: "))

    if opcion == 1:
        id = input ("Ingrese el id de la materia: ")
        title = input ("Ingrese el nombre de la materia: ")
        
        MateriaDAO.altaMateria(id, title)
        
    elif opcion == 2:
        id = input ("Ingrese el id de la materia: ")
        
        MateriaDAO.verMateria(id)
        
    elif opcion == 3:
        MateriaDAO.verTodasMateria()
        
    elif opcion == 4:
        id = input ("Ingrese el id de la materia: ")
        title = input ("Ingrese el nuevo nombre de la materia: ")
        
        MateriaDAO.modificarMateria(id, title)

    elif opcion == 5:
        id = input ("Ingrese el id de la materia: ")
        
        MateriaDAO.eliminarMateria(id)

    respuesta = int (input ("\n*Ingrese un 1 para hacer algo más, cualquier otro número para salir: "))

    if respuesta != 1:
        continuar = False
        
    else:
        BorrarPantalla.limpiar()