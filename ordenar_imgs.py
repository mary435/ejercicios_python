#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:06:34 2021

@author: marilinaorihuela
"""
#%% Ejercicio 8.6: Ordenar el árbol de archivos (optativo)
import sys
import os
from datetime import datetime
import shutil

#%%
def procesar_nombre(fname):
    'Toma el nombre de un archivo y devuelva la fecha y el nombre corregido'
    'Pre: recibe el nombre o la ruta al archivo nombrado Nombre_YYYYmmdd.png'
    'Pos: devuelve el nuevo nombre del archivo y la fecha'
    
    head_tail = os.path.split(fname)    #divide la ruta del nombre 
    file_name = head_tail[1]            #me quedo con el nombre
    
    file_extension = os.path.splitext(file_name) #divido nombre de extension
    extension = file_extension[1]                #guardo la extension
    nombre_fecha = file_extension[0]             #nobre_fecha
        
    name = nombre_fecha[:-9] + extension       #saco 9 caracteres de:_YYYYmmdd    
    
    fecha = nombre_fecha[-8:]                    #8 caracteres de:YYYYmmdd       
    fecha_date = datetime.strptime(fecha, '%Y%m%d') #fecha de str a datetime
    ts_fecha = fecha_date.timestamp()           #fecha de datetime a timestamp 

    os.utime(fname, (ts_fecha, ts_fecha))        #cambio la fecha del archivo
    
    dir_destino = sys.argv[2]                   #tomo la direccion de destino
    destino = os.path.join(dir_destino, name)   #la uno con el nombre nuevo
    
    os.rename(fname, destino)                   #renombro el archivo   
      
    return (name, fecha_date)

#%%
def borrar_dir_vacios(dir_original):
    'Recorre el directorio y borra carpetas vacias'
    'Pre: recibe el directorio a recorrer'
    'Pos: devuelve un int con la cantidad de carpetas borradas'
    
    contador = 0
    for root, dirs, files in os.walk(dir_original, topdown=False):
        for name in dirs:
            path = os.path.join(root, name)       #recorro los directorios
            if not os.listdir(path) or os.listdir(path)==['.DS_Store']:
                shutil.rmtree(path)    #los borro si estan vacios
                contador  += 1
    return contador
             
#%%
def procesar(fname):
    'Procesa cada archivo del directorio con la función procesar_nombre(fname)'
    'Pre: recibe un directorio origen y uno destino por argv'
    'Pos: se borran las carpetas vacias del directorio original y las imagenes'
    ' procesadas quedan en el directorio de destino'
    
    if len(sys.argv) != 3:           
        raise SystemExit(f'Uso adecuado:{sys.argv[0]}' ' directorio_original'
                         ' directorio_destino')    
    dir_original = sys.argv[1]    
    dir_destino = sys.argv[2]    

    try:
        os.mkdir(dir_destino)   #creo el directorio de destino
    except FileExistsError:     #si ya existe no muestro el error
        pass
    
    contar_archivos = 0    
    for root, dirs, files in os.walk(dir_original):     
        for name in files:              #recorro los archivos
            if '.png' in name:          #filtro los archivos con .png  #Probar: string.endswith('.png')
                                        #proceso el archivo
                nombre, fecha = procesar_nombre(os.path.join(root, name))  
                contar_archivos += 1
    contar_directorios = borrar_dir_vacios(dir_original)
    print(f'Se procesaron {contar_archivos} archivos.')
    print(f'Se borraron {contar_directorios} directorios.')
    
#%%

if __name__ == '__main__':
    procesar(sys.argv)
