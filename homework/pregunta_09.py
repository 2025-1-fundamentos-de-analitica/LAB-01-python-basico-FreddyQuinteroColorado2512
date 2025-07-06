def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    """

    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    contador = {}

    for line in lines:
        parts = line.strip().split('\t')
        columna5 = parts[4]  # ejemplo: "aaa:1,bbb:2,ccc:3"
        pares = columna5.split(',')

        for par in pares:
            if ':' in par:
                clave, _ = par.split(':')
                if clave not in contador:
                    contador[clave] = 0
                contador[clave] += 1

    # Ordenar el diccionario por clave (opcional pero recomendable)
    return dict(sorted(contador.items()))
