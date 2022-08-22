#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:28:05 2021

@author: marilinaorihuela
"""
#%% Ejercicio 11.2: Números triangulares

def triangular(n):
    '''calcule recursivamente el n-ésimo número triangular'''
    if n == 0:
        res = 0
    else:
        res = n + triangular(n-1)
    return res

#%% Ejercicio 11.3: Dígitos

def cant_digitos(n):
    '''reciba un número positivo, n, y devuelva la cantidad de dígitos que tiene'''
    if n <10:
        res = 1
    else:
        res = 1 + cant_digitos(n/10)
    return res
        
#%%Ejercicio 11.4: Potencias

def es_potencia(n, b):
    '''reciba 2 enteros, n y b, y devuelva True si n es potencia de b y False en caso contrario.'''
    
    if n == b:
        return 0
    elif b > n:
        return 1
    elif n > b:
        res = es_potencia(n, b*b)
    if res == 0 :
        return True
    if res == 1:
        return False

#%% version del profe
'''
    if n ==1:
        return True
    if b ==1:
        return False
    if n%b ==0:
        return es_potencia(n//b,b)
    else:
        return False
'''

#%% Ejercicio 11.5: Subcadenas

def posiciones_de(a, b):
    '''reciba como parámetros dos cadenas y devuelva una lista con las 
    posiciones en donde se encuentra b dentro de a'''
    
    def posiciones(a, b):
        if b in a:
            return a.find(b)
        else:
            return 888888888
     
    res = []
    indice=0
    #c = a[indice:]
    while b in a[indice:]:
    
        ubicacion = posiciones(a[indice:], b)
        if not ubicacion == 888888888:
            indice += ubicacion
            res.append(indice)
            indice += len(b)
    return res


'''solucion del profe
if len(b)>len(a):
    return []
return pociciones_de(a[:-1],b + a[-len(b):==b]*[len(a)-len(b)])


'''

#%% Ejercicio 11.6: Paridad

def par(n):
    
    if n % 2 == 0:
        res = True
    else:
        res = False
    return res
    

def impar(n):
    
    if n == 1:
        res = True
    elif n > 1:
        res = par(n-1)
    return res

#%% Ejercicio 11.7: Máximo

def maximo(lista):
    if len(lista) == 1:
        res = lista[0]
    else:
        primero = lista[0]
        max_del_resto = maximo(lista[1:])
        if max_del_resto > primero:
            res = max_del_resto
        else:
            res = primero
    return res
                          
#%% Ejercicio 11.8: Replicar

def replicar(lista, n):
    
    if len(lista)==0:
        res = []
    elif len(lista)==1:
        res = [lista]
    else:
        res = []
        for i, elem in enumerate(lista):
            replicar (lista[:i]+lista[i+1:],n)
            res += [elem for i in range(n)]
            
    return res

#%% Ejercicio 11.10: Combinatorios

def combinaciones(lista, k):
    
    if len(lista)==0:
        res = []
    elif len(lista)==1:
        res = [lista]
    else:
        res = []
        for i, elem in enumerate(lista):
            combinaciones (lista[:i]+lista[i+1:],k)
            res += [elem + i for i in lista]
            
    return res
    

#%% Solucion del profe
'''    if k==1:
        comb = lista
    
    else:
        comb_rec = combinaciones (lista,k-1)
        comb = [e+c for e in lista for c in comb_rec]
        return comb

'''






            
            
                          
                          
                          
                          
                         






















        
