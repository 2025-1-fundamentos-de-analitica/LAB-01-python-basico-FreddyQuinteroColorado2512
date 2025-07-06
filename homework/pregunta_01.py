"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
    
    total = 0

    for line in lines:  # Skip the header line
        parts = line.strip().split('\t')
        total += int(parts[1])
            
    
    print("Total=", total)  # Print the total for verification
    return total

