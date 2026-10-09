import os

def mostrar_menu():
    print("---- SISTEMA DEL BUFFET ----\n")
    print("1. Cargar nuevo producto al catalogo")
    print("2. Registrar venta")
    print("3. Ver catalogo")
    print("4. Ver informes semanales")
    print("5. Guardar y salir\n")

def cargar_producto(catalogo, ventas):
    print("\n---- SISTEMA DEL BUFFET ----")
    print("- Cargar producto -\n")
    codigo_producto = int(input("Ingrese el codigo del producto: "))
    existe = False
    for i in range(len(catalogo)):
        if catalogo[i]["codigo"] == codigo_producto:
            existe = True
            break

    if existe:
        print("Error: codigo de producto ya existente")
    else:
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        catalogo.append({
            "codigo": codigo_producto,
            "nombre": nombre_producto,
            "precio": precio_producto,
        })
        ventas.append([0, 0, 0, 0, 0])
        print("\nProducto registrado con exito")

def registrar_venta(ventas, catalogo):
    print("\n---- SISTEMA DEL BUFFET ----")
    print("- Registrar venta -\n")
    correcto = True
    existe = False
    dia_venta = int(input("Ingrese el dia de la venta (1=Lunes a 5=Viernes): "))
    if dia_venta >= 1 and dia_venta <= 5:
        codigo_producto = int(input("Ingresar el codigo del producto: "))
        for i in range(len(catalogo)):
            if catalogo[i]["codigo"] == codigo_producto:
                indice = i
                existe = True
                break
        if existe:
            cantidad_vendida = int(input("Ingresar la cantidad vendida: "))
            if cantidad_vendida <= 0:
                print("Error: cantidad no valida")
                correcto = False
        else:
            print("Error: producto no existente en catalogo")
            correcto = False
    else:
        print("Error: dia no valido")
        correcto = False

    if correcto:
        ventas[indice][dia_venta - 1] += cantidad_vendida
        print("\nVenta registrada con exito")

def mostrar_catalogo(catalogo):
    print("\n---- SISTEMA DEL BUFFET ----")
    print("- Catalogo -\n")
    print(f"{'CODIGO':<10} {'PRODUCTO':<25} {'PRECIO':<10}")
    print("-" * 45)
    for prod in catalogo:
        print(f"{prod['codigo']:<10} {prod['nombre']:<25} ${prod['precio']:<10.2f}")
    print("-" * 45)

def calcular_total_unidades(ventas, fila_prod):
    total = 0
    for i in range(5):
        total += ventas[fila_prod][i]
    return total

def calcular_recaudacion_dia(ventas, catalogo, dia):
    total = 0
    for i in range(len(catalogo)):
        total += ventas[i][dia] * catalogo[i]["precio"]
    return total

def producto_mas_vendido(ventas, catalogo):
    mayor_venta = -1
    indice_producto = 0
    for i in range(len(catalogo)):
        total_actual = calcular_total_unidades(ventas, i)
        if total_actual > mayor_venta:
            mayor_venta = total_actual
            indice_producto = i
    return catalogo[indice_producto]["nombre"], mayor_venta

def dia_mayor_recaudacion(ventas, catalogo):
    mayor_venta = -1
    indice_dia = 0
    for i in range(5):
        total_actual = calcular_recaudacion_dia(ventas, catalogo, i)
        if total_actual > mayor_venta:
            mayor_venta = total_actual
            indice_dia = i
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    dia = dias[indice_dia]
    return dia, mayor_venta

def obtener_productos_sin_ventas(ventas, catalogo):
    sin_ventas = []
    for i in range(len(catalogo)):
        if calcular_total_unidades(ventas, i) == 0:
            sin_ventas.append(catalogo[i]["nombre"])
    return sin_ventas

def calcular_recaudacion_total_semana(ventas, catalogo):
    total_semana = 0
    for dia in range(5):
        total_semana += calcular_recaudacion_dia(ventas, catalogo, dia)
    return total_semana

def cargar_datos():
    catalogo = []
    ventas = []
    if os.path.exists("productos.txt"):
        archivo = open("productos.txt", "r")
        for linea in archivo:
            datos = linea.strip().split(";")
            catalogo.append({
                "codigo": int(datos[0]),
                "nombre": datos[1],
                "precio": float(datos[2]),
            })
        archivo.close()
    if os.path.exists("ventas.txt"):
        archivo = open("ventas.txt", "r")
        for linea in archivo:
            datos = linea.strip().split(";")
            fila = []
            for i in range(5):
                fila.append(int(datos[i]))
            ventas.append(fila)
        archivo.close()
    while len(ventas) < len(catalogo):
        ventas.append([0, 0, 0, 0, 0])
    return catalogo, ventas

def guardar_datos(catalogo, ventas):
    archivo = open("productos.txt", "w")
    for prod in catalogo:
        archivo.write(f"{prod['codigo']};{prod['nombre']};{prod['precio']}\n")
    archivo.close()
    archivo = open("ventas.txt", "w")
    for fila in ventas:
        archivo.write(f"{fila[0]};{fila[1]};{fila[2]};{fila[3]};{fila[4]}\n")
    archivo.close()

def mostrar_informes(ventas, catalogo):
    print("\n---- SISTEMA DEL BUFFET ----")
    print("- Informes semanales -\n")
    total_semana = calcular_recaudacion_total_semana(ventas, catalogo)
    if len(catalogo) == 0:
        print("No hay productos cargados")
    elif total_semana == 0:
        print("Todavia no hay ventas registradas esta semana")
    else:
        dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

        print("Unidades vendidas por producto:")
        for i in range(len(catalogo)):
            print(f"  {catalogo[i]['nombre']:<25} {calcular_total_unidades(ventas, i)}")

        print("\nRecaudacion por dia:")
        for d in range(5):
            print(f"  {dias[d]:<12} ${calcular_recaudacion_dia(ventas, catalogo, d):.2f}")

        nombre, unidades = producto_mas_vendido(ventas, catalogo)
        print(f"\nProducto mas vendido: {nombre} ({unidades} unidades)")
        for i in range(len(catalogo)):
            if calcular_total_unidades(ventas, i) == unidades and catalogo[i]["nombre"] != nombre:
                print(f"Empata con: {catalogo[i]['nombre']} ({unidades} unidades)")

        dia, recaudacion = dia_mayor_recaudacion(ventas, catalogo)
        print(f"\nDia de mayor recaudacion: {dia} (${recaudacion:.2f})")
        for d in range(5):
            if calcular_recaudacion_dia(ventas, catalogo, d) == recaudacion and dias[d] != dia:
                print(f"Empata con: {dias[d]} (${recaudacion:.2f})")

        sin_ventas = obtener_productos_sin_ventas(ventas, catalogo)
        print("\nProductos sin ventas:")
        if len(sin_ventas) == 0:
            print("  Todos los productos tuvieron ventas")
        else:
            for nombre_prod in sin_ventas:
                print(f"  {nombre_prod}")

        print(f"\nRecaudacion total de la semana: ${total_semana:.2f}\n")

catalogo, ventas = cargar_datos()
if len(catalogo) == 0:
    print("No hay datos guardados, se empieza una semana nueva\n")

opcion = 0
while opcion != 5:
    mostrar_menu()
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        cargar_producto(catalogo, ventas)
        guardar_datos(catalogo, ventas)
    elif opcion == 2:
        registrar_venta(ventas, catalogo)
        guardar_datos(catalogo, ventas)
    elif opcion == 3:
        mostrar_catalogo(catalogo)
    elif opcion == 4:
        mostrar_informes(ventas, catalogo)
    elif opcion == 5:
        guardar_datos(catalogo, ventas)
        print("Datos guardados. Hasta mañana!")
    else:
        print("Opcion no valida\n")