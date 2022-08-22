#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: marilinaorihuela

"""
#%% 
import sys
import lote
from camion import Camion
import formato_tabla
from fileparse import parse_csv

#%%
def leer_camion(nombre_archivo):
    'Genera un diccionario del camion'
    'Pre: recibe un archivo.'
    'Pos: devuelve por cada fila: nombre, cajones, precio'
    
    with open(nombre_archivo) as file:
        camion_dicts = parse_csv(file, 
                                 select = ['nombre', 'cajones', 'precio'],
                                 types = [str, int, float])
    
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) 
              for d in camion_dicts]
    
    return Camion(camion)

           
#%%
def leer_precios(nombre_archivo):
    'Arma un diccionario de precios'
    'Pre: recibe un archivo.'
    'Pos: devuelve por cada fila: nombre, precio'
    
    with open(nombre_archivo) as file:    
        precios = parse_csv(file, types = [str, float], has_headers = False)
    lista_precios = dict(precios)

    return lista_precios

#%%
def hacer_informe(camion, precios):
    'Arma el informe'
    'Pre: recibe camion{} y precios{}.'
    'Pos: devuelve una lista de tuplas (nombre, cajones, costo, variacion)'
    
    informe=[]
    
    for producto in camion:
        
        variacion = precios[producto.nombre] - producto.precio
        lote = (producto.nombre, producto.cajones, producto.precio,
                variacion)
        informe.append(lote)

    return informe

#%% 
def imprimir_encabezado(head):
    'Imprime los encabezados del informe'
    
    print(f'{head[0]:>10s} {head[1]:>10s} {head[2]:>10s} {head[3]:>10s}')
    print('-'*10,'-'*10,'-'*10,'-'*10,)

#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

#%%
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    'Genera e imprime el informe'
    'Pre: recibe dos archivos: camion y precios'
    #leer datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    #creo los datos para el informe
    data_informe = hacer_informe(camion, precios)
    
    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
        
#%% Función principal
def f_principal(argv):
    'Genera el balance'
    'Pre: recibe dos archivos de la línea de comandos: camion y precios'
    'Pos: Imprime el informe'
   
    if len(argv) != 3:
        raise SystemExit(f'Uso adecuado: {argv[0]} ' 
                         'archivo_camion archivo_precios')

    camion = argv[1]
    precios = argv[2]
 
    informe_camion(camion, precios)    
 
    
#%%
if __name__ == '__main__':
    
    f_principal(sys.argv)





