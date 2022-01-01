import random, time, os, numpy as np
from funciones import *

def menu(nro_discos, nro_palos, nivel):

    SALIR = False

    while not SALIR:

    ### Variables Iniciales ###
        largo_palos = 17 + (nro_discos * 2)
        espacio = 17 + (nro_palos * 2)

    ### Posición de Discos ###

        vector_posiciones = []

        for i in range(nro_discos):
            posicion = '0' + str(i) # 'xy' -> x = palo ; y = Disco
            vector_posiciones.append(posicion)

        final = listas_ganar(nro_discos, nro_palos)

    ### Menú ###
        os.system('clear')

        print(f'Menu Principal: Nivel {nivel}'.center(70))

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

            elif eleccion == 2: # Juego

                JUEGO = True

                movis = 0 # Contador de movimientos

                base(largo_palos, espacio, nro_palos, nro_discos, vector_posiciones)

                while JUEGO:

                    print()
                    print(f'Movimientos: {movis}')
                    print()

                    movimiento = input('Ingrese el par de movimiento: ')
                    disco = int(movimiento[0])
                    palo = int(movimiento[1])

                    if detectar_arriba(disco, vector_posiciones):

                        print()
                        print('El disco seleccionado tiene uno por encima, por favor mueva el que esta encima primero.')
                        input('Press ENTER to continue... ')

                    else:

                        traslado = mover_discos(disco, vector_posiciones, palo, nro_discos, vector_posiciones[disco])

                        vector_posiciones[disco] = traslado

                        movis += 1

                        os.system('clear')
                        base(largo_palos, espacio, nro_palos, nro_discos, vector_posiciones)

                        for i in range(nro_palos-1):
                            if vector_posiciones == final[i]:
                                JUEGO = False
                                ganar(movis)
                                SALIR = True


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


nro_discos = 3
nro_palos = 3

menu(nro_discos, nro_palos, 1)
