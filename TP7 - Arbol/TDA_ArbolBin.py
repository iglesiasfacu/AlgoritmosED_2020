from TDA_ColaDin import Cola, arribo, atencion, cola_vacia

class Nodo_Arbol():
    def __init__(self, info):
        self.info = info 
        self.izq = None
        self.der = None


def insertar_nodo(raiz, dato):
    'Agrega elementos a un arbol'
    if raiz is None:
        raiz = Nodo_Arbol(dato)
    else:
        if dato < raiz.info:
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


def par_impar(raiz, cp, ci):
    'Cuenta la cantidad de numeros pares e impares de un arbol'
    if raiz is not None:
        if raiz.info % 2 == 0:
            cp += 1
        else:
            ci += 1
        cp, ci = par_impar(raiz.izq, cp, ci)
        cp, ci = par_impar(raiz.der, cp, ci)
    return cp, ci


def contar_repetidos(raiz, buscado, cantidad):
    'Determina la cantidad de ocurrencias de un determinado numero'
    if raiz is not None:
        if raiz.info == buscado:
            cantidad += 1
            cantidad = contar_repetidos(raiz.der, buscado, cantidad)
        else:
            cantidad = contar_repetidos(raiz.izq, buscado, cantidad)
    return cantidad


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