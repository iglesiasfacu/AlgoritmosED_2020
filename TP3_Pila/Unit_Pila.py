from TDA_Pila import Pila, apilar, desapilar, pilaint, pilastring, invertir
from TDA_Pila import pila_vacia, pila_llena, tamanio, ordenar_pila
from TDA_Pila import cima, barrido
import random

print('TP3 - PILA')
print('')

# Declaraciones para ejercicios
vec = [5, 3, 2, 1, 6, 9, 0, 8, 7, 4]

PN = Pila()
pilaint(PN)
print('Pila de numeros enteros')
barrido(PN)
print('')

PC = Pila()
pilastring(PC)
print('Pila de caracteres')
barrido(PC)
print('')


# EJ 1
def ocurrencias(P):
    '''Numero de ocurrencias de un determinado elemento en una pila'''
    c = 0
    busc = 10
    while not pila_vacia(P):
        x = desapilar(P)
        if x == busc:
            c += 1
    print('El numero ' + str(busc) + ' se repite ' + str(c) + ' veces')


# EJ 2
def impares(P):
    '''Elimina numeros impares de una pila'''
    P2 = Pila()
    while not pila_vacia(P):
        x = desapilar(P)
        if x % 2 == 0:
            apilar(P2, x)
            invertir(P2)
    barrido(P2)


# EJ 3
def reemplazo(P):
    '''Reemplaza un elemento repetido en una pila por otro dado'''
    P2 = Pila()
    reemplazar = 1999
    busc = 10
    while not pila_vacia(P):
        x = desapilar(P)
        if x == busc:
            x = reemplazar
            apilar(P2, x)
            invertir(P2)
        else:
            apilar(P2, x)
    barrido(P2)


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
def i_esimo(P):
    '''Elimina un i-esimo elemento que esta debajo de la cima'''
    Paux = Pila()
    pos = 5   # posicion en la pila
    if tamanio(P) > pos+1:
        i = 0
        while i < pos:
            x = desapilar(P)
            apilar(Paux, x)
            i += 1
        x = desapilar(P)
        print('elemento eliminado: ' + x)
        while not pila_vacia(Paux):
            x = desapilar(Paux)
            apilar(P, x)


# EJ 8
def cartas():
    '''Pila de cartas de baraja espaniola,
    se debe incrementar el tamanio de la pila a 48 para este ejercicio'''
    P = Pila()
    Pesp = Pila()
    Pbas = Pila()
    Poro = Pila()
    Pcop = Pila()
    palos = ['Espada', 'Basto', 'Oro', 'Copa']
    for i in range(1, 48):
        num = random.randint(1, 12)
        palo = random.choice(palos)
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
    barrido(Pesp)
    print('Mazo de basto')
    barrido(Pbas)
    print('Mazo de oro')
    barrido(Poro)
    print('Mazo de copa')
    barrido(Pcop)
    Pesp = ordenar_pila(Pesp)
    print('Mazo de espada ordenados')
    barrido(Pesp)


# EJ 9
def factorial(num):
    '''Pila de factoriales de un numero dado'''
    P = Pila()
    for i in range(1, num+1):
        apilar(P, i)
    print('')
    barrido(P)
    resultado = 1
    while not pila_vacia(P):
        resultado *= desapilar(P)
    return resultado


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
    barrido(P)
    print('')
    if tamanio(P) > pos+1:
        i = 0
        while i < pos:
            x = desapilar(P)
            apilar(Paux, x)
            i += 1
        x = apilar(P, 'ATENEA')
        while not pila_vacia(Paux):
            apilar(P, desapilar(Paux))
        barrido(P)
        print('Se inserto a la diosa "Atenea" en la posicion: ' + str(pos))


# EJ 11
def vocales(P):
    '''Determina cuantas vocales hay en una pila de caracteres'''
    c = 0
    while not pila_vacia(P):
        x = desapilar(P)
        if x == 'A' or x == 'a' or x == 'E' or x == 'e' or x == 'I' or x == 'i' or x == 'O' or x == 'o' or x == 'U' or x == 'u':
            c += 1
    print('Cantidad de vocales: ' + str(c))


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
        sw = random.choice(personajes)
        apilar(P, sw)
    print('Pila de personajes:')
    barrido(P)
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
    while not pila_llena(P):
        dato = random.randint(1, 50)
        print(str(dato) + ' agregado')
        if not pila_vacia(P):   # ingresa cuando hay al menos un elemento en P
            while not pila_vacia(P) and cima(P) >= dato:
                apilar(Paux, desapilar(P))
        apilar(P, dato)
        while not pila_vacia(Paux):
            apilar(P, desapilar(Paux))
    print('')
    barrido(P)


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
    for i in range(0, 5):
        apilar(P5, ep5[i])
        apilar(P7, ep7[i])
    print('Episodio V: The empire strikes back')
    barrido(P5)
    print('')
    print('Episodio VII: The force awakens')
    barrido(P7)
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
    parrafo = 'Miedo, ira, agresividad, el lado oscuro ellos s0n. Si algun dia rigen tu vida, para siempre tu destino dominaran.'
    numeros = '0123456789'
    vocales = 'aeiouAEIOU'
    consonantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
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
    print('Cantidad de vocales: ' + str(voc))
    print('Cantidad de consonantes: ' + str(cons))
    print('Cantidad de otros caracteres: ' + str(otr))
    print('Cantidad de espacios en blanco: ' + str(espbl))
    print('Cantidad de numeros: ' + str(num))

    # C)
    total = voc + cons + otr
    print('Porcentaje de vocales: ' + str((voc * 100) / total) + '%')
    print('Porcentaje de consonantes: ' + str((cons * 100) / total) + '%')

    # E)
    if voc == otr:
        print('Igual cantidad')
    else:
        print('Cantidades distintas')

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
        pes = random.randint(1, 20)
        apilar(P, [pes, objetos[i]])
    print('Pila de objetos(en kg.)')
    barrido(P)
    print('')
    P = ordenar_pila(P)
    print('Pila de objetos ordenados por peso:')
    barrido(P)


# EJ 18
def peliculas():
    '''Pila de peliculas y sus datos'''
    P = Pila()
    Paux = Pila()
    c = 0
    titulo = ['Capitan America', 'Relatos Salvajes', 'Bohemian Rhapsody',
              'Doctor Strange', 'Avengers: Infinity War',
              'Guardianes de la galaxia']
    estudio = ['Marvel Studios', 'Kramer and Sigman Films', 'GK Films',
               'Marvel Studios', 'Marvel Studios', 'Marvel Studios']
    anio = ['2016', '2014', '2018', '2016', '2018', '2014']
    for i in range(0, 6):
        title, studio, year = titulo[i], estudio[i], anio[i]
        apilar(P, [title, studio, year])
    print('Peliculas:')
    barrido(P)
    print('')
    while not pila_vacia(P):
        dato = desapilar(P)
        if dato[2] == '2014':
            print(str(dato[0]) + ' fue estrenada en 2014')
        if dato[2] == '2018':
            c += 1
        if dato[1] == 'Marvel Studios' and str(dato[2]) == '2018':
            print(str(dato[0]) + ' fue producida por Marvel en el anio 2018')
    print('Se estrenaron ' + str(c) + ' peliculas en 2018')


# EJ 19


# ocurrencias(PN)
# impares(PN)
# reemplazo(PN)
# invertir(PN)
# palindromo()
# inversa()
# i_esimo(PC)
# cartas()
# factorial(10)
# dioses_griegos()
# vocales(PC)
# busqueda_sw()
# crecientes()
# quicksort(vec, 0, len(vec)-1)
# print(vec)
# interseccion_sw()
# contador()
# piladeobjetos()
# peliculas()
