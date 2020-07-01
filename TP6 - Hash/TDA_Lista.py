class Nodo_Lista():
    '''Crea una variable nodo cola'''
    def __init__(self):
        self.info = None
        self.sig = None


class Lista():
    '''Crea un objeto lista'''
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato, campo=None):
    '''Inserta un dato en una lista'''
    nodo = Nodo_Lista()
    nodo.info = dato
    # si esta vacia o es primer elemento
    if lista.inicio is None or criterio(lista.inicio.info, campo) > criterio(nodo.info, campo):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    # si va al medio o a lo ultimo
    else:
        actual = lista.inicio.sig
        anterior = lista.inicio
        while actual is not None and criterio(actual.info, campo) <= criterio(nodo.info, campo):
            actual = actual.sig
            anterior = anterior.sig
        nodo.sig = actual
        anterior.sig = nodo
    lista.tamanio += 1


def eliminar(lista, clave, campo=None):
    '''Elimina un nodo de una lista'''
    dato = None
    if criterio(lista.inicio.info, campo) == clave:
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    else:
        actual = lista.inicio.sig
        anterior = lista.inicio
        while actual is not None and criterio(actual.info, campo) != clave:
            actual = actual.sig
            anterior = anterior.sig
        if actual is not None:
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamanio -= 1
    return dato


def criterio(dato, campo=None):
    '''Determina el campo por el cual se debe comparar el dato'''
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]


def lista_vacia(lista):
    '''Devuelve True si la lista esta vacia'''
    return lista.inicio is None


def busqueda_lista(lista, buscado, campo=None):
    '''Devuelve el elemento buscado en una lista, si es que se encuentra'''
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != buscado:
        aux = aux.sig
    return aux


def tamanio_lista(lista):
    '''Devuelve el tamanio de una lista'''
    return lista.tamanio


def barrido_lista(lista):
    '''Muestra los elementos de una lista'''
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig
