import random, time, os, numpy as np
from funciones import *

def menu():

    SALIR = False

    while not SALIR:

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

    ### Menú ###
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

                JUEGO = True

                while JUEGO:

                    os.system('clear')

                    base(largo_palos, espacio, nro_palos, nro_discos, vector_posiciones)

                    print()
                    movimiento = input('Ingrese el movimiento deseado: ')

                    disco = int(movimiento[0])
                    palo = int(movimiento[1])

                    if detectar_arriba(disco, vector_posiciones):

                        print()
                        print('El disco seleccionado tiene uno por encima, por favor mueva el que esta encima primero.')
                        input('Press ENTER to continue... ')

                    else:

                        traslado = mover_discos(disco, vector_posiciones, palo, nro_discos, vector_posiciones[disco])

                        vector_posiciones[disco] = traslado


            elif eleccion == 3: # Salida
                SALIR = True

            else: # Error
                print('Recuerde que tiene que seleccionar una de las opciones disponibles 1, 2 o 3. Por favor vuelva a intentarlo.')
                print()
                input('Press ENTER to continue... ')

        else: # Error
            print('La opción seleccionada no existe, por favor vuelva a intentarlo.')
            print()
            input('Press ENTER to continue... ')


menu()
