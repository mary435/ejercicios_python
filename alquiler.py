#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 18:16:18 2021

@author: marilinaorihuela
"""
#%% Ejercicio 11.14: precio_alquiler ~ superficie

import numpy as np
import matplotlib.pyplot as plt

#%%

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

#%%

superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(alquiler, superficie)

grilla_x = np.linspace(start = min(alquiler), stop = max(alquiler), num = 100)
grilla_y = grilla_x*a + b

g = plt.scatter(x = alquiler, y = superficie)
plt.title('Precio Alquiler ~ Superficie')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('Alquiler')
plt.ylabel('Superficie')

plt.show()

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
