from TDA_ArbolBin import insertar_nodo, eliminar_nodo, inorden, preorden, postorden, por_nivel
from TDA_ArbolBin import busqueda_arbol, arbol_vacio, par_impar, contar_ocurrencias, hijo_der, hijo_izq
from TDA_ArbolBin import inorden_marvel, inorden_villanos, superheroes_c, generar_bosque, cantidad_nodos
from TDA_ArbolBin import busqueda_proximidad, inorden_name
from TDA_Archivo import abrir, cerrar, leer
from random import randint

print('TP7 - ARBOL')
# No van: 2 3 7 10 13 18 22 24
print()


# EJ 1
def arbol_aleatorio():
    arbol = None
    for i in range(0, 10):
        arbol = insertar_nodo(arbol, randint(0, 100))

    # a
    '''
    print('Barrido inorden')
    inorden(arbol)
    print()
    print('Barrido preorden')
    preorden(arbol)
    print()
    print('Barrido postorden')
    postorden(arbol)
    print()'''
    print('Barrido por nivel')
    por_nivel(arbol)
    print()

    # b
    buscado = int(input('Ingrese valor a buscar: '))
    pos = busqueda_arbol(arbol, buscado)
    if pos is not None:
        print('El numero se encuentra en el arbol')
    else:
        print('El numero no existe')
    print()
    
    # c
    eliminado = int(input('Ingrese valor a eliminar: '))
    pos = busqueda_arbol(arbol, eliminado)
    if pos is not None:
        arbol, eliminado = eliminar_nodo(arbol, eliminado)
        print('Se elimino:', eliminado)
    else:
        print('El numero no existe')
    print()
    print('Nuevo arbol')
    por_nivel(arbol)
    print()

    # e
    ocurrencia = int(input('Ingrese valor para determinar sus ocurrencias: '))
    pos = busqueda_arbol(arbol, ocurrencia)
    if pos is not None:
        print('Cantidad de ocurrencias:', contar_ocurrencias(pos, ocurrencia, 0))
    else:
        print('El numero no existe')
    print()
    
    # f
    pares, impares = 0, 0
    pares, impares = par_impar(arbol, pares, impares)
    print('Cantidad de pares:', pares)
    print('Cantidad de impares:', impares)
    print()


# EJ 4
def hijos():
    arbol = None
    for i in range(0, 10):
        arbol = insertar_nodo(arbol, randint(0, 100))
    print('Barrido por nivel')
    por_nivel(arbol)
    print()

    buscado = int(input('Ingrese valor a buscar: '))
    pos = busqueda_arbol(arbol, buscado)
    if pos is not None:
        print('hijos izquierdo')
        hijo_izq(arbol)
        print('hijos derecho')
        hijo_der(arbol)
    else:
        print('El numero no existe')
    print()


# EJ 5
class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre


def saga_marvel():
    arbol = None
    arbol_superheroes = None
    arbol_villanos = None

    # a
    arbol = insertar_nodo(arbol, 'Batman', True)
    arbol = insertar_nodo(arbol, 'Joker', False)
    arbol = insertar_nodo(arbol, 'Iron Man', True)
    arbol = insertar_nodo(arbol, 'Lex Luthor', False)
    arbol = insertar_nodo(arbol, 'Doctor Extraño', True)
    arbol = insertar_nodo(arbol, 'Magneto', False)
    arbol = insertar_nodo(arbol, 'Capitán America', True)
    arbol = insertar_nodo(arbol, 'Thanos', False)
    print('PERSONAJE | BANDO')
    inorden_marvel(arbol)
    print()

    # b
    print('Villanos listados alfabeticamente')
    inorden_villanos(arbol)
    print()

    # c
    print('Superheores que empiecen con "C"')
    superheroes_c(arbol)
    print()

    # e
    busqueda_proximidad(arbol, 'Doctor')
    print()

    # g
    arbol_superheroes, arbol_villanos = generar_bosque(arbol, arbol_superheroes, arbol_villanos)
    print('Arbol Superheroes')
    inorden(arbol_superheroes)
    print()
    print('Arbol Villanos')
    inorden(arbol_villanos)
    print()

    # d
    print('Cantidad de superheroes en el arbol:', cantidad_nodos(arbol_superheroes))
    print()

    # f
    print('Superheroes ordenados de manera descendente')
    postorden(arbol_superheroes)
    print()


# EJ 6
class Jedi():
    def __init__(self, nombre, especie, año_nacimiento, color_sable, ranking, maestro):
        self.nombre = nombre
        self.especie = especie
        self.año_nacimiento = año_nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestro = maestro


def jedis():
    arbol_nombre = None
    arbol_ranking = None
    arbol_especie = None

    jedis = []

    file = abrir('jedis')
    pos = 0
    while pos < len(file):
        jedi = leer(file, pos)
        jedis.append(jedi)
        arbol_nombre = insertar_nodo(arbol_nombre, jedi[0], pos)
        arbol_ranking = insertar_nodo(arbol_ranking, jedi[1], pos)
        arbol_especie = insertar_nodo(arbol_especie , jedi[2], pos)
        pos += 1

    cerrar(file)

    inorden_name(arbol_nombre, file, jedis)

#arbol_aleatorio()
#hijos()
#saga_marvel()
jedis()
