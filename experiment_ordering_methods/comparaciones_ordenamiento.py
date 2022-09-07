#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 14:45:10 2021

@author: marilinaorihuela
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
def generar_lista(N):
    '''Genera una lista aleatoria de largo N con números enteros del 1 al 1000
    (puede haber repeticiones).'''
    
    lista = np.random.randint(1, 1000, N)
    return lista.tolist()
#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
       
    contador = 0   
    n = len(lista) - 1     # posición final del segmento a tratar

    while n > 0:    # mientras haya al menos 2 elementos para ordenar
        
        p = buscar_max(lista, 0, n)    # posición del mayor valor del segmento
        contador += n 
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        
        n = n - 1 # reducir el segmento en 1
    
    return contador

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
    contador = 0   
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
      
        if lista[i + 1] < lista[i]:
            v, cont = reubicar(lista, i + 1)
            contador +=cont

    return contador

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    contador = 0 
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        contador +=1 
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v
    return v, contador
    

#%%
def ord_burbujeo(lista):
    contador = 0  
    modif = 0                        #para controlar si no hubo modificaciones
    n = len(lista)
    #recorro la lista de 1 a n 
    for i in range(1,n):
        if i > 1 and modif ==0:     #controlo si no hay modificaciones corto
            break
        else:
            modif = 0 
            #Recorro los desordenados. n-i ya estan ordenados
            for j in range(0,n-i):
                contador +=1
                if(lista[j+1] < lista[j]):                         #comparo de a 2 
                    lista[j], lista[j+1] = lista[j+1], lista[j]   #los intercambio
                    modif = 1
              
    return contador  

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
def experimento(N, k):
    '''Repite k veces lo siguiente: generar una lista de largo N, ordenar la 
    lista con los tres métodos y guardar la cantidad de operaciones. 
    Al final, la función debe devolver el promedio de comparaciones realizadas 
    con cada método.'''
   
    seleccion = []
    insercion = []
    burbujeo = []
    
    #repito K veces cada ordenamiento y lo guardo en la lista
    for i in range(k):
        lista = generar_lista(N)
        seleccion.append(ord_seleccion(lista.copy()))
        insercion.append(ord_insercion(lista.copy()))
        burbujeo.append(ord_burbujeo(lista.copy()))
    
    #promedio de cada uno
    sel = sum(seleccion)/len(seleccion)
    ins = sum(insercion)/len(insercion)
    bur = sum(burbujeo)/len(burbujeo)
    
    return [sel, ins, bur]
    
    
def experimento_vectores(Nmax):
    '''Para N entre 1 y Nmax genera una lista de largo N con números enteros 
    del 1 al 1000 en orden aleatorio, calcula la cantidad de comparaciones 
    realizadas por cada método de ordenamiento y guarda estos resultados en 
    tres vectores de largo Nmax: comparaciones_seleccion, 
    comparaciones_insercion y comparaciones_burbujeo.'''
    
    seleccion = []
    insercion = []
    burbujeo = []
    merge_sort_l = []
    
    #Repito Nmax veces el experimento
    for N in range(1, Nmax):
        lista = generar_lista(N)                            #genero la lista
        seleccion.append(ord_seleccion(lista.copy()))       #ordeno y guardo el
        insercion.append(ord_insercion(lista.copy()))       # resultado para 
        burbujeo.append(ord_burbujeo(lista.copy()))         # cada metodo
        merge_sort_l.append(merge_sort(lista.copy())[1])
    
    #paso los contadores a array
    comparaciones_seleccion = np.array(seleccion)
    comparaciones_insercion = np.array(insercion)
    comparaciones_burbujeo = np.array(burbujeo)
    compraraciones_merge = np.array(merge_sort_l)

    #grafico
    plt.plot(comparaciones_seleccion, c = 'red', label = 'Selección',
             linestyle  = '--')
    plt.plot(comparaciones_insercion, c = 'green', label = 'Insercion',
             linestyle  = '--')
    plt.plot(comparaciones_burbujeo, c = 'blue', label = 'Burbujeo', 
             linestyle = ':')
    plt.plot(compraraciones_merge, c = 'orange', label = 'Merge Sort', 
             linestyle = '-.')
    
    plt.legend()
    plt.title(f'Experimento con {Nmax} Vectores')
    plt.show()
    
    
if __name__ == '__main__':
    experimento_vectores(10)    
    
    
'''Los metodos de insersion y burbujeo son los que mas dependen de la lista 
a ordenar. 
En cambio el metodo de seleccion depente del largo de la lista.
Pero entre los primeros 3 no hay diferencias significativas.
El metodo Merge Sort es mucho mas eficiente.
'''    
    
    
    
    
    
    
    