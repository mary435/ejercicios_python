#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 17:24:06 2021

@author: marilinaorihuela
"""


class FormatoTabla:
    'Clase base abstracta'
    def encabezado(self, headers):
        'Crea el encabezado de la tabla.'
        raise NotImplementedError()

    def fila(self, rowdata):
        'Crea una única fila de datos de la tabla.'
        raise NotImplementedError()
    
'''    def crear_formateador(self, tipo):
        'Crea un objeto formateador dado un tipo'        
        #def __new__(self, tipo):
        if tipo == 'txt':
            return FormatoTablaTXT()
        elif tipo == 'csv':
            return FormatoTablaCSV()
        elif tipo == 'html':
            return FormatoTablaHTML()
        else:
            raise RuntimeError(f'Unknown format {tipo}')
'''

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()


class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''   
    def encabezado(self, headers):
        print('<tr><th>','</th><th>'.join(headers),'</th></tr>', sep='')
    def fila(self, data_fila):
        print('<tr><td>','</td><td>'.join(data_fila),'</td></tr>', sep='')
        
        
       
class crear_formateador(FormatoTabla):
    'Crea un objeto formateador dado un tipo'        
    def __new__(self, tipo):
        if tipo == 'txt':
            return FormatoTablaTXT()
        elif tipo == 'csv':
            return FormatoTablaCSV()
        elif tipo == 'html':
            return FormatoTablaHTML()
        else:
            raise RuntimeError(f'Unknown format {tipo}')


 









