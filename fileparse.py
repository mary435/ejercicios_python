#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: marilinaorihuela

Parsear un archivo CSV
"""
#%%
import csv

def parse_csv(file, select = None, types = None, has_headers = True, 
              silence_errors = False):
    '''Parsea un archivo CSV en una lista de registros.
    Pre: recibe un iterable.
    Opcionales:
        -select: nombres de columnas que se desea seleccionar
        -types: convertir el tipo de datos recuperados antes de devolverlos.
        -has_headers: si tiene encabezados genera diccionario, sino tuplas.
        -silence_errors = True: muestra los errores.
    Pos: diccionario o tupla de datos'''
    
    filas = csv.reader(file)
    
    indices = []
    #Filtrar error:se indica que no hay encabezados, pero se envian los nombres
    if has_headers == False and select!=None :
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    
    #Filtrar si hay encabezados    
    if has_headers:                                                    
        encabezados = next(filas)         
        
        #Filtrar si se indicó un selector de columnas 
        if select:    
            indices = [encabezados.index(nombre_columna) for nombre_columna 
                       in select]
            encabezados = select    #Se achica el conjunto de encabezados
                        
    registros = []
    for i,fila in enumerate(filas, start=1):

        if not fila:    #Saltear filas vacías
            continue
            
        if indices:    # Filtrar si se especificaron columnas
            fila = [fila[index] for index in indices]
           
        if types:    # Filtrar si se especificaron tipos
            try:
                fila = [func(val) for func, val in zip(types, fila)]
            except ValueError as e:
                # Si hay algun valor faltante salteo esa linea
                if silence_errors==False:    
                    print (f'Fila {i}: No pude convertir {fila}')
                    print(f'Fila {i}: Motivo: {e}')       
                continue
                
        if has_headers:    #Filtrar si hay encabezados 
            #Armar diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
        else:
            #Armar tupla
            registros.append(fila)

    return registros




