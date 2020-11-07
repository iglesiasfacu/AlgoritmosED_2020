import random
import string


class Pila():
    '''Crea un objeto pila'''
    def __init__(self):
        self.cima = -1
        self.datos = [0] * 30


def apilar(P, x):
    '''Apila un dato en la cima'''
    P.cima += 1
    P.datos[P.cima] = x


def desapilar(P):
    '''Desapila el elemento de la cima'''
    x = P.datos[P.cima]
    P.cima -= 1
    return x


def pila_vacia(P):
    '''Devuelve true si la pila esta vacia'''
    return P.cima == -1


def pila_llena(P):
    '''Devuelve true si la pila esta llena'''
    return P.cima == len(P.datos)-1


def tamanio(P):
    '''Tamanio de la pila'''
    return len(P.datos)


def cima(P):
    '''Elemento que se encuetra en la cima de la pila'''
    return P.datos[P.cima]


def pilaint(P):
    '''Carga una pila con numeros enteros randomicos'''
    while not pila_llena(P):
        apilar(P, random.randint(0, 10))


def pilastring(P):
    '''Carga una pila con letras randomicas'''
    while not pila_llena(P):
        apilar(P, random.choice(string.letters))


def barrido(P):
    '''Muestra los elementos de una pila'''
    Paux = Pila()
    while not pila_vacia(P):
        dato = desapilar(P)
        print(dato)
        apilar(Paux, dato)
    while not pila_vacia(Paux):
        apilar(P, desapilar(Paux))


def invertir(P):
    '''Invierte los elementos de una pila'''
    Paux = Pila()
    while not pila_vacia(P):
        apilar(Paux, desapilar(P))
    barrido(Paux)


def ordenar_pila(P):
    '''Ordena una pila de forma creciente'''
    Paux = Pila()
    while not pila_vacia(P):
        c = 0
        dato = desapilar(P)
        while not pila_vacia(Paux) and cima(Paux) >= dato:
            apilar(P, desapilar(Paux))
            c += 1
        apilar(Paux, dato)
        for i in range(0, c):
            apilar(Paux, desapilar(P))
    return Paux
