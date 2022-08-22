#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:57:46 2021

@author: marilinaorihuela
"""
#%%

from vigilante import vigilar
import csv
import informe_final
from formato_tabla import crear_formateador

#%% Ejercicio Ejercicio 10.15: Código simple
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    
    #elegir columnas
    indices = [0, 1, 2]
    rows = ((row[index] for index in indices) for row in rows)
    
    #cambiar tipos
    types = [str, float, int]
    rows = ((func(val) for func, val in zip(types, row)) for row in rows)
    
    #hacer diccionario
    headers = ['nombre', 'precio', 'volumen']
    rows = (dict(zip(headers, row)) for row in rows )
    return rows
            
#%% Ejercicio 10.12: El pipeline ensamblado       
     
def ticker(camion_file, log_file, fmt): 
    
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Cajones', 'Precio'])
    
    camion = informe_final.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    #filtrar datos
    filas = (fila for fila in filas if fila['nombre'] in camion)

    for fila in filas:
        rowdata = [fila['nombre'], str(fila['precio']), str(fila['volumen'])]
        formateador.fila(rowdata)

#%%
if __name__ == '__main__':
    
    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    #filtrar datos
    rows =  (row for row in rows if row['nombre'] in camion)
    for row in rows:
        print(row)
        
        
        
