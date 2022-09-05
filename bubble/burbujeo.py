#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:59:43 2021

@author: marilinaorihuela
"""
#%% Ejercicio 12.2: burbujeo
   
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


'''
Esta funcion realiza n^2 comparaciones para una lista de largo n. 
Ya que recorre casi toda la lista, para cada elemento que ordena.
'''

#%%
def ord_burbujeo_recursivo(lista):
    
    def burbuja(lista):
        n = len(lista)-1
        for i in range(n):                                  #recorro la lista
            if lista[i] > lista[i+1]:                           #comparo
                lista[i], lista[i+1] = lista[i+1], lista[i]     #intercambio
        return lista
    
    if len(lista) == 1: #caso base
        return lista
    else:               #caso recursivo 
        n = len(lista)
        res =[]
        lista_c = burbuja(lista)   #ordena el ultimo elemento
        
        #me quedo con el elememnto ordenado y llamo recursivaente para el resto
        res = ord_burbujeo_recursivo(lista_c[:n-1]) + [lista_c[n-1]]
    
    return res    

            
   
        
        









     