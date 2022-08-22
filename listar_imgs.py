#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 17:06:10 2021

@author: marilinaorihuela
"""
#%% Ejercicio 8.5: Recorrer el árbol de archivos

import os
import sys

#%%
def archivos_png(directorio):
    'Lista todos los archivos .png que se encuentren en algún subdirectorio,'
    ' directorio dado.'
    'Pre: recibe el directorio.'
    'Pos: devuelve una lista donde cada elemento es un archivo.'
    
    if len(sys.argv) != 2:           
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio')
    
    directorio = sys.argv[1]
    
    archivos = ((root,name) for root, dirs, files in os.walk(directorio) for 
                name in files if '.png' in name) 
    return archivos
    
def modificar_archivos(lista_archivos):
    '''generador que, dada la secuencia filtrada (directorios y archivos png),
    genere ternas consistentes de: 
    ('viejo_dir/viejo_nombre', 'nuevo_dir/nuevo_nombre', fecha_a_setear) 
    de manera que pueda ser fácilmente usada por una función para completar 
    las tareas del Ejercicio 8.6.'''
    
    dir_nuevo = '../Data/imgs_procesadas/'
    info = ((os.path.join(directorio, archivo), os.path.join(dir_nuevo, 
            archivo[:-13]+'.png'), archivo[-12:-4])for directorio, archivo in 
            lista_archivos) 
    
    return info         
   
    
#%%
#%%    
if __name__ == '__main__':
    archivos = archivos_png('../Data/ordenar')
    archis = modificar_archivos(archivos)
    for a in archis:
        print (a)
    
    #archivos = archivos_png(sys.argv)
    #for a in archivos:
    #    print(a)

        
        
        
        
        