"""
@author: marilinaorihuela

Lee los datos de un camion y calcula su costo
"""
#%%
import sys
from informe_final import leer_camion

#%%
def costo_camion(nombre_archivo):
    'Calcula el costo del camion'
    'Pre: recibe un archivo que contiene: nombre, cajones, precio'
    'Pos: devuelve la suma(cajones * precio)'

    camion=leer_camion(nombre_archivo)      
    
    #return sum([producto.cajones * producto.precio for producto in camion])
    return camion.precio_total()

#%% Función principal
def f_principal(argv):
    'Calcula el costo del camion'
    'Pre: recibe un archivo de la línea de comandos'
    'Pos: Imprime el costo'

    if len(argv) != 2:
        raise SystemExit(f'Uso adecuado: {argv[0]} ' 'archivo_camion')

    camion = argv[1]
 
    print('Costo total:', costo_camion(camion))
 

#%%
if __name__ == '__main__':
    
    f_principal(sys.argv)