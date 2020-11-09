class Cola():
    '''Crea un objeto cola'''
    def __init__(self):
        self.datos, self.frente, self.final, self.tamanio = [0] * 5, 0, -1, 0


def arribo(C, x):
    '''Inserta un elemento al final de la cola'''
    C.final += 1
    C.datos[C.final] = x
    if(C.final == len(C.datos)-1):
        C.final = -1
    C.tamanio += 1


def atencion(C):
    '''Quita un elemento desde el frente de la cola'''
    x = C.datos[C.frente]
    C.frente += 1
    if(C.frente == len(C.datos)):
        C.frente = 0
    C.tamanio -= 1
    return x


def cola_vacia(C):
    '''Devuelve true si la cola esta vacia'''
    return C.tamanio == 0


def cola_llena(C):
    '''Devuelve true si la cola esta llena'''
    return C.tamanio == len(C.datos)


def tamanio(C):
    '''Tamanio de la cola'''
    return C.tamanio


def barrido(C):
    '''Muestra los elementos de una cola'''
    Caux = Cola()
    while not cola_vacia(C):
        aux = atencion(C)
        print(aux)
        arribo(Caux, aux)
    while not cola_vacia(Caux):
        aux = atencion(Caux)
        arribo(C, aux)


def en_frente(C):
    '''Muestra el dato que esta al frente en la cola'''
    return C.datos[C.frente]


def mover_final(C):
    '''Quita el elemento del frente y lo mueve al final'''
    x = atencion(C)
    arribo(C, x)
    return x
