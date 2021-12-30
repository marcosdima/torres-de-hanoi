import random, time, os, numpy as np
from funciones import *

### Variables Iniciales ###

nro_discos = 3
nro_palos = 3
largo_palos = 17 + nro_discos
espacio = 20

### Posición de Discos ###

disc_0 = '00'
disc_1 = '01'
disc_2 = '02'

vector_posiciones = [disc_0, disc_1, disc_2] # 'xy' -> x = palos ; y = Discos

def menu():

    SALIR = False

    while not SALIR:

        os.system('clear')

        print('Menu Principal'.center(70))

        print()
        print('1- Reglas')
        print()
        print('2- Jugar')
        print()
        print('3- SALIR')
        print()
        eleccion = input('Seleccione una de las opciones [1/2/3]... ')
        print()

        if eleccion.isdigit():

            eleccion = int(eleccion)

            if eleccion == 1: # Reglas
                reglas()
                print()
                input('Press ENTER to continue... ')

            elif eleccion == 2: # Juego (PENDIENTE)
                pass

            elif eleccion == 3: # Salida
                SALIR = True

            else:
                print('Recuerde que tiene que seleccionar una de las opciones disponibles 1, 2 o 3. Por favor vuelva a intentarlo.')
                print()
                input('Press ENTER to continue... ')

        else:
            print('La opción seleccionada no existe, por favor vuelva a intentarlo.')
            print()
            input('Press ENTER to continue... ')


menu()
