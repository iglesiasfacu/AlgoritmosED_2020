from TDA_ColaDin import Cola, arribo, atencion, cola_vacia
from TDA_Archivo import abrir, leer
# No van: 2 3 7 10 13 18 22 24

class Nodo_Arbol():
    def __init__(self, info, nrr=None):
        self.info = info
        self.izq = None
        self.der = None
        self.nrr = nrr
        self.altura = 0

class Nodo_ArbolHuffman(): 
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor


def insertar_nodo(raiz, dato, nrr=None):
    'Agrega elementos a un arbol'
    if raiz is None:
        raiz = Nodo_Arbol(dato, nrr)
    else:
        if raiz.info > dato:
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    return raiz


def insertar_nodo_morse(raiz, dato):
    if raiz is None:
        raiz = Nodo_Arbol(dato)
    else:
        if raiz.info[0] > dato[0]:
            raiz.izq = insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = insertar_nodo(raiz.der, dato)
    return raiz


def busqueda_arbol(raiz, buscado):
    'Busca un elemento en un arbol'
    if raiz is not None:
        if raiz.info == buscado:
            return raiz
        else:
            if buscado < raiz.info:
                return busqueda_arbol(raiz.izq, buscado)
            else:
                return busqueda_arbol(raiz.der, buscado)


def busqueda_proximidad(raiz, buscado):
    if raiz is not None:
        if raiz.info[0:len(buscado)] == buscado:
            print('Se encontro:', raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)


def reemplazar(raiz):
    aux = None
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    return raiz, aux


def eliminar_nodo(raiz, clave):
    'Elimina un elemento de un arbol'
    x = None   # x elemento a eliminar
    if raiz is not None:
        if clave < raiz.info:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave > raiz.info:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                x = raiz.info
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x


def arbol_vacio(raiz):
    'Devuelve True si el arbol esta vacio'
    return raiz is None


def inorden(raiz):
    'Barrido de menor a mayor'
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def preorden(raiz):
    'Barrido que muestra la raiz en primer lugar'
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def por_nivel(raiz):
    'Barrido por nivel'
    cola = Cola()
    arribo(cola, raiz)
    while not cola_vacia(cola):
        nodo = atencion(cola)
        print(nodo.info)
        if nodo.izq is not None:
            arribo(cola, nodo.izq)
        if nodo.der is not None:
            arribo(cola, nodo.der)


def generar_bosque(arbol, arbol_superheroes, arbol_villanos):
    if arbol is not None:
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.izq, arbol_superheroes, arbol_villanos)
        if arbol.nrr is True:
            arbol_superheroes = insertar_nodo(arbol_superheroes, arbol.info)
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, arbol.info)
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.der, arbol_superheroes, arbol_villanos)
    return arbol_superheroes, arbol_villanos


def cantidad_nodos(raiz, cont=0):
    'Devuelve la cantidad de nodos de un arbol'
    if raiz is not None:
        cont = cantidad_nodos(raiz.izq, cont)
        cont += 1
        cont = cantidad_nodos(raiz.der, cont)
    return cont


def cantidad_hojas(raiz, cont=0):
    'Devuelve la cantidad de hojas de un arbol'
    if raiz is not None:
        if raiz.izq is None and raiz.der is None:
            cont += 1
            print(raiz.info, 'es una hoja')
        cont = cantidad_hojas(raiz.izq, cont)
        cont = cantidad_hojas(raiz.der, cont)
    return cont


def altura(raiz):
    '''Devuelve la altura de un nodo'''
    if raiz is None:
        return -1
    else:
        return raiz.altura


def actualizar_altura(raiz):
    if raiz is not None:
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def hijo_der(arbol):
    if arbol.der is None:
        print(arbol.der)
    else:
        print(arbol.der.info)


def hijo_izq(arbol):
    if arbol.izq is None:
        print(arbol.izq)
    else:
        print(arbol.izq.info)


def padre(raiz, buscado):
    '''Determina el padre de un nodo'''
    if raiz is not None:
        if raiz.der is not None and raiz.der.info == buscado or raiz.izq is not None and raiz.izq.info == buscado:
            print('El padre de buscado es', raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def nodo_minimo(raiz):
    '''Obtiene el nodo minimo de un arbol'''
    if raiz.izq is not None:
        raiz = nodo_minimo(raiz.izq)
    return raiz


def nodo_maximo(raiz):
    '''Obtiene el nodo maximo de un arbol'''
    if raiz.der is not None:
        raiz = nodo_maximo(raiz.der)
    return raiz


def decodificar_morse(raiz, cadena):
    cadena_deco = ''
    raiz_aux = raiz
    pos = 0
    while pos < len(cadena):
        if cadena[pos] == '.':
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
    if raiz_aux is not None:
        cadena_deco += raiz_aux.info[1]
    raiz_aux = raiz
    return cadena_deco


def descifrar_morse(arbol, morse, mensaje):
    for palabra in morse.split('/'):
        x = ''
        for letra in palabra.split(' '):
            x += decodificar_morse(arbol, letra)
        mensaje += x
        mensaje += ' '
    return mensaje


'''
arbol = None
arbol = insertar_nodo(arbol, 5)
arbol = insertar_nodo(arbol, 3)
arbol = insertar_nodo(arbol, 4)
arbol = insertar_nodo(arbol, 7)
arbol = insertar_nodo(arbol, 9)
arbol = insertar_nodo(arbol, 0)
arbol = insertar_nodo(arbol, 1)
arbol = insertar_nodo(arbol, 6)

arbol, dato = eliminar_nodo(arbol, 5)
inorden(arbol)'''