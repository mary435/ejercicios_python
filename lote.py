#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:21:45 2021

@author: marilinaorihuela
"""

class Lote:
    'Representa un lote de cajones de una misma fruta'
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    def __repr__(self):
        return f'Lote(\'{self.nombre}\', {self.cajones}, {self.precio})'
    
    def __str__(self):
        texto = f'Lote de {self.cajones} cajones de \'{self.nombre}\', '
        texto += f'pagados a ${self.precio} cada uno.' 
        return  texto
    
    def vender(self, cantidad):
        self.cajones -= cantidad
        return self.cajones
    
    def costo(self):
        return self.cajones * self.precio
    
    
    
        
        
        