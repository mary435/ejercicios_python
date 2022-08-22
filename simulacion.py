# -*- coding: utf-8 -*-
"""
mundo.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""
#%% Archivo Mundo

from animal import Leon, Antilope
from tablero import Tablero

#%%
def print_debug(msg, print_flag=False):
    if print_flag:
        print(msg)

class Mundo(object):
    """docstring for Mundo"""

    def __init__(self, columnas, filas, n_leones, n_antilopes, debug=False):
        super(Mundo, self).__init__()

        self.debug = debug

        self.ciclo = 0
        self.tablero = Tablero(filas, columnas)
        self.llenar_mundo(n_leones, n_antilopes)


    def llenar_mundo(self, n_leones, n_antilopes):
        for _ in range(n_leones):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un leon", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Leon())

        for _ in range(n_antilopes):
            if self.tablero.hay_posiciones_libres():
                print_debug("ubicando un Antilope", self.debug)
                self.tablero.ubicar_en_posicion_vacia(Antilope())

    def cant_leones(self):
        return sum([1 for x in self.tablero.elementos() if x.es_leon()])

    def cant_antilopes(self):
        return sum([1 for x in self.tablero.elementos() if x.es_antilope()])

    def etapa_movimiento(self):
        print_debug(f"Iniciando Movimiento en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            posiciones_libres = self.tablero.posiciones_vecinas_libre(p)
            nueva_posicion = animal.moverse(posiciones_libres)
            if nueva_posicion:
                self.tablero.mover(p, nueva_posicion)

    def etapa_alimentacion(self):
        print_debug(f"Iniciando Alimentación en ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
            desplazo = animal.alimentarse(animales_cercanos)
            if desplazo:
                self.tablero.ubicar(desplazo, self.tablero.retirar(p))
                print_debug(f' Se retira {"Antilope: "if animal.es_leon() else "Leon: "}{p}', self.debug)
            #else:
            #    print_debug(f' No se pudo alimentar {"Antilope: " if animal.es_leon() else "Leon: "}{p}', self.debug)
    
    def etapa_reproduccion(self):
        print_debug(f"Iniciando Reproducción en ciclo {self.ciclo}", self.debug)
        if self.tablero.posiciones_libres():
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                if animal.puede_tener_cria():
                    animales_cercanos = self.tablero.posiciones_vecinas_con_ocupantes(p)
                    cria_pos = animal.reproducirse(animales_cercanos, self.tablero.posiciones_libres())
                    if cria_pos:
                        if animal.es_leon():
                            print_debug(f" Nace un nuevo leoncito en la posición {cria_pos}", self.debug)
                            self.tablero.ubicar(cria_pos,Leon())
                        if animal.es_antilope():
                            print_debug(f" Nace un nuevo antilopecito en la posición {cria_pos}", self.debug)
                            self.tablero.ubicar(cria_pos,Antilope())
        # pass

    def cerrar_un_ciclo(self):
        print_debug(f"Concluyendo ciclo {self.ciclo}", self.debug)
        for p in self.tablero.posiciones_ocupadas():
            animal = self.tablero.posicion(p)
            animal.pasar_un_ciclo() #envejecer, consumir alimento
            if not animal.en_vida():
                self.tablero.retirar(p)
                print_debug(f' Se retira {"Leon: "if animal.es_leon() else "Antilope: "}{p}', self.debug)
        self.ciclo += 1

    def pasar_un_ciclo(self):
        self.etapa_movimiento()
        self.etapa_alimentacion()
        self.etapa_reproduccion()
        self.cerrar_un_ciclo()


    def __repr__(self):
        res = str(self.tablero)
        res += f"\nEstamos en la ciclo {self.ciclo}"
        res += f"\nCon {self.cant_leones()} Leones, y {self.cant_antilopes()} Antilopes."
        if False:
            res += '\nEspecie   Posicion   años  energia   puede_reproduc\n'
            for p in self.tablero.posiciones_ocupadas():
                animal = self.tablero.posicion(p)
                res += f'{"Leon    " if animal.es_leon() else "Antilope"} {str(p):^10s} {animal.fila_str()}\n'

        return res

    def __str__(self):
        return self.__repr__()
    
#%% Archivo Animal

# -*- coding: utf-8 -*-
"""
animal.py
Created on Wed Oct  7 14:00:00 2020
@author: mlopez
"""
#%%
import random

#%%
class Animal(object):
    """docstring for Animal"""
    def __init__(self):
        super(Animal, self).__init__()
        self.reproducciones_pendientes = 4
        self.edad = 0
        self.sexo = None # Posible mejora para que no se puedan reproducir dos del mismo sexo
        self.energia = self.energia_maxima
        self.es_reproductore = False

    def pasar_un_ciclo(self):
        self.energia -= 1 # Se puede restar si no llega a comer
        self.edad += 1
        if self.reproducciones_pendientes > 0: #
            self.es_reproductore = True

    def en_vida(self):
        return (self.edad <= self.edad_maxima) and self.energia > 0

    def tiene_hambre(self):
        """Acá se puede poner comportamiento para que no tenga hambre todo el tiempo
        debería depender de la diferencia entre su nivel de energía y su energía máxima"""
        if self.energia < self.energia_maxima:
            return True
        return False
        #pass
    def puede_tener_cria(self):
        if self.en_vida() and self.edad >= 2 and self.es_reproductore == True:
            return True
        return False
    
    def es_leon(self):
        return False

    def es_antilope(self):
        return False

    def puede_reproducir(self):
        return self.es_reproductore

    def tener_cria(self):
        """Acá se puede poner comportamiento que sucede al tener cria para 
        evitar que tengamás de una cria por ciclo, etc"""
        self.reproducciones_pendientes -= 1
        self.es_reproductore = False
        # pass

    def reproducirse(self, vecinos, lugares_libres):
        pos = None
        if self.es_leon():
            amigos_cercanos = [animal for (pos, animal) in vecinos 
                               if animal.es_leon() and animal.puede_tener_cria()]
        if self.es_antilope():
            amigos_cercanos = [animal for (pos, animal) in vecinos 
                               if animal.es_antilope() and animal.puede_tener_cria()]
        
        if amigos_cercanos:
            animal  = random.choice(amigos_cercanos)
            if lugares_libres:
                animal.tener_cria()
                self.tener_cria()
                pos = random.choice(lugares_libres)

        return pos

    def alimentarse(self, animales_vecinos = None):
        self.energia = self.energia_maxima
        return None

    def moverse(self, lugares_libres):
        pos = None
        if lugares_libres:
            pos = random.choice(lugares_libres)

        return pos

    def fila_str(self):
        return f"{self.edad:>3d}    {self.energia:>3d}/{self.energia_maxima:<3d}       {self.es_reproductore!s:<5}"

    def __format__(self):
        return self.__repr__()

    def __str__(self):
        return self.__repr__()


class Leon(Animal):
    """docstring for Leon"""
    def __init__(self):
        self.energia_maxima = 6
        self.edad_maxima = 10
        super(Leon, self).__init__()

    def es_leon(self):
        return True

    def alimentarse(self, animales_vecinos):
        # Se alimenta si puede e indica la posición del animal que se pudo comer
        pos = None
        p = 1
    
        if self.tiene_hambre(): # no está lleno 
            presas_cercanas = [(pos,animal) for (pos, animal) in animales_vecinos 
                           if animal.es_antilope()]
            if presas_cercanas: # hay presas cerca
                (pos, animal) = random.choice(presas_cercanas) #(pos, animal) elijo 1
                if self.edad < 4 or self.edad > 7: # leon joven/viejo baja la prob.
                    p = p/2
                if animal.edad < 3 or animal.edad > 4: #presa joven/viejo baja la prob.
                    p = p/2
                if len(presas_cercanas) > 4: # presa en manada baja la prob.
                    p = p/2
                if random.random() > p:
                    super(Leon, self).alimentarse()
                else:
                    pos = None

        return pos


    def __repr__(self):
        # return "León"
        return "L{}".format(self.edad)



class Antilope(Animal):
    """docstring for Antilope"""
    def __init__(self):
        self.energia_maxima = 10
        self.edad_maxima = 6
        super(Antilope, self).__init__()
        self.reproducciones_pendientes = 3

    def es_antilope(self):
        return True

    def __repr__(self):
        # return "A"
        return "A{}".format(self.edad)
    
    


