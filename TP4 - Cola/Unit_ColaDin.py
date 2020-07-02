from TDA_ColaDin import Cola, arribo, atencion, cola_vacia, barrido_cola
from TDA_ColaDin import colaint, colastring, colaneg, colacaracteres, primos
from TDA_ColaDin import tamanio_cola, en_frente, mover_final
from TDA_PilaDin import Pila, apilar, desapilar, pila_vacia, pilaint
from TDA_PilaDin import barrido_pila, ordenar_pila
from math import asin, sqrt, sin, cos, radians
from time import sleep
from random import randint, choice


print('TP4 - COLA')
print('')

# Declaraciones para ejercicios
vec = [5, 3, 2, 1, 6, 9, 0, 8, 7, 4]

CE = Cola()
colaint(CE, 10)
# print('Cola de numeros enteros')
# barrido_cola(CE)
# print('')

CS = Cola()
colastring(CS, 10)
# print('Cola de letras')
# barrido_cola(CS)
# print('')

CN = Cola()
colaneg(CN, 10)
# print('Cola de numeros enteros positivos y negativos')
# barrido_cola(CN)
# print('')

CC = Cola()
colacaracteres(CC, 50000)
# print('Cola de caracteres')
# barrido_cola(CC)
# print('')

PN = Pila()
pilaint(PN, 10)
# print('Pila de numeros enteros')
# barrido_pila(PN)
# print('')


# EJ 1
def vocales(C):
    '''Elimina las vocales de una cola'''
    Caux = Cola()
    while not cola_vacia(C):
        x = atencion(C)
        if ord(x.lower()) != 97 and ord(x.lower()) != 101 and ord(x.lower()) != 105 and ord(x.lower()) != 111 and ord(x.lower()) != 117:
            arribo(Caux, x)
    C = Caux
    print('Cola sin vocales')
    barrido_cola(C)


# EJ 2
def invertir_cola(C):
    '''Invierte el contenido de una cola con una pila auxiliar'''
    P = Pila()
    while not cola_vacia(C):
        apilar(P, atencion(C))
    while not pila_vacia(P):
        arribo(C, desapilar(P))
    print('Cola invertida')
    barrido_cola(C)


# EJ 3
def palindromo():
    '''Devuelve True si una palabra es un palindromo'''
    P = Pila()
    C = Cola()
    cad = 'neuquen'
    palindr = True
    print(cad)
    for letra in cad:
        apilar(P, letra)
        arribo(C, letra)
    for i in range(0, tamanio_cola(C)):
        dato_cola = atencion(C)
        dato_pila = desapilar(P)
        if dato_cola != dato_pila:
            palindr = False
    if palindr:
        print(True)
    else:
        print(False)


# EJ 4
def eliminacion(C):
    '''Elimina los numeros NO primos de una cola'''
    Caux = Cola()
    while not cola_vacia(C):
        x = atencion(C)
        if primos(x):  # Funcion primos() en TDA_ColaDin
            arribo(Caux, x)
    C = Caux
    print('Cola de numeros primos')
    barrido_cola(C)


# EJ 5
def invertir_pila_cola(P):
    '''Invierte el contenido de una pila con una cola auxiliar'''
    C = Cola()
    while not pila_vacia(P):
        arribo(C, desapilar(P))
    while not cola_vacia(C):
        apilar(P, atencion(C))
    print('Pila invertida')
    barrido_pila(P)


# EJ 6
def ocurrencias(C):
    '''Cantidad de repeticiones de un determinado elemento en una cola'''
    c = 0
    busc = 2   # elemento a comparar
    while not cola_vacia(C):
        dato = atencion(C)
        if dato == busc:
            c += 1
    print('El elemento', busc, 'se repite', c, 'veces')


# EJ 7
def i_esimo_cola(C):
    '''Elimina un i-esimo elemento despues de frente de la cola'''
    Caux = Cola()
    pos = 5
    if tamanio_cola(C) > pos:
        i = 0
        while i < pos:
            x = atencion(C)
            arribo(Caux, x)
            i += 1
        elim = atencion(C)
        print('elemento eliminado:', elim)
        while not cola_vacia(C):
            arribo(Caux, atencion(C))
        print('Nueva cola')
        barrido_cola(Caux)
    else:
        print('Se excedio la cantidad de posiciones')


# EJ 8
def cola_ordenada():
    '''Manteniene ordenados los elementos agregados en una cola'''
    C = Cola()
    Caux = Cola()
    for i in range(10):
        dato = randint(1, 50)
        print(str(dato) + ' agregado')   # pregunta uno por uno
        while not cola_vacia(C) and en_frente(C) <= dato:
            arribo(Caux, atencion(C))
        arribo(Caux, dato)
        while not cola_vacia(C):
            arribo(Caux, atencion(C))
        while not cola_vacia(Caux):
            arribo(C, atencion(Caux))
    print()
    print('Cola ordenada:')
    barrido_cola(C)


# EJ 9
def rango_negativos(C):
    '''Calcula el rango de valores de una cola y la cantidad
    de numeros negativos que contiene'''
    neg, rango, max, min = 0, 0, 0, 0
    while not cola_vacia(C):
        x = atencion(C)
        if x > max:
            max = x
        if x < min:
            min = x
        if x < 0:
            neg += 1
    rango = max + min
    print('Rango de valores enteros: ' + str(rango))
    print('Cantidad de numeros negativos: ' + str(neg))


# EJ 10
def personajes_sw():
    '''Operaciones sobre una cola de personajes de star wars
    y sus planetas de origen'''
    C, Caux, C1, C2 = Cola(), Cola(), Cola(), Cola()
    personaje = ['Breha Organa', 'Bail Organa', 'Killik',
                 'Chirpa el Ewok', 'Asha Fahn el Ewok', 'Kneesaa el Ewok',
                 'Saqueador Tusken', 'Dathcha el Jawa', 'Jabba el Hutt',
                 'Luke Skywalker', 'Han Solo', 'Yoda',
                 'Jar Jar Binks', 'Darth Maul']
    origen = ['Alderaan', 'Alderaan', 'Alderaan', 'Endor', 'Endor', 'Endor',
              'Tatooine', 'Tatooine', 'Tatooine', 'Polis Massa', 'Corellia',
              'Desconocido', 'Naboo', 'Dathomir']
    for i in range(0, len(personaje)):
        arribo(C, [personaje[i], origen[i]])
    print('Personaje  |   Planeta de origen')
    barrido_cola(C)
    print()
    while not cola_vacia(C):
        x = atencion(C)
        if x[1] == 'Alderaan' or x[1] == 'Endor' or x[1] == 'Tatooine':
            print(str(x[0]) + ' originario/a del planeta ' + str(x[1]))
        if x[0] == 'Luke Skywalker' or x[0] == 'Han Solo':
            print(str(x[0]) + ' originario/a del planeta ' + str(x[1]))
        if x[0] != 'Yoda':
            arribo(C1, x)
        else:
            arribo(C1, ['Sheev Palpatine', 'Naboo'])
            arribo(C1, x)
        arribo(Caux, x)
        while not cola_vacia(Caux):
            x = atencion(Caux)
            if x[0] == 'Jar Jar Binks' and not cola_vacia(Caux):
                atencion(Caux)
            arribo(C2, x)
    print()
    print('Agregar personaje antes de Yoda')
    barrido_cola(C1)
    print()
    print('Eliminar personaje despues de Jar Jar Binks')
    barrido_cola(C2)


# EJ 11
def dos_colas():
    '''Combina dos colas en una ordenada'''
    C1 = Cola()
    C2 = Cola()
    dato1 = [0, 2, 4, 6, 8]
    dato2 = [1, 3, 5, 7, 9]
    for i in range(0, len(dato1)):
        arribo(C1, dato1[i])
        arribo(C2, dato2[i])
    print('Cola 1')
    barrido_cola(C1)
    print('Cola 2')
    barrido_cola(C2)
    print()
    for i in range(0, tamanio_cola(C1)):
        if en_frente(C1) < en_frente(C2):
            mover_final(C1)
        else:
            while en_frente(C1) > en_frente(C2):
                arribo(C1, atencion(C2))
            mover_final(C1)
    while not cola_vacia(C2):
        arribo(C1, atencion(C2))
    print('Cola combinada y ordenada')
    barrido_cola(C1)


# EJ 12
def caracteres(C):
    '''Operaciones con una cola de letras, numeros y simbolos'''
    C_dig = Cola()
    C_car = Cola()
    cont_letras = 0
    numer, inter = False, False
    while not cola_vacia(C):
        dato = atencion(C)
        if dato.isdigit():
            arribo(C_dig, dato)
        else:
            arribo(C_car, dato)
    # barrido_cola(C_dig)
    # barrido_cola(C_car)
    print('Tamanio de la cola de numeros: ' + str(tamanio_cola(C_dig)))
    print('Tamanio de la cola de caracteres: ' + str(tamanio_cola(C_car)))
    while not cola_vacia(C_car):
        dato = atencion(C_car)
        if dato.isalpha():
            cont_letras += 1
        if dato == '?':
            inter = True
        if dato == '#':
            numer = True
    print('Cantidad de letras en la cola de caracteres: ' + str(cont_letras))
    if inter:
        print('Existen signos de interrogacion en la cola')
    else:
        print('NO existen signos de interrogacion en la cola')
    if numer:
        print('Existen numerales en la cola')
    else:
        print('NO existen numerales en la cola')


# EJ 14
def Haversine():
    '''Datos de bases rebeldes proporcionados a un Caza TIE'''
    C, Caux, P = Cola(), Cola(), Pila()
    base = ['Base Dantooine', 'Base Eco', 'Cuartel General de la Resistencia',
            'Gran Templo de Massassi', 'Puesto de avanzada Beta']
    lat = [73, -23, -37, 45, 4]
    lng = [-54, 166, -72, 4, 113]
    q1 = radians(randint(-90, 90))  # latitud de origen
    d1 = radians(randint(-180, 180))  # longitud de origen
    # q2 = latitud de llegada
    # d2 = longitud de llegada
    r = 6371  # en kilometros
    c1, c2, c3 = 0, 0, 0
    for i in range(len(base)):
        arribo(C, [base[i], randint(10, 200), lat[i], lng[i]])
    print('Base | Tamanio de la flota | Latitud | Longitud')
    barrido_cola(C)
    print()
    print('Coordenada actual:', round(q1, 6), ',', round(d1, 6))
    while not cola_vacia(C):
        x = atencion(C)
        q2 = radians(x[2])
        d2 = radians(x[3])
        formula = 2*r*asin(sqrt(sin((q1-q2)/2)**2+cos(q1)*cos(q2)*sin((d1-d2)/2)**2))
        dist = int(formula)
        print(x[0] + ' se encuentra a ' + str(dist) + 'km')
        apilar(P, [dist, x[0], x[1]])
        arribo(Caux, [x[1], x[0], dist])
    print()
    P = ordenar_pila(P)
    c1 = desapilar(P)
    c2 = desapilar(P)
    c3 = desapilar(P)
    print('Las tres bases mas cercanas son:')
    print(c1[1] + ' se encuentra a ' + str(c1[0]) + 'km')
    print(c2[1] + ' se encuentra a ' + str(c2[0]) + 'km')
    print(c3[1] + ' se encuentra a ' + str(c3[0]) + 'km')
    if c1[2] > c2[2] and c1[2] > c3[2]:
        print(c1[1] + ' posee la mayor flota aerea')
    elif c2[2] > c1[2] and c2[2] > c3[2]:
        print(c2[1] + ' posee la mayor flota aerea')
    else:
        print(c3[1] + ' posee la mayor flota aerea')
    print()
    barrido_cola(Caux)
    cont = 0
    while not cola_vacia(Caux):
        dato = atencion(Caux)
        if dato[0] > cont:
            cont = dato[0]
            info = dato
    print()
    print(info[1], 'posee la mayor flota(' + str(info[0]) + ')')
    print('Se encuentra a:', info[2], 'km')


# EJ 16
def procesador():
    '''Cola de procesos de ejecucion en un procesador'''
    C = Cola()
    id = [1, 455, 3421, 5628, 9340]
    te = [3, 5, 4, 12, 2]
    for i in range(len(id)):
        arribo(C, [id[i], te[i]])
    print('ID | Tiempo de ejecucion')
    while not cola_vacia(C):
        dato = atencion(C)
        print()
        print('Ejecutando: ' + str(dato))
        if dato[1] < 4.5:
            sleep(dato[1])
            print(str(dato) + ' ejecutado con exito')
        else:
            print('El dato ' + str(dato) + ' excedio el tiempo de procesamiento de 4,5 segundos')
            print('El dato ha sido devuelto a la cola con el tiempo restante de ejecucion')
            dato[1] = dato[1] - 4.5
            arribo(C, dato)
            print()
            while True:
                try:
                    print('Presione 1 si desea ingresar un nuevo proceso')
                    print('Presione 2 si quiere omitir el paso 1')
                    val = int(input())
                    if val == 1:
                        id = int(input('Ingrese ID: '))
                        te = int(input('Ingrese Tiempo de ejecucion: '))
                        arribo(C, [id, te])
                        break
                    elif val == 2:
                        break
                except Exception:
                    print('Solo puede ingresar 1 o 2')


# EJ 17
def turnos():
    '''Cola de turnos en un consultorio'''
    Corig, Caux, C1, C2 = Cola(), Cola(), Cola(), Cola()
    letr = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(1000):
        # zfill() agrega ceros a la izquierda
        arribo(Corig, [choice(letr), randint(000, 999)])
    barrido_cola(Corig)
    while not cola_vacia(Corig):
        dato = atencion(Corig)
        if dato[0] == 'A' or dato[0] == 'C' or dato[0] == 'F':
            arribo(C1, dato)
        if dato[0] == 'B' or dato[0] == 'D' or dato[0] == 'E':
            arribo(C2, dato)
        arribo(Caux, dato)
    print('Cantidad turnos A, C o F: ' + str(tamanio_cola(C1)))
    print('Cantidad turnos B, D o E: ' + str(tamanio_cola(C2)))
    if tamanio_cola(C1) > tamanio_cola(C2):
        print('La cola 1 tiene mayor cantidad de turnos')
    elif tamanio_cola(C2) > tamanio_cola(C1):
        print('La cola 2 tiene mayor cantidad de turnos')
    else:
        print('Son iguales')
    print('')
    A, C, F = 0, 0, 0
    B, D, E = 0, 0, 0
    while not cola_vacia(C1):
        dato1 = atencion(C1)
        if dato1[0] == 'A':
            A += 1
        if dato1[0] == 'C':
            C += 1
        if dato1[0] == 'F':
            F += 1
    while not cola_vacia(C2):
        dato2 = atencion(C2)
        if dato2[0] == 'B':
            B += 1
        if dato2[0] == 'D':
            D += 1
        if dato2[0] == 'E':
            E += 1
    print('La cola 1 contiene:')
    print('A: ' + str(A) + ', C: ' + str(C) + ', F: ' + str(F))
    print('La cola 2 contiene:')
    print('B: ' + str(B) + ', D: ' + str(D) + ', E: ' + str(E))
    print('')
    if A > C and A > F:
        print('En cola 1, mayoria de letras A')
    elif C > A and C > F:
        print('En cola 1, mayoria de letras C')
    else:
        print('En cola 1, mayoria de letras F')
    if B > D and B > E:
        print('En cola 2, mayoria de letras B')
    elif D > B and D > E:
        print('En cola 2, mayoria de letras D')
    else:
        print('En cola 2, mayoria de letras E')
    print('')
    cont = 0
    while not cola_vacia(Caux):
        dato = atencion(Caux)
        if dato[1] <= 506:
            # print(dato)
            cont += 1
    print('Cantidad de turnos con numero menor a 506: ' + str(cont))


# EJ 19
def peajes():
    '''Control de un puesto de peajes'''
    C1, C2, C3 = Cola(), Cola(), Cola()
    vehiculo = ['Automovil', 'Camioneta', 'Camion', 'Colectivo']
    cab1, cab2, cab3 = 0, 0, 0
    aut1, cta1, cmn1, col1 = 0, 0, 0, 0
    aut2, cta2, cmn2, col2 = 0, 0, 0, 0
    aut3, cta3, cmn3, col3 = 0, 0, 0, 0
    for i in range(30):
        arribo(C1, choice(vehiculo))
        arribo(C2, choice(vehiculo))
        arribo(C3, choice(vehiculo))
    # barrido_cola(C1)
    # barrido_cola(C2)
    # barrido_cola(C3)
    print('Tarifas:')
    print('Automoviles $47, Camionetas $59, Camiones $71, Colectivos $64')
    print('')
    while not cola_vacia(C1):  # conteo cabina 1
        v = atencion(C1)
        if v == 'Automovil':
            cab1 += 47
            aut1 += 1
        if v == 'Camioneta':
            cab1 += 59
            cta1 += 1
        if v == 'Camion':
            cab1 += 71
            cmn1 += 1
        if v == 'Colectivo':
            cab1 += 64
            col1 += 1
    while not cola_vacia(C2):  # conteo cabina 2
        v = atencion(C2)
        if v == 'Automovil':
            cab2 += 47
            aut2 += 1
        if v == 'Camioneta':
            cab2 += 59
            cta2 += 1
        if v == 'Camion':
            cab2 += 71
            cmn2 += 1
        if v == 'Colectivo':
            cab2 += 64
            col2 += 1
    while not cola_vacia(C3):  # conteo cabina 3
        v = atencion(C3)
        if v == 'Automovil':
            cab3 += 47
            aut3 += 1
        if v == 'Camioneta':
            cab3 += 59
            cta3 += 1
        if v == 'Camion':
            cab3 += 71
            cmn3 += 1
        if v == 'Colectivo':
            cab3 += 64
            col3 += 1
    print('La cabina 1 recaudo: $' + str(cab1))
    print('La cabina 2 recaudo: $' + str(cab2))
    print('La cabina 3 recaudo: $' + str(cab3))
    if cab1 > cab2 and cab1 > cab3:
        print('La cabina 1 recuado mayor cantidad de pesos')
    elif cab2 > cab1 and cab2 > cab3:
        print('La cabina 2 recuado mayor cantidad de pesos')
    else:
        print('La cabina 3 recuado mayor cantidad de pesos')
    print('')
    print('--EN CABINA 1 INGRESARON--')
    print('Automoviles: ' + str(aut1))
    print('Camionetas: ' + str(cta1))
    print('Camiones: ' + str(cmn1))
    print('Colectivos: ' + str(col1))
    print('')
    print('--EN CABINA 2 INGRESARON--')
    print('Automoviles: ' + str(aut2))
    print('Camionetas: ' + str(cta2))
    print('Camiones: ' + str(cmn2))
    print('Colectivos: ' + str(col2))
    print('')
    print('--EN CABINA 3 INGRESARON--')
    print('Automoviles: ' + str(aut3))
    print('Camionetas: ' + str(cta3))
    print('Camiones: ' + str(cmn3))
    print('Colectivos: ' + str(col3))
    print('')


# EJ 20
def aeropuerto():
    '''Algoritmo que permite administrar los despegues y aterrizajes de un
    aeropuerto'''
    Cdesp, Cater = Cola(), Cola()
    empr = ['Singapore Airlines', 'Fly Emirates', 'LATAM', 'Qatar Airways',
            'Aerolineas Argentinas', 'Iberia', 'Turkish Airlines', 'Avianca']
    hs = [00.30, 02.00, 04.45, 07.15,
          12.15, 15.30, 18.05, 20.40]
    hl = [03.10, 04.30, 08.00, 11.25,
          14.30, 17.50, 21.20, 23.45]
    aero = ['Aeropuerto Alfa', 'Aeropuerto Beta', 'Aeropuerto Gamma',
            'Aeropuerto Delta', 'Aeropuerto Lambda', 'Aeropuerto Sigma',
            'Aeropuerto Omega', 'Aeropuerto Epsilon', 'Aeropuerto Kappa']
    tipo = ['Negocios', 'Carga', 'Pasajeros']
    tdesp = [9, 3, 5]
    tater = [12, 5, 10]
    print('     Empresa      | Hora salida | Hora llegada |    Origen    |    Destino    | Tipo de vuelo')
    for i in range(len(empr)):
        arribo(Cdesp, [empr[i], hs[i], hl[i], choice(aero), choice(aero), choice(tipo)])
    barrido_cola(Cdesp)
    print('')
    while not cola_vacia(Cdesp) or not cola_vacia(Cater):
        if not cola_vacia(Cater):
            avion = atencion(Cater)
            pos = tipo.index(avion[5])
            tiempo = tater[pos]
            print('')
            print('Aterrizando avion de la empresa: ' + str(avion[0]))
            print('Horario de llegada: ' + str('{0:.2f}'.format(avion[2]).zfill(5)) + 'hs')
            print('Tipo de vuelo: ' + str(avion[5]))
            sleep(tiempo)
        else:
            avion = atencion(Cdesp)
            pos = tipo.index(avion[5])
            tiempo = tdesp[pos]
            print('')
            print('Despegando avion de la empresa: ' + str(avion[0]))
            print('Horario de salida: ' + str('{0:.2f}'.format(avion[1]).zfill(5)) + 'hs')
            print('Tipo de vuelo: ' + str(avion[5]))
            sleep(tiempo)
            arribo(Cater, avion)


# EJ 21
def marvel():
    '''Cola con personajes de Marvel Cinematic Universe'''
    C = Cola()
    personaje = ['Carol Danvers', 'Natasha Romanoff', 'Gamora Zen Whoberi',
                 'Tony Stark', 'Scott Lang', 'Steve Rogers', 'Stephen Strange',
                 'Peter Benjamin Parker']
    superheroe = ['Capitana Marvel', 'Black Widow', 'Gamora', 'Iron Man',
                  'Ant-Man', 'Capitan America', 'Doctor Strange', 'Spider Man']
    genero = ['F', 'F', 'F', 'M', 'M', 'M', 'M', 'M']
    for i in range(len(personaje)):
        arribo(C, [personaje[i], superheroe[i], genero[i]])
    print('Nombre del personaje | Nombre del superheroe | Genero')
    barrido_cola(C)
    print('')
    while not cola_vacia(C):
        dato = atencion(C)
        if dato[1] == 'Capitana Marvel':
            print('El personaje de la Capitana Marvel es: ' + dato[0])
        if dato[2] == 'F':
            print(dato[1] + ', personaje femenino')
        if dato[2] == 'M':
            print(dato[1] + ', personaje masculino')
        if dato[0] == 'Scott Lang':
            print('El nombre del superheroe de Scott Lang es: ' + dato[1])
        cad = dato[0]
        if cad[0] == 'S' or cad[0] == 'S':
            print('El personaje ' + dato[0] + ' empieza con S')
            print('El superheroe ' + dato[1] + ' empieza con S')
        if dato[0] == 'Carol Danvers':
            print('El superheroe de Carol Danvers es: ' + dato[1])


# vocales(CS)
# invertir_cola(CE)
# palindromo()
# eliminacion(CE)
# invertir_pila_cola(PN)
# ocurrencias(CE)
# i_esimo_cola(CE)
# cola_ordenada()
# rango_negativos(CN)
# personajes_sw()
# dos_colas()
# caracteres(CC)
# procesador()
# Haversine()
# turnos()
# peajes()
# aeropuerto()
# marvel()
