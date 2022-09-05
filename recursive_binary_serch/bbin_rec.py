#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 15:47:51 2021

@author: marilinaorihuela
"""
#%% Ejercicio 11.11: Búsqueda binaria 

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        
        if lista[medio] > e:                    
            res = bbinaria_rec(lista[:medio], e)    #descarto la mitad derecha
        else:                                   
            res = bbinaria_rec(lista[medio:], e)  #descarto la mitad izquierda
    
    return res
