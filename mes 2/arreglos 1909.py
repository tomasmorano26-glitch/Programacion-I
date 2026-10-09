def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota

    promedio = suma / len(notas)

    return promedio


def es_regular(alumno):
    promedio = calcular_promedio(alumno["notas"])

    if promedio >= 6 and alumno["asistencia"] > 60:
        return True
    else:
        return False


def mostrar_alumnos(alumnos):
    for alumno in alumnos:

        promedio = calcular_promedio(alumno["notas"])

        print("Nombre:", alumno["nombre"])
        print("Promedio:", promedio)
        print("Asistencia:", alumno["asistencia"], "%")

        if es_regular(alumno):
            print("Estado: REGULAR")
        else:
            print("Estado: NO REGULAR")

        print("------------------------")


alumnos = [
    {"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90},
    {"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60},
    {"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95},
    {"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85}
]


mostrar_alumnos(alumnos)