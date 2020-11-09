from random import randint, choice


class Nodo_Pila():
    '''Crea una variable nodo pila'''
    def __init__(self):
        self.info = None
        self.sig = None


class Pila():
    '''Crea un objeto pila'''
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, dato):
    '''Apila un dato en la cima'''
    nodo = Nodo_Pila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    '''Desapila el elemento de la cima'''
    dato = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return dato


def pila_vacia(pila):
    '''Devuelve true si la pila esta vacia'''
    return pila.cima is None


def tamanio_pila(pila):
    '''Tamanio de la pila'''
    return pila.tamanio


def cima(pila):
    '''Elemento que se encuetra en la cima de la pila'''
    return pila.cima.info


def pilaint(pila, cant):
    '''Carga una pila con numeros enteros randomicos'''
    for i in range(0, cant):
        apilar(pila, randint(0, 10))


def pilastring(pila, cant):
    '''Carga una pila con letras randomicas'''
    letras = 'abcdefghijklmñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    for i in range(0, cant):
        apilar(pila, choice(letras))


def pilatemp(pila, cant):
    '''Carga temperaturas en una pila'''
    for i in range(0, cant):
        apilar(pila, randint(-20, 10))


def barrido_pila(pila):
    '''Muestra los elementos de una pila'''
    paux = Pila()
    while not pila_vacia(pila):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)
    while not pila_vacia(paux):
        apilar(pila, desapilar(paux))


def invertir_pila(pila):
    '''Invierte los elementos de una pila'''
    paux = Pila()
    while not pila_vacia(pila):
        apilar(paux, desapilar(pila))
    barrido_pila(paux)


def ordenar_pila(pila):
    '''Ordena una pila de forma creciente'''
    paux = Pila()
    while not pila_vacia(pila):
        c = 0
        dato = desapilar(pila)
        while not pila_vacia(paux) and cima(paux) >= dato:
            apilar(pila, desapilar(paux))
            c += 1
        apilar(paux, dato)
        for i in range(0, c):
            apilar(paux, desapilar(pila))
    return paux
