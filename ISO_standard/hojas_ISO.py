#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:57:05 2021

@author: marilinaorihuela
"""
#%% Ejercicio 11.13: Hojas ISO y recursión

def medidas_hoja_A(N):
    '''Para una entrada N mayor que cero, devuelva el ancho y el largo de 
        la hoja A(N) calculada recursivamente a partir de las medidas de 
        la hoja A(N−1), usando la hoja A0 como caso base. La función debe 
        devolver el ancho y el largo -en ese orden- en una tupla..'''
    
    if N == 0:
        res = 841, 1189                              #caso base: A0
    else:
        ancho, largo = medidas_hoja_A(N-1)           #caso recursivo:
        res = largo//2, ancho                      #cambio ancho por largo 
                                                       # y largo/2 por ancho
    return res