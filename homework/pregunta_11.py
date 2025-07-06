def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
        data = [line.strip().split('\t') for line in lines]

    resultado = {}

    for row in data:
        valor = int(row[1])         # columna 2 (entero)
        letras = row[3].split(',')  # columna 4 (letras separadas por coma)

        for letra in letras:
            if letra not in resultado:
                resultado[letra] = valor
            else:
                resultado[letra] += valor

    # Ordenar el diccionario por clave (letra)
    return dict(sorted(resultado.items()))
