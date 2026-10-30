# Actividad 03 - Ordenamiento en el torneo
import json
import os

if not os.path.exists("inscriptos.json"):
    arch = open("inscriptos.json", "w")
    json.dump([], arch)
    arch.close()

if not os.path.exists("parejas.json"):
    arch = open("parejas.json", "w")
    json.dump([], arch)
    arch.close()

opcion = -1
while opcion != 0:
    print("\nMENU")
    print("1- Inscribir jugadores")
    print("2- Mostrar inscriptos")
    print("3- Buscar jugador")
    print("4- Dar de baja jugador")
    print("5- Modificar categoria")
    print("6- Mostrar inscriptos en orden alfabetico")
    print("7- Mostrar jugadores por categoria")
    print("8- Armar pareja")
    print("9- Cargar puntos a una pareja")
    print("10- Tabla de posiciones")
    print("0- Salir")
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        cant = int(input("Cuantos jugadores quiere inscribir: "))
        for i in range(cant):
            nom = input("Nombre: ").strip()
            repetido = False
            for jugador in jugadores:
                if jugador["nombre"].strip().lower() == nom.lower():
                    repetido = True
            if repetido == True:
                print(nom, "ya esta inscripto")
            else:
                cat = int(input("Categoria: "))
                jugadores.append({"nombre": nom, "categoria": cat})
        arch = open("inscriptos.json", "w")
        json.dump(jugadores, arch, indent=4)
        arch.close()
        print("Jugadores guardados")

    elif opcion == 2:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        print("Lista de inscriptos:")
        for jugador in jugadores:
            print(jugador["nombre"], "-", jugador["categoria"])

    elif opcion == 3:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        nom = input("Nombre del jugador: ").strip()
        encontrado = False
        for jugador in jugadores:
            if jugador["nombre"].strip().lower() == nom.lower():
                print("Esta inscripto en categoria", jugador["categoria"])
                encontrado = True
        if encontrado == False:
            print("No esta inscripto")

    elif opcion == 4:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        nom = input("Nombre del jugador a dar de baja: ").strip()
        encontrado = False
        nuevos = []
        for jugador in jugadores:
            if jugador["nombre"].strip().lower() != nom.lower():
                nuevos.append(jugador)
            else:
                encontrado = True
        arch = open("inscriptos.json", "w")
        json.dump(nuevos, arch, indent=4)
        arch.close()
        if encontrado == True:
            print("Jugador dado de baja")
        else:
            print("Ese jugador no esta inscripto")

    elif opcion == 5:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        nom = input("Nombre del jugador: ").strip()
        encontrado = False
        for jugador in jugadores:
            if jugador["nombre"].strip().lower() == nom.lower():
                jugador["categoria"] = int(input("Nueva categoria: "))
                encontrado = True
        arch = open("inscriptos.json", "w")
        json.dump(jugadores, arch, indent=4)
        arch.close()
        if encontrado == False:
            print("Ese jugador no esta inscripto")

    elif opcion == 6:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        lista = jugadores.copy()
        n = len(lista)
        comparaciones = 0
        intercambios = 0
        for i in range(n - 1):
            menor = i
            for j in range(i + 1, n):
                comparaciones = comparaciones + 1
                if lista[j]["nombre"].lower() < lista[menor]["nombre"].lower():
                    menor = j
            if menor != i:
                aux = lista[i]
                lista[i] = lista[menor]
                lista[menor] = aux
                intercambios = intercambios + 1
        print("Inscriptos en orden alfabetico:")
        for jugador in lista:
            print(jugador["nombre"], "-", jugador["categoria"])
        print("Seleccion:", comparaciones, "comparaciones y", intercambios, "intercambios")

    elif opcion == 7:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        lista = jugadores.copy()
        n = len(lista)
        comparaciones = 0
        intercambios = 0
        for i in range(n - 1):
            for j in range(n - 1 - i):
                comparaciones = comparaciones + 1
                a = lista[j]
                b = lista[j + 1]
                if a["categoria"] > b["categoria"] or (a["categoria"] == b["categoria"] and a["nombre"].lower() > b["nombre"].lower()):
                    lista[j] = b
                    lista[j + 1] = a
                    intercambios = intercambios + 1
        print("Categoria  Jugadores")
        cat_actual = 0
        linea = ""
        for jugador in lista:
            if jugador["categoria"] != cat_actual:
                if linea != "":
                    print(linea)
                cat_actual = jugador["categoria"]
                linea = str(cat_actual) + "ª         " + jugador["nombre"]
            else:
                linea = linea + ", " + jugador["nombre"]
        if linea != "":
            print(linea)
        print("Burbuja:", comparaciones, "comparaciones y", intercambios, "intercambios")

    elif opcion == 8:
        arch = open("inscriptos.json", "r")
        jugadores = json.load(arch)
        arch.close()
        arch = open("parejas.json", "r")
        parejas = json.load(arch)
        arch.close()
        nombre_pareja = input("Nombre de la pareja: ").strip()
        j1 = input("Primer jugador: ").strip()
        j2 = input("Segundo jugador: ").strip()
        inscripto1 = False
        inscripto2 = False
        for jugador in jugadores:
            if jugador["nombre"].strip().lower() == j1.lower():
                inscripto1 = True
            if jugador["nombre"].strip().lower() == j2.lower():
                inscripto2 = True
        repetida = False
        ocupado = False
        for pareja in parejas:
            if pareja["nombre"].strip().lower() == nombre_pareja.lower():
                repetida = True
            if pareja["jugador1"].strip().lower() == j1.lower() or pareja["jugador2"].strip().lower() == j1.lower():
                ocupado = True
            if pareja["jugador1"].strip().lower() == j2.lower() or pareja["jugador2"].strip().lower() == j2.lower():
                ocupado = True
        if inscripto1 == False or inscripto2 == False:
            print("Los dos jugadores tienen que estar inscriptos")
        elif j1.lower() == j2.lower():
            print("Tienen que ser dos jugadores distintos")
        elif repetida == True:
            print("Ya existe una pareja con ese nombre")
        elif ocupado == True:
            print("Alguno de los jugadores ya tiene pareja")
        else:
            parejas.append({"nombre": nombre_pareja, "jugador1": j1, "jugador2": j2, "puntos": 0})
            arch = open("parejas.json", "w")
            json.dump(parejas, arch, indent=4)
            arch.close()
            print("Pareja guardada")

    elif opcion == 9:
        arch = open("parejas.json", "r")
        parejas = json.load(arch)
        arch.close()
        if len(parejas) == 0:
            print("Todavia no hay parejas. Primero arme una con la opcion 8")
        else:
            print("Parejas:")
            for pareja in parejas:
                print("-", pareja["nombre"], "-", pareja["puntos"], "puntos")
            nom = input("Nombre de la pareja: ").strip()
            encontrado = False
            for pareja in parejas:
                if pareja["nombre"].strip().lower() == nom.lower():
                    puntos = int(input("Puntos que gano: "))
                    pareja["puntos"] = pareja["puntos"] + puntos
                    print(pareja["nombre"], "tiene", pareja["puntos"], "puntos")
                    encontrado = True
            if encontrado == True:
                arch = open("parejas.json", "w")
                json.dump(parejas, arch, indent=4)
                arch.close()
            else:
                print("Esa pareja no existe")

    elif opcion == 10:
        arch = open("parejas.json", "r")
        parejas = json.load(arch)
        arch.close()
        lista = parejas.copy()
        n = len(lista)
        for i in range(n - 1):
            mayor = i
            for j in range(i + 1, n):
                if lista[j]["puntos"] > lista[mayor]["puntos"]:
                    mayor = j
            if mayor != i:
                aux = lista[i]
                lista[i] = lista[mayor]
                lista[mayor] = aux
        print("Puesto  Pareja  Puntos")
        for i in range(n):
            print(i + 1, "-", lista[i]["nombre"], "-", lista[i]["puntos"])

    elif opcion != 0:
        print("Opcion incorrecta")
