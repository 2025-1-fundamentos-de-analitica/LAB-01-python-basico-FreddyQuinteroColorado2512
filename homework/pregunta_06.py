"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines() 
        data = [line.strip().split('\t') for line in lines]

    result = {}
    for row in data:
        values = row[4].split(',')
        for value in values:
            if ':' in value:
                key, val = value.split(':')
                val = int(val)
                if key not in result:
                    result[key] = [val, val]
                else:
                    result[key][0] = min(result[key][0], val)
                    result[key][1] = max(result[key][1], val)
    # Convertir el diccionario a una lista de tuplas con formato (clave, min_val, max_val)
    result = [(key, min_val, max_val) for key, (min_val, max_val) in result.items()]

    # Ordenar por clave
    result.sort(key=lambda x: x[0])
    return result
