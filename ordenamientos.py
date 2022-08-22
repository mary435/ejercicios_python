#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:56:43 2021

@author: marilinaorihuela
"""

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    
    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        print("DEBUG: ", lista)

    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

#%%
'''
lista = [0, 9, 3, 8, 5, 3, 2, 4]

ord_seleccion(lista)
DEBUG:  1 7 [0, 4, 3, 8, 5, 3, 2, 9] #max=9 queda en su lugar
DEBUG:  3 6 [0, 4, 3, 2, 5, 3, 8, 9] #max=8 lo inserta al final
DEBUG:  4 5 [0, 4, 3, 2, 3, 5, 8, 9] #max=5 lo inserta al final
DEBUG:  1 4 [0, 3, 3, 2, 4, 5, 8, 9] #max=4 lo inserta al final
DEBUG:  1 3 [0, 2, 3, 3, 4, 5, 8, 9] #max=3 lo inserta al final
DEBUG:  2 2 [0, 2, 3, 3, 4, 5, 8, 9] #max=3 lo inserta al final
DEBUG:  1 1 [0, 2, 3, 3, 4, 5, 8, 9] #max=2 queda
Out[714]: [0, 2, 3, 3, 4, 5, 8, 9]

ord_insercion(lista)
DEBUG:  [0, 9, 3, 8, 5, 3, 2, 4] #0>9 queda asi
DEBUG:  [0, 3, 9, 8, 5, 3, 2, 4] #9>3 cambian
DEBUG:  [0, 3, 8, 9, 5, 3, 2, 4] #9>8>3 cambian
DEBUG:  [0, 3, 5, 8, 9, 3, 2, 4] #9>8>5>3 cambian
DEBUG:  [0, 3, 3, 5, 8, 9, 2, 4] #9>8>5>3=3 cambian
DEBUG:  [0, 2, 3, 3, 5, 8, 9, 4] #9>8>5>3=3>2 cambian
DEBUG:  [0, 2, 3, 3, 4, 5, 8, 9] #9>8>5>4 cambian
Out[717]: [0, 2, 3, 3, 4, 5, 8, 9]


'''