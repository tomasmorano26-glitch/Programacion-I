arch = open("jugadores.txt", "a")
arch.close()

opcion = -1
while opcion != 0:
    print("\nMENU")
    print("1- Inscribir jugadores")
    print("2- Mostrar inscriptos")
    print("3- Buscar jugador")
    print("4- Dar de baja jugador")
    print("5- Modificar categoria")
    print("0- Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        cant = int(input("Cuantos jugadores quiere inscribir: "))
        arch = open("jugadores.txt", "a")
        for i in range(cant):
            nom = input("Nombre: ")
            cat = input("Categoria: ")
            arch.write(nom + "," + cat + "\n")
        arch.close()
        print("Jugadores guardados")

    elif opcion == 2:
        arch = open("jugadores.txt", "r")
        print("Lista de inscriptos:")
        for linea in arch:
            datos = linea.strip().split(",")
            print(datos[0], "-", datos[1])
        arch.close()

    elif opcion == 3:
        nom = input("Nombre del jugador: ")
        encontrado = False
        arch = open("jugadores.txt", "r")
        for linea in arch:
            datos = linea.strip().split(",")
            if datos[0] == nom:
                print("Esta inscripto en categoria", datos[1])
                encontrado = True
        arch.close()
        if encontrado == False:
            print("No esta inscripto")

    elif opcion == 4:
        nom = input("Nombre del jugador a dar de baja: ")
        arch = open("jugadores.txt", "r")
        lineas = arch.readlines()
        arch.close()
        encontrado = False
        arch = open("jugadores.txt", "w")
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0] != nom:
                arch.write(linea)
            else:
                encontrado = True
        arch.close()
        if encontrado == True:
            print("Jugador dado de baja")
        else:
            print("Ese jugador no esta inscripto")

    elif opcion == 5:
        nom = input("Nombre del jugador: ")
        arch = open("jugadores.txt", "r")
        lineas = arch.readlines()
        arch.close()
        encontrado = False
        arch = open("jugadores.txt", "w")
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[0] == nom:
                cat = input("Nueva categoria: ")
                arch.write(nom + "," + cat + "\n")
                encontrado = True
            else:
                arch.write(linea)
        arch.close()
        if encontrado == False:
            print("Ese jugador no esta inscripto")

    elif opcion != 0:
        print("Opcion incorrecta")