# =============================================
#  TORNEO DE PÁDEL - Actividad 01
#  Carga de jugadores y armado de parejas
# =============================================

# ----- a) Ingreso de jugadores -----

cantidad = int(input("¿Cuántos jugadores van a participar en el torneo? "))

# Inicializo los vectores (uno para cada dato del jugador)
nombres = [""] * cantidad
categorias = [""] * cantidad

# Cargo los datos por teclado
for i in range(cantidad):
    print()
    print("Jugador", i + 1)
    nombres[i] = input("Nombre: ")
    categorias[i] = input("Categoría (4ª, 5ª, 6ª...): ")

# Recorro los vectores para mostrar los jugadores
print()
print("LISTA DE JUGADORES")
for i in range(cantidad):
    print(i + 1, "-", nombres[i], "- Categoría:", categorias[i])


# ----- b) Armado de parejas -----

print()
cant_parejas = int(input("¿Cuántas parejas se van a formar? "))
while cant_parejas > cantidad // 2:
    print("No alcanzan los jugadores. Como máximo se pueden formar", cantidad // 2, "parejas.")
    cant_parejas = int(input("¿Cuántas parejas se van a formar? "))

# Inicializo los vectores de las parejas
nombres_parejas = [""] * cant_parejas
jugador1 = [""] * cant_parejas
jugador2 = [""] * cant_parejas

# Este vector sirve para saber si un jugador ya tiene pareja (True) o no (False)
tiene_pareja = [False] * cantidad

for i in range(cant_parejas):
    print()
    print("Pareja", i + 1)
    nombres_parejas[i] = input("Nombre de la pareja: ")

    # Primer jugador (se elige por el número que aparece en la lista)
    num = int(input("Número del primer jugador: "))
    while tiene_pareja[num - 1] == True:
        print("Ese jugador ya tiene pareja, elegí otro.")
        num = int(input("Número del primer jugador: "))
    jugador1[i] = nombres[num - 1]
    tiene_pareja[num - 1] = True

    # Segundo jugador
    num = int(input("Número del segundo jugador: "))
    while tiene_pareja[num - 1] == True:
        print("Ese jugador ya tiene pareja, elegí otro.")
        num = int(input("Número del segundo jugador: "))
    jugador2[i] = nombres[num - 1]
    tiene_pareja[num - 1] = True

# Recorro los vectores para mostrar las parejas
print()
print("PAREJAS DEL TORNEO")
for i in range(cant_parejas):
    print(nombres_parejas[i], ":", jugador1[i], "y", jugador2[i])