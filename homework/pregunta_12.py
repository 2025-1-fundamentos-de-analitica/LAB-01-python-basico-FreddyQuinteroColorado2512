def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
        data = [line.strip().split('\t') for line in lines]

    resultado = {}

    for row in data:
        letra = row[0]            # Columna 1 (índice 0)
        columna5 = row[4]         # Columna 5 (índice 4)
        pares = columna5.split(',')

        suma_valores = 0
        for par in pares:
            if ':' in par:
                _, valor = par.split(':')
                suma_valores += int(valor)

        if letra not in resultado:
            resultado[letra] = suma_valores
        else:
            resultado[letra] += suma_valores

    # Ordenar el diccionario por clave (letra)
    return dict(sorted(resultado.items()))
