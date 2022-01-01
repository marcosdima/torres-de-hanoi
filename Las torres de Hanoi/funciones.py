import random, time, os, numpy as np

def base(largo_palos, espacio, nro_palos, nro_discos, vector_posiciones, REGLAS): # Dibuja el armatoste. (REGLAS surge de la necesidad de que no se borre cuando esta en el tutorial)

    if not REGLAS:
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
            print()
            print('No se puede poner un disco grande sobre uno chico. Vuelva a intentarlo.')
            input('Press ENTER to continue... ')
            disco_a = posicion_actual

        elif espacio:

            disco_a = str(palo_nuevo) + str(fila_nueva)
            SALIR = True

        else:

            fila_nueva -= 1

    return disco_a

def detectar_espacio_y_tamaño(vector_posiciones, fila, palo, disco): # Dandole los parametros indicados, detecta si hay espacio en el pilar/torre y si estás poniendo un disco grande sobre uno chico.

    espacio = True
    tamaño = False

    posicion = str(palo) + str(fila)

    for i in vector_posiciones:

        if posicion == i:
            espacio = False
            if disco > vector_posiciones.index(i):
                tamaño = True


    return espacio, tamaño

def reglas():

    os.system('clear')

    print('Reglas'.center(70))
    print()
    reglas = ['El objetivo del juego es mover la torre de un pilar a otro.', 'Los discos solo se mueven uno a la vez', 'Un disco no se puede poner sobre otro más chico.', 'Para indicar el movimiento deseado, ingrese una pareja de numeros. Donde el primero sea del disco a mover y el segundo de la torre destino.', 'Para referirse a los discos deben orientarse por el tamaño, el más chico es el disco "0" (cero) y a medida que se aumenta el tamaño, sube en 1 dicha etiqueta.', 'Con los palos es similar, el máz a la izquierda es el palo "0" y a medida que se mueve a la derecha se aumenta en uno.']
    for i in reglas:
        print('- ', i)

    print()
    input('Press ENTER to continue... ')
    print()
    print('Ejemplo:')
    print()

    base(20, 20, 3, 3, ['00','01','02'], True)

    print()
    print()
    print('Ingrese el par de movimiento: 01 <-- El "0" indica que seleccionas el disco más pequeño y el "1" que queres moverlo al pilar 1°.')

    base(20, 20, 3, 3, ['12','01','02'], True)

    print()
    print()
    print('El disco "0" se movió al pilar "1".')

def detectar_arriba(disco, vector_posiciones): # Devuelve True si el disco indicado tiene un disco arriba

    posicion = vector_posiciones[disco]

    fila = str(int(posicion[1]) - 1)
    columna = posicion[0]

    posicion_arriba = columna + fila

    arriba = False

    if disco == 0:
        pass

    else:

        for i in vector_posiciones:
            if i == posicion_arriba:
                arriba = True

    return arriba

def listas_ganar(nro_discos, nro_palos): # Genera las posibles convinaciones ganadoras

    final = []

    for p in range(1, nro_palos+1):

        posiciones = []

        for d in range(nro_discos):
            posicion = str(p) + str(d)
            posiciones.append(posicion)

        final.append(posiciones)

    return final

def ganar(movis):

    for i in range(3):
        print()

    ganaste = open('ganaste.txt', 'r')

    linea = ganaste.readline().strip()

    while linea != '':

        print(linea)
        linea = ganaste.readline().strip()

    for i in range(3):
        print()

    print(f'Te tomo {movis} movimientos! Bien Hecho!')
    print()
    input('Press ENTER to continue... ')


### Pruebas ###

nro_discos = 3

disc_0 = '00'
disc_1 = '01'
disc_2 = '02'

vector_posiciones = [disc_0, disc_1, disc_2] # 'xy' -> x = palos ; y = Discos

#print(mover_discos(2, vector_posiciones, 1, nro_discos, vector_posiciones[0]))

#print(detectar_arriba(1, vector_posiciones))

#reglas()

#ganar(10)