#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:10:18 2021

@author: marilinaorihuela
"""

#%% Ejercicio 11.9: Pascal

def pascal(n, k):
    'Devuelve el valor de pascal para fila n y columna k'
    
    if k == 0 or k == n:            #caso base: inicio y bordes
        res = 1
    else:                           
        res = pascal(n - 1, k - 1) + pascal (n - 1, k)  #caso recursivo: 
                                                        #suma los superiores
    return res






