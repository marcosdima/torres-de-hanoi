import random, time, os, numpy as np

def base(largo_palos, espacio, nro_palos, nro_discos, vector_posiciones): # Dibuja el armatoste.

    os.system('clear')

    for i in range(4):
        print()

    contador = 0
    discos = calcualo_de_colocacion(nro_discos, largo_palos)

    posiciones = posicion_discos(nro_discos, nro_palos, espacio, vector_posiciones)

    vacio = ' ' * espacio

    for i in range(largo_palos):

        if contador < len(discos) and i == discos[contador]:

            relleno_final = 0

            for f in range(nro_palos):

                

                if posiciones[contador,f] != (espacio * ' '):

                    vacio_pa_discos = ' ' * (espacio - (len(posiciones[contador,f]) // 2) - relleno_final)
                    relleno_final = (len(posiciones[contador,f]) // 2) # Esto es para que no se corra los discos de la derecha
                    print(vacio_pa_discos + posiciones[contador,f],  end = '')

                else:
                    print(vacio + ' ', end = '')
            print()

            contador += 1


        else:
            for f in range(nro_palos):
                print(vacio + '|', end = '')
            print()

    base = '_' * espacio * (nro_palos-1) + ('_' * nro_palos)
    print(vacio + base)

def calcualo_de_colocacion(nro_discos, largo_palos): # Devuelve una lista con los lugares que les corresponderían a los discos.

    division = largo_palos // (nro_discos)

    colocacion = []

    for i in range(4, largo_palos-2, division):

        colocacion.append(i)

    return colocacion

def posicion_discos(nro_discos, nro_palos, espacio, vector_posiciones): # Deevuelve una matriz con la posición de los discos. 

    #vector_posiciones es una lista que contiene las posiciones en orden, del más chico al más grande.

    cuarto = (espacio // 4)

    vacio = espacio * ' '

    posiciones = np.array([[vacio]*nro_palos]*nro_discos) # Discos = Filas, Palos = Columnas

    contador = 2

    for i in vector_posiciones:

        x = int(i[1])
        y = int(i[0])

        disco = ('-' * cuarto) + '-' * contador

        posiciones[x,y] = disco

        contador += 2


    return posiciones

def mover_discos(disco, vector_posiciones, palo, nro_discos, posicion_actual):

    palo_nuevo = int(palo)

    SALIR = False

    fila_nueva = nro_discos - 1

    while not SALIR:


        espacio, tamaño = detectar_espacio_y_tamaño(vector_posiciones, fila_nueva, palo_nuevo, disco)

        if not espacio and tamaño:

            SALIR = True
            print('No se puede poner un disco grande sobre uno chico. Vuelva a intentarlo.')
            input('Press ENTER to continue... ')
            disco_a = posicion_actual

        elif espacio:

            disco_a = str(palo_nuevo) + str(fila_nueva)
            SALIR = True

        else:

            fila_nueva -= 1

    return disco_a

def detectar_espacio_y_tamaño(vector_posiciones, fila, palo, disco):

    espacio = True
    tamaño = False

    posicion = str(palo) + str(fila)

    for i in vector_posiciones:

        if posicion == i:
            espacio = False
            if disco > vector_posiciones.index(i):
                tamaño = True


    return espacio, tamaño


### Pruebas ###

nro_discos = 3

disc_0 = '00'
disc_1 = '12'
disc_2 = '23'

vector_posiciones = [disc_0, disc_1, disc_2] # 'xy' -> x = palos ; y = Discos

#print(mover_discos(2, vector_posiciones, 1, nro_discos, vector_posiciones[0]))