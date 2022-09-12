#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 15:08:41 2021

@author: marilinaorihuela
"""
#%%
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt

#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
        
    n = len(lista) - 1     # posición final del segmento a tratar
    while n > 0:    # mientras haya al menos 2 elementos para ordenar
        
        p = buscar_max(lista, 0, n)    # posición del mayor valor del segmento

        lista[p], lista[n] = lista[n], lista[p] # intercambiar el valor de p con
                                                # la última posición del segmento
        n = n - 1 # reducir el segmento en 1
    
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
def ord_burbujeo(lista):
    '''Ordena una lista de elementos según el método de burbujeo.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada.'''
    n = len(lista)
    modif = 0 
    #recorro la lista de 1 a n 
    for i in range(1,n):      
        if i > 1 and modif ==0:       #controlo si no hay modificaciones corto
            break
        else:
        #Recorro los desordenados. n-i ya estan ordenados
            for j in range(0,n-i): 
                if(lista[j+1] < lista[j]):                     #comparo de a 2  
                    lista[j], lista[j+1] = lista[j+1], lista[j]   #los intercambio
                    modif = 1
    return lista                                   
#%%

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    contador = 0   
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, cont_izq = merge_sort(lista[:medio])
        der, cont_der = merge_sort(lista[medio:])
        lista_nueva, cont_comp = merge(izq, der)
        contador += cont_comp + cont_izq + cont_der
    return lista_nueva, contador

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    contador = 0
    
    while(i < len(lista1) and j < len(lista2)):
        contador +=1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, contador

           
#%%
def generar_lista(N):
    '''Genera una lista aleatoria de largo N con números enteros del 1 al 1000
    (puede haber repeticiones).'''
    
    lista = np.random.randint(1, 1000, N)
    return lista.tolist()
#%%
def generar_listas(Nmax):
   '''Genera una lista de listas, una de cada longitud entre 1 y Nmax, 
   con valores aleatorios entre 1 y 1000.''' 

   return [generar_lista(n) for n in range(1,Nmax)]

#%%
def experimento_timeit(Nmax):
    '''Para N entre 1 y Nmax genera una lista de largo N con números enteros 
    del 1 al 1000 en orden aleatorio, calcula el tiempo que tarda cada método 
    en ordenar la lista y guarda estos resultados en tres vectores de largo 
    Nmax para graficarlos'''
    
    listas = generar_listas(Nmax)    
    global lista
        
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_merge = []

    for lista in listas:
        
        # evalúo cada método en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', 
                                     number = Nmax, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())',
                                     number = Nmax, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', 
                                    number = Nmax, globals = globals())
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', 
                                    number = Nmax, globals = globals())
        
        # guardo los resultados
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_merge.append(tiempo_merge)
    
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    tiempos_merge = np.array(tiempos_merge)
    
    
    plt.plot(tiempos_seleccion, label = 'Selección')
    plt.plot(tiempos_insercion, label = 'Insercion')
    plt.plot(tiempos_burbujeo, label = 'Burbujeo')
    plt.plot(tiempos_merge, label = 'Merge Sort')
    plt.title('Comparacion de metodos de ordenamiento')
    plt.xlabel('Largo de los vectores')
    plt.ylabel('Tiempo')
    plt.legend()
    plt.show()

    
if __name__ == '__main__':
    experimento_timeit(10)

