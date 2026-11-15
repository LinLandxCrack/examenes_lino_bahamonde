import random


def generar_lista(n):
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("La cantidad 'n' debe ser un número entero positivo.")

    lista = []
    for _ in range(n):
        lista.append(random.randint(1, 100))
    return lista

def eliminar_duplicados(lista):
    vistos = set()
    sin_repetidos = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            sin_repetidos.append(elemento)
    return sin_repetidos

def ordenar_listas(lista):
    ascendente = sorted(lista)
    descendente = sorted(lista, reverse=True)
    return ascendente, descendente

def mayor_par(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)

    if len(pares) > 0:
        return max(pares)
    else:
        print("Aviso: No existen números pares en la lista.")
        return None

def obtener_elemento(lista, posicion):
    try:
        return lista[posicion]
    except IndexError:
        print("Error de índice: La posición {} está fuera del rango de la lista.".format(posicion))
        return None
    except TypeError:
        print("Error de tipo: La posición debe ser un número entero.")
        return None