#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:10:39 2021

@author: marilinaorihuela
"""
#%%
# camion.py

class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self, item):
        return self.lotes[item]
    
    def __repr__(self):
        return f'Camion({self.lotes})' 
    
    def __str__(self): 
        texto = f'Camion con {len(self)} lotes:'
        for lote in self.lotes:
            texto += '\n' + str(lote)
        return  texto 
    
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    