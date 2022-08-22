#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:18:53 2021

@author: marilinaorihuela
"""
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
#%% 
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

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

#%% Ejercicio 11.14: precio_alquiler ~ superficie

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(alquiler, superficie)

grilla_x = np.linspace(start = min(alquiler), stop = max(alquiler), num = 100)
grilla_y = grilla_x*a + b

x = alquiler
y = superficie
xc = x**2
ap, bp = ajuste_lineal_simple(xc, y)
grilla_y_p = (grilla_x**2)*ap + bp



plt.scatter(x,y)
plt.plot(grilla_x, grilla_y, c = 'green')
plt.plot(grilla_x, grilla_y_p, c = 'red')
plt.title('ajuste lineal con x^2')
plt.show()

'''
g = plt.scatter(x = alquiler, y = superficie)
plt.title('Precio Alquiler ~ Superficie')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('Alquiler')
plt.ylabel('Superficie')

plt.show()'''

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
#%% Scikit-Learn

x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4]) # mismos datos x, y
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
datosxy = pd.DataFrame({'x': x, 'y': y}) # paso los datos a un dataframe

ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(datosxy[['x']], datosxy['y']) # ajusto el modelo

grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
grilla_y = ajus.predict(grilla_x.reshape(-1,1))

datosxy.plot.scatter('x','y')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

#%%

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0]

data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})

X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)

ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)

errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio

ajuste_deptos.intercept_

ajuste_deptos.coef_

#%% Ejercicio 11.15: Peso específico

import requests
import io

enlace = 'https://raw.githubusercontent.com/python-unsam/Programacion_en_Python_UNSAM/master/Notas/11_Recursion/longitudes_y_pesos.csv'
r = requests.get(enlace).content
data_lyp = pd.read_csv(io.StringIO(r.decode('utf-8')))

ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(data_lyp [['longitud']], data_lyp['peso']) # ajusto el modelo
ajus.fit_intercept = False

grilla_x = np.linspace(start = min(data_lyp.longitud), stop = max(data_lyp.longitud), num = 50)
grilla_y = ajus.predict(grilla_x.reshape(-1,1))

data_lyp.plot.scatter('longitud','peso')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

errores = data_lyp.longitud - data_lyp.peso
print(errores)
print("ECM:", (errores**2).mean())
###
x = data_lyp.longitud
y = data_lyp.peso
xc = x**2
ap, bp = ajuste_lineal_simple(xc, y)
grilla_y_p = grilla_x + (grilla_x**2) *ap + bp
plt.scatter(x,y)
plt.plot(grilla_x, grilla_y, c = 'green')
plt.plot(grilla_x, grilla_y_p, c = 'red')
plt.title('ajuste lineal con x^2')
plt.show()

####


#%% Ejercicio 11.16: Modelo cuadrático

np.random.seed(3141) # semilla para fijar la aleatoriedad
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática

x = indep_vars
xc = x**2
y = dep_vars
X = np.concatenate((x.reshape(-1,1),xc.reshape(-1,1)),axis=1)
X.shape
#%%

ajuste_lineal = linear_model.LinearRegression()
ajuste_lineal.fit(x.reshape(-1,1), y)

ajuste_lineal_xc = linear_model.LinearRegression()
ajuste_lineal.fit(xc.reshape(-1,1), y)

ajuste_multiple = linear_model.LinearRegression()
ajuste_multiple.fit(X, y)

grilla_x = np.linspace(start = 0, stop = 10, num = 1000)
grilla_ajuste_lineal = ajuste_lineal.predict(grilla_x.reshape(-1,1))
grilla_ajuste_lineal_xc = ajuste_lineal_xc.predict((grilla_x**2).reshape(-1,1))
grilla_doble = np.concatenate(grilla_x.reshape(-1,1), (grilla_x**2).reshape(-1,1))

plt.scatter(indep_vars, dep_vars)
plt.plot(grilla_x, grilla_ajuste_lineal, c = 'green', label = 'Ajuste lineal')
plt.plot(grilla_x, grilla_ajuste_lineal_xc, c = 'blue', label = 'Ajuste cuadratico' )
plt.plot(grilla_x, ajuste_multiple, c = 'red', label = 'Ajuste multiple')
plt.legend()
plt.title('Ajustes: x, x^2, (x, x^2)')
plt.show()#%%


#%%11.17

aic_lista = []

for n in range(8):
    X = pot(x, n + 1)
    lm = linear_model.LinearRegression()
    lm.fit(X, y) 
    errores = y - lm.predict(X)
    ecm = (errores**2).mean()
    aic = AIC(y.shape[0], ecm, n+1)  
    aic_lista.append(aic)
    print('-------------------------')
    print(f'Grado del polinomio:{n}')
    print(f'Cantidad de parámetros:{n+1}')
    print(f'ECM: {ecm}')
    print(f'AIC: {aic}')
    
minimo = np.argmin(aic_lista)+1

