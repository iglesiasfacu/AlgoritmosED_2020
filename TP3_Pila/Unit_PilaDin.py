from TDA_PilaDin import Pila, apilar, desapilar, pila_vacia, cima
from TDA_PilaDin import pilaint, pilastring, pilatemp, barrido_pila
from TDA_PilaDin import invertir_pila, ordenar_pila, tamanio_pila
from random import randint, choice


print('TP3 - PILA')
print('')

# Declaraciones para ejercicios
vec = [5, 3, 2, 1, 6, 9, 0, 8, 7, 4]

PN = Pila()
pilaint(PN, 10)
print('Pila de numeros enteros')
barrido_pila(PN)
print('')

PC = Pila()
pilastring(PC, 10)
print('Pila de caracteres')
barrido_pila(PC)
print('')

PT = Pila()
pilatemp(PT, 30)
# print('Pila de temperaturas')
# barrido_pila(PT)
# print('')


# EJ 1
def ocurrencias(P):
    '''Numero de ocurrencias de un determinado elemento en una pila'''
    c = 0
    busc = 5
    while not pila_vacia(P):
        x = desapilar(P)
        if x == busc:
            c += 1
    print('El numero', busc, 'se repite', c, ' veces')


# EJ 2
def impares(P):
    '''Elimina numeros impares de una pila'''
    Paux = Pila()
    while not pila_vacia(P):
        x = desapilar(P)
        if x % 2 == 0:
            apilar(Paux, x)
    print('Pila de numeros pares')
    invertir_pila(Paux)
    barrido_pila(Paux)


# EJ 3
def reemplazo(P):
    '''Reemplaza un elemento repetido en una pila por otro dado'''
    Paux = Pila()
    reemplazar = 1999
    busc = 10
    while not pila_vacia(P):
        x = desapilar(P)
        if x == busc:
            x = reemplazar
            apilar(Paux, x)
            invertir_pila(Paux)
        else:
            apilar(Paux, x)
    barrido_pila(Paux)


# EJ 4
'''Ejercicio invertir esta en TDA'''


# EJ 5
def palindromo():
    '''Devuelve True si una palabra es un palindromo'''
    P = Pila()
    cad = 'neuquen'
    print(cad)
    aux = len(cad)
    cad_aux = ''
    for i in range(0, aux):
        c = cad[i]
        apilar(P, c)
    while not pila_vacia(P):
        cad_aux = cad_aux + desapilar(P)
    if cad == cad_aux:
        print(cad_aux)
        print(True)
    else:
        print(cad_aux)
        print(False)


# EJ 6
def inversa():
    '''Invierte una palabra'''
    P = Pila()
    cad = 'python'
    print(cad)
    aux = len(cad)
    cad_aux = ''
    for i in range(0, aux):
        c = cad[i]
        apilar(P, c)
    while not pila_vacia(P):
        cad_aux = cad_aux + desapilar(P)
    print(cad_aux)


# EJ 7
def i_esimo_pila(P):
    '''Elimina un i-esimo elemento que esta debajo de la cima'''
    Paux = Pila()
    pos = 5   # posicion en la pila
    if tamanio_pila(P) > pos+1:
        i = 0
        while i < pos:
            x = desapilar(P)
            apilar(Paux, x)
            i += 1
        elim = desapilar(P)
        print('elemento eliminado: ' + str(elim))
        while not pila_vacia(Paux):
            apilar(P, desapilar(Paux))
        print('Nueva pila')
        barrido_pila(P)
    else:
        print('Se excedio la cantidad de posiciones')


# EJ 8
def cartas():
    '''Pila de cartas de baraja espaniola'''
    P = Pila()
    Pesp = Pila()
    Pbas = Pila()
    Poro = Pila()
    Pcop = Pila()
    palos = ['Espada', 'Basto', 'Oro', 'Copa']
    for i in range(1, 48):
        num = randint(1, 12)
        palo = choice(palos)
        apilar(P, [num, palo])
    while not pila_vacia(P):
        x = desapilar(P)
        if x[1] == 'Espada':
            apilar(Pesp, x)
        elif x[1] == 'Basto':
            apilar(Pbas, x)
        elif x[1] == 'Oro':
            apilar(Poro, x)
        elif x[1] == 'Copa':
            apilar(Pcop, x)
    print('Mazo de espada')
    barrido_pila(Pesp)
    print()
    print('Mazo de basto')
    barrido_pila(Pbas)
    print()
    print('Mazo de oro')
    barrido_pila(Poro)
    print()
    print('Mazo de copa')
    barrido_pila(Pcop)
    print()
    Pesp = ordenar_pila(Pesp)
    print('Mazo de espada ordenados')
    barrido_pila(Pesp)


# EJ 9
def factorial(num):
    '''Pila de factoriales de un numero dado'''
    P = Pila()
    for i in range(1, num+1):
        apilar(P, i)
    print('')
    barrido_pila(P)
    resultado = 1
    while not pila_vacia(P):
        resultado *= desapilar(P)
    print('El factorial de', num, 'es:', resultado)


# EJ 10
def dioses_griegos():
    '''Inserta el nombre de 'Atenea' en una pila de dioses griegos'''
    P = Pila()
    Paux = Pila()
    pos = 2   # posicion en la lista
    dioses = ['Zeus', 'Poseidon', 'Hades', 'Arkantos', 'Apolo', 'Hermes',
              'Ares', 'Persefone', 'Artemisa']
    for i in range(0, 9):
        apilar(P, dioses[i])
    print('Pila de dioses griegos:')
    barrido_pila(P)
    print('')
    if tamanio_pila(P) > pos+1:
        i = 0
        while i < pos:
            x = desapilar(P)
            apilar(Paux, x)
            i += 1
        x = apilar(P, 'ATENEA')
        while not pila_vacia(Paux):
            apilar(P, desapilar(Paux))
        barrido_pila(P)
        print('Se inserto a la diosa "Atenea" en la pila')


# EJ 11
def vocales(P):
    '''Determina cuantas vocales hay en una pila de caracteres'''
    c = 0
    while not pila_vacia(P):
        x = desapilar(P)
        if x == 'A' or x == 'a' or x == 'E' or x == 'e' or x == 'I' or x == 'i' or x == 'O' or x == 'o' or x == 'U' or x == 'u':
            c += 1
    print('Cantidad de vocales:', c)


# EJ 12
def busqueda_sw():
    '''Busqueda personajes de Star Wars'''
    P = Pila()
    Paux = Pila()
    leia = False
    bf = False
    personajes = ['Darth Vader', 'Luke Skywalker', 'Chewbacca', 'Yoda', 'R2D2',
                  'Obi-Wan Keobi', 'Han Solo', 'C3PO', 'Leia Organa',
                  'Jabba el Hutt', 'Boba Fett']
    for i in range(0, 10):
        sw = choice(personajes)
        apilar(P, sw)
    print('Pila de personajes:')
    barrido_pila(P)
    print('')
    while not pila_vacia(P):
        x = desapilar(P)
        if x == 'Leia Organa':
            apilar(Paux, x)
            leia = True
        if x == 'Boba Fett':
            apilar(Paux, x)
            bf = True
    while not pila_vacia(Paux):
        apilar(P, desapilar(Paux))
    if leia:
        print('Leia Organa se encuentra en la pila')
    else:
        print('Leia Organa no esta almacenada')
    if bf:
        print('Boba Fett se encuentra en la pila')
    else:
        print('Boba Fett no esta almacenado')


# EJ 13
def crecientes():
    '''Inserta elementos en una pila de manera creciente'''
    P = Pila()
    Paux = Pila()
    for i in range(0, 10):
        dato = randint(1, 50)
        print(str(dato) + ' agregado')
        if not pila_vacia(P):   # ingresa cuando hay al menos un elemento en P
            while not pila_vacia(P) and cima(P) >= dato:
                apilar(Paux, desapilar(P))
        apilar(P, dato)
        while not pila_vacia(Paux):
            apilar(P, desapilar(Paux))
    print('')
    print('Pila ordenada:')
    barrido_pila(P)


# EJ 14
def quicksort(vec, pri, ult):
    '''Ordenamiento quicksort'''
    P = Pila()
    apilar(P, [pri, ult])
    datos = []
    while not pila_vacia(P):
        datos = desapilar(P)
        i = datos[0]
        j = datos[1] - 1
        pivot = datos[1]
        while i < j:
            while vec[i] <= vec[pivot] and i < j:
                i += 1
            while vec[j] > vec[pivot] and i < j:
                j -= 1
            if i <= j:
                vec[i], vec[j] = vec[j], vec[i]
        if vec[pivot] < vec[i]:
            vec[pivot], vec[i] = vec[i], vec[pivot]
        if datos[0] < j:
            apilar(P, [datos[0], j])
        if datos[1] > i:
            apilar(P, [i+1, datos[1]])


# EJ 15
def interseccion_sw():
    '''Obtiene los personajes que aparecieron en el episodio V y VII
    de la saga Star Wars'''
    P5 = Pila()
    P7 = Pila()
    Paux = Pila()
    ep5 = ['Luke Skywalker', 'Lando Calrissian', 'Yoda', 'Chewbacca',
           'Emperador Palpatine', 'C3PO']
    ep7 = ['Rey', 'Finn', 'Luke Skywalker', 'Kylo Ren', 'Chewbacca',
           'C3PO']
    for i in range(0, len(ep5)):
        apilar(P5, ep5[i])
        apilar(P7, ep7[i])
    print('Episodio V: The empire strikes back')
    barrido_pila(P5)
    print('')
    print('Episodio VII: The force awakens')
    barrido_pila(P7)
    print('')
    while not pila_vacia(P5):
        x = desapilar(P5)
        while not pila_vacia(P7):
            y = desapilar(P7)
            if(x == y):
                print('El personaje ' + str(x) + ' se encuentra en ambos episodios')
            apilar(Paux, y)
        while(not pila_vacia(Paux)):
            y = desapilar(Paux)
            apilar(P7, y)


# EJ 16
def contador():
    '''Algoritmo que muestra datos de un parrafo, tal como sus vocales,
    consonantes, numeros, espacios en blancos y otros simbolos'''
    PV = Pila()
    PC = Pila()
    PO = Pila()
    parrafo = 'El hombre adecuado en el sitio equivocad0 puede cambiar el rumbo del mundo. Despierte, Sr. Freeman. Despierte y mire a su alrededor.'
    numeros = '0123456789'
    vocales = 'aeiouAEIOU'
    consonantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    print(parrafo)
    print('')
    for elemento in parrafo:
        if elemento in vocales:
            apilar(PV, elemento)
        elif elemento in consonantes:
            apilar(PC, elemento)
        else:
            apilar(PO, elemento)

    # A) B) y D)
    voc, cons, otr, espbl, num = 0, 0, 0, 0, 0
    while not pila_vacia(PV):
        desapilar(PV)
        voc += 1
    while not pila_vacia(PC):
        desapilar(PC)
        cons += 1
    while not pila_vacia(PO):
        x = desapilar(PO)
        otr += 1
        if x == ' ':
            espbl += 1
        elif x in numeros:
            num += 1
    print('Cantidad de vocales:', voc)
    print('Cantidad de consonantes:', cons)
    print('Cantidad de otros caracteres:', otr)
    print('Cantidad de espacios en blanco:', espbl)
    print('Cantidad de numeros:', num)

    # C)
    total = voc + cons + otr
    print('Porcentaje de vocales:', round(voc * 100 / total, 2), '%')
    print('Porcentaje de consonantes:', round(cons * 100 / total, 2), '%')

    # E)
    if voc == otr:
        print('Igual cantidad de vocales y otros caracteres')
    else:
        print('Cantidades distintas de vocales y otros caracteres')

    # F)
    LetraZ = False
    while not pila_vacia(PC):
        dato = desapilar(PC)
        if dato == 'z':
            LetraZ = True
    if LetraZ:
        print('Existen letras Z en el parrafo')
    else:
        print('No hay letras Z en el parrafo')


# EJ 17
def piladeobjetos():
    '''Ordena una pila de objetos por su peso'''
    P = Pila()
    objetos = ['monitor', 'teclado', 'raton', 'carpeta',
               'almohadilla', 'sujetapapeles', 'abrochadora', 'cafetera']
    for i in range(0, len(objetos)):
        pes = randint(1, 20)
        apilar(P, [pes, objetos[i]])
    print('Pila de objetos(en kg.)')
    barrido_pila(P)
    print('')
    P = ordenar_pila(P)
    print('Pila de objetos ordenados por peso:')
    barrido_pila(P)


# EJ 18
def peliculas():
    '''Pila de peliculas y sus datos'''
    P = Pila()
    c = 0
    titulo = ['Capitan America', 'Reservoir Dogs', 'Bohemian Rhapsody',
              'Doctor Strange', 'Avengers: Infinity War',
              'Guardianes de la galaxia']
    estudio = ['Marvel Studios', 'Artisan Entertainment', 'GK Films',
               'Marvel Studios', 'Marvel Studios', 'Marvel Studios']
    anio = ['2016', '1992', '2018', '2016', '2018', '2014']
    for i in range(0, 6):
        title, studio, year = titulo[i], estudio[i], anio[i]
        apilar(P, [title, studio, year])
    print('Peliculas:')
    barrido_pila(P)
    print('')
    while not pila_vacia(P):
        dato = desapilar(P)
        if dato[2] == '2014':
            print(str(dato[0]) + ' fue estrenada en 2014')
        if dato[2] == '2018':
            c += 1
        if dato[1] == 'Marvel Studios' and str(dato[2]) == '2018':
            print(str(dato[0]) + ' fue producida por Marvel en el anio 2018')
    print('Se estrenaron', c, 'peliculas en 2018')


# EJ 19
def robot():
    '''Registro de los pasos ida y vuelta que realiza un robot'''
    P = Pila()
    Paux = Pila()
    movimientos = ['norte', 'sur', 'este', 'oeste', 'noreste', 'sureste', 'noroeste', 'suroeste']
    for i in range(1, randint(0, 20)):
        apilar(P, choice(movimientos))
    print('Pasos realizados por el robot:')
    barrido_pila(P)
    while not pila_vacia(P):
        x = desapilar(P)
        if x == 'norte':
            apilar(Paux, 'sur')
        if x == 'sur':
            apilar(Paux, 'norte')
        if x == 'este':
            apilar(Paux, 'oeste')
        if x == 'oeste':
            apilar(Paux, 'este')
        if x == 'norte':
            apilar(Paux, 'sur')
        if x == 'noreste':
            apilar(Paux, 'suroeste')
        if x == 'noroeste':
            apilar(Paux, 'sureste')
        if x == 'sureste':
            apilar(Paux, 'noroeste')
        if x == 'suroeste':
            apilar(Paux, 'noreste')
    while not pila_vacia(Paux):
        apilar(P, desapilar(Paux))
    print('')
    print('Pasos en reversa para volver a punto de partida:')
    barrido_pila(P)
    print('')
    print('El robot realiza', tamanio_pila(P), 'movimientos en ida')
    print('El robot realiza', tamanio_pila(P), 'movimientos en vuelta')
    print('El robot realiza', tamanio_pila(P) * 2, 'movimientos en total')


# EJ 20
def fibonacci_pila(num):
    '''Fibonacci de un numero con pila'''
    P = Pila()
    apilar(P, 0)
    if num == 1:
        apilar(P, 1)
    elif num > 1:
        apilar(P, 1)
        while tamanio_pila(P) <= num:
            dato1 = desapilar(P)
            dato2 = cima(P)
            suma = dato1 + dato2
            apilar(P, dato1)
            apilar(P, suma)
    barrido_pila(P)


# EJ 21
def temperaturas(P):
    '''Pila de temperaturas registradas en un mes, y algunas operaciones
        con ellas'''
    Paux = Pila()
    temp_max = cima(P)
    temp_min = cima(P)
    temp_med = 0
    valores_mayores = 0
    valores_menores = 0
    print('Temperaturas registradas en el mes:')
    barrido_pila(P)
    print('')
    while not pila_vacia(P):
        dato = desapilar(P)
        temp_med += dato
        if dato < temp_min:
            temp_min = dato
        if dato > temp_max:
            temp_max = dato
        apilar(Paux, dato)
    grado = tamanio_pila(Paux)
    temp_med = temp_med / grado
    while not pila_vacia(Paux):
        dato = desapilar(Paux)
        if dato >= temp_med:
            valores_mayores += 1
        else:
            valores_menores += 1
    print('Temperatura minima registrada:', temp_min, '°')
    print('Temperatura maxima registrada:', temp_max, '°')
    print('Rango de temperatura media:', round(temp_med, 2), '°')
    print('Cantidad temperaturas mayores e iguales a la media:', valores_mayores, '°')
    print('Cantidad temperaturas menores a la media:', valores_menores, '°')


# EJ 22
def pila_marvel():
    '''Pila de personajes de Marvel Cinematic Universe'''
    P = Pila()
    P1 = Pila()
    P2 = Pila()
    personaje = ['Iron Man', 'Heimdall', 'J.A.R.V.I.S', 'Doctor Strange',
                 'Groot', 'Thor Odinson', 'Rocket Raccoon', 'Black Widow']
    apariciones = [7, 4, 5, 1, 2, 5, 2, 5]
    for i in range(0, len(personaje)):
        apilar(P, [personaje[i], apariciones[i]])
    print('Pila de personajes y sus apariciones en Marvel')
    barrido_pila(P)
    print('')
    while not pila_vacia(P):
        dato = desapilar(P)
        if dato[0] == 'Black Widow':
            print(str(dato[0]) + ' participo en ' + str(dato[1]) + ' peliculas')
        if dato[1] >= 5:
            print('Participo en 5 o mas peliculas: ' + str([dato[0], dato[1]]))
        cad = dato[0]
        if cad[0] == 'C' or cad[0] == 'D' or cad[0] == 'G':
            print('Personajes que empiezan con la letra C, D o G: ' + dato[0])
        apilar(P1, dato)
    barrido_pila(P1)
    rr, gt = 1, 1
    while not pila_vacia(P1):
        x = desapilar(P1)
        if x[0] == 'Rocket Raccoon':
            print('Rocket Raccoon se encuentra en la posicion', rr)
        else:
            rr += 1
        apilar(P2, x)
        while not pila_vacia(P2):
            y = desapilar(P2)
            if y[0] == 'Groot':
                print('Groot se encuentra en la posicion', gt)
            else:
                gt += 1


# EJERCICIOS

# ocurrencias(PN)
# impares(PN)
# reemplazo(PN)
# print('Pila invertida:')
# invertir_pila(PN)
# palindromo()
# inversa()
# i_esimo_pila(PN)
# cartas()
# factorial(5)
# dioses_griegos()
# vocales(PC)
# busqueda_sw()
# crecientes()
# quicksort(vec, 0, len(vec)-1)
# interseccion_sw()
# contador()
# piladeobjetos()
# peliculas()
# robot()
# fibonacci_pila(10)
# temperaturas(PT)
# pila_marvel()
