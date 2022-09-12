#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  11 16:31:16 2020

@author: marilinaorihuela
"""
#%%
import os
import sys
from datetime import datetime

#%%
def procesar_nombre(name):
    '''Procesa el nombre de un archivo.
    Recibe el nombre por ejemplo: 'correlation_20200924.png'
    Devuelve una tupla con nombre y fecha 
    ejemplo: ('correlation.png', datetime.datetime(2020, 9, 24, 0, 0))'''
    
    new_name = name[:-13] + name[-4:]           #nombre
    fecha = name[-12:-4]                        #fecha
    date_object = datetime.strptime(fecha, '%Y%m%d')
    
    return (new_name, date_object)
    
#%%
def ordenar(argv):
    '''Recorre el directorio, reubica los archivos .png 
    y borra directorios vacios.
    Devuelve la cantidad de archivos reubicados.'''
         
    if len(argv)!= 3:
        raise SystemError(f'Uso inadecuado de {argv[0]} ' 'directorio de origen directorio destino')
    
    dir_origen = argv[1]
    dir_destino = argv[2]
    os.mkdir(argv[2])                               #creo el directorio destino
    procesados = 0
    
    for root, dirs, files in os.walk(dir_origen):
        for name in files: 
            if name[-3:] == 'png':                          #procesar si es png
             
                new_name, date_object = procesar_nombre(name)
                
                vieja_ruta = os.path.join(root, name)
                nueva_ruta = os.path.join(dir_destino, new_name)
                                                            #cambiar el timestamp
                os.utime(vieja_ruta,(date_object.timestamp(), date_object.timestamp()))
                
                os.rename(vieja_ruta, nueva_ruta)              #cambia de lugar
                procesados +=1
                
    for root, dirs, files in os.walk(dir_origen):
        for name in dirs:                                   #borra los directorios viejos 
    
            vieja_ruta = os.path.join(root, name)       #obtengo el directorio
            l = os.listdir(vieja_ruta)                  #listo los archivos
            if len(l)==0:                               #si esta vacia la borro
                os.rmdir(vieja_ruta)
                        
    return procesados

#%%
if __name__=='__main__':
    #'../data/ordenar' ''../data/imgs_procesadas/'
    a=ordenar(sys.argv)
    print(a)
