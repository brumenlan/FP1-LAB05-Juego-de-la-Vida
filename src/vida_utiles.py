import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    return [[False for _ in range(columnas)] for _ in range(filas)]

'''
    fila_f = []
    tablero = []
    for c in range(columnas):
        fila_f.append(False)
    for f in range(filas):
        tablero.append(fila_f)
    return tablero'''

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    fila_f = []
    tablero = []

    for c in range(columnas):
        if random.random() < probabilidad_vida:
            fila_f.append(True)
        else:
            fila_f.append(False)
    for f in range(filas):
        tablero.append(fila_f)
    return tablero

def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """
    filas_tablero = len(tablero)
    columnas_tablero = len(tablero[0])
    filas_patron = len(patron)
    columnas_patron = len(patron[0])

    for i in range(filas_patron):
        for j in range(columnas_patron):
            fila_destino = pos_fila + i
            col_destino = pos_col + j

            # Evitar escribir fuera del tablero
            if 0 <= fila_destino < filas_tablero and 0 <= col_destino < columnas_tablero:
                tablero[fila_destino][col_destino] = patron[i][j]

def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """
    # TODO: Ejercicio 4
    pass

def calcular_siguiente_generacion(tablero):
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    # TODO: Ejercicio 5
    pass
