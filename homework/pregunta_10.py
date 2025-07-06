"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """

    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
        result = []

        for line in lines:
            parts = line.strip().split('\t')
            letter = parts[0]  # First column letter
            col4_count = len(parts[3].split(',')) if len(parts) > 3 else 0  # Length of column 4
            col5_count = len(parts[4].split(',')) if len(parts) > 4 else 0  # Length of column 5

            result.append((letter, col4_count, col5_count))
        print(result)
    return result
