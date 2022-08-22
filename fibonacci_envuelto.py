#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:03:06 2021

@author: marilinaorihuela
"""
#%% Ejercicio 11.12: Envolviendo a Fibonacci


def fibonacci(n):
    """
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    """
    def fibonacci_aux(n, dict_fibo):
        """
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        """
        if n in dict_fibo.keys():
            F = dict_fibo[n]                #si ya esta en el diccionario
        else:
            F_2, dict_fibo_2 = fibonacci_aux(n-2, dict_fibo)        #para n-2
            F_1, dict_fibo = fibonacci_aux(n-1, dict_fibo_2)        #para n-1
            F = F_1 + F_2
            dict_fibo[n] =F
        return  F, dict_fibo
    
    dict_fibo = {0:0, 1:1} 
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F 
