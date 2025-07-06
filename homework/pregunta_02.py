"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """

    with open('files/input/data.csv', 'r') as file:
        data = file.readlines()

    # Contar registros por letra
    counts = {}
    for line in data:
        letter = line[0].upper()  # Convertir a mayúscula para uniformidad
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    # Convertir el diccionario a una lista de tuplas y ordenar alfabéticamente
    result = sorted(counts.items())

    return result
