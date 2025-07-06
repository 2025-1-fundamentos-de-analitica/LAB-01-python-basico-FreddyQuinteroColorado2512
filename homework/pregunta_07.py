def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
        data = [line.strip().split('\t') for line in lines]

    resultado = {}
    for row in data:
        clave = int(row[1])   # columna 0 → número
        letra = row[0]        # columna 1 → letra

        if clave not in resultado:
            resultado[clave] = [letra]
        else:
            resultado[clave].append(letra)

    # Convertir el diccionario a lista de tuplas y ordenar por clave
    resultado_ordenado = sorted(resultado.items(), key=lambda x: x[0])

    return resultado_ordenado
