#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:42:17 2021

@author: marilinaorihuela
"""
#%%
import numpy as np
from sklearn import linear_model

#%%
def pot(x,n):
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X,(x**(i+2)).reshape(-1,1)),axis=1)
    return X

#%%
def AIC(k, ecm, num_params):
    '''Calcula el AIC de una regresión lineal múltiple de 'num_params' 
    parámetros, ajustada sobre una muestra de 'k' elementos, y que da lugar a 
    un error cuadrático medio 'ecm'.'''
    
    aic = k * np.log(ecm) + 2 * num_params
    return aic

#%% Ejercicio 11.18: selección de modelos

def seleccion_modelos():

    np.random.seed(3141)                  # semilla para fijar la aleatoriedad
    N=50
    indep_vars = np.random.uniform(size = N, low = 0, high = 10)
    r = np.random.normal(size = N, loc = 0.0, scale = 8.0)          # residuos
    dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r    # relación cuadrática

    x = indep_vars
    xc = x**2
    y = dep_vars
    X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)
    X.shape

    aic_lista = []

    for n in range(8):
        X = pot(x, n + 1)                           #calculo la potencia
        lm = linear_model.LinearRegression()
        lm.fit(X, y)                                #ajusto el modelo
        errores = y - lm.predict(X)
        ecm = (errores**2).mean()                   #calculo del ecm
        aic = AIC(y.shape[0], ecm, n+1)             #calculo del aic
        aic_lista.append(aic)                       #lo agrego a una lista
        print('-------------------------')          #imprimo
        print(f'Grado del polinomio:{n}')
        print(f'Cantidad de parámetros:{n+1}')
        print(f'ECM: {ecm}')
        print(f'AIC: {aic}')
    
    minimo = np.argmin(aic_lista)+1                 #busco el aic minimo
   
    return minimo

if __name__ == '__main__':
    minimo = seleccion_modelos()
    print('--------------------------------------------------')
    print (f'Modelo selecionado de: {minimo} parámetros')
    