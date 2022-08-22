#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 12:45:04 2021

@author: marilinaorihuela
"""
#%%
from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

#%%

def graficar():
    '''Repite el gráfico del apunte pero usando seaborn para graficar.'''
    
    iris_dataset = load_iris()

    # creamos un dataframe de los datos de flores
    # etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
    iris_dataframe = pd.DataFrame(iris_dataset['data'], 
                              columns = iris_dataset.feature_names)
    
    # agregamos el atributo target para setear las especies 
    iris_dataframe['target'] = iris_dataset['target']
    
    # y hacemos una matriz de gráficos de dispersión
    g =sns.pairplot(iris_dataframe, hue = 'target', diag_kind="hist", 
                    palette='deep')
    
    g._legend.remove()                     #no muestro la leyenda, asi es igual
    
if __name__ == '__main__':
    graficar()