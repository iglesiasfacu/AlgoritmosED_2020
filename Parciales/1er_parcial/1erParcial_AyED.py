from TDA_PilaDin import Pila, apilar, desapilar, pila_vacia, barrido_pila
from TDA_ColaDin import Cola, arribo, atencion, cola_vacia, barrido_cola
from TDA_Lista import Lista, insertar, barrido_lista, busqueda_lista
from random import randint, choice
from datetime import time
avengers = ['Iron Man', 'X-Men', 'Dr. Strange', 'Thanos']


# punto 1
def punto_1a(array, pos):
    if pos == len(array):
        return None
    else:
        print(array[pos])
        return punto_1a(array, pos+1)


def punto_1b(array, pos, buscado):
    if pos == len(array):
        return None
    else:
        return punto_1b(array, pos+1, buscado)


# punto 2
class Notificacion():
    def __init__(self, app, hora, msj):
        self.app = app
        self.hora = hora
        self.msj = msj

    def __str__(self):
        return self.app + ' | ' + str(self.hora) + ' | ' + self.msj


def punto_2():
    cola, nueva_cola, cola_ig = Cola(), Cola(), Cola()
    app = ['Facebook', 'Twitter', 'Instagram']
    cmnt = ['Nuevo amigo', 'Python', 'Me gusta', 'Hola!']
    for i in range(10):
        dato = Notificacion(choice(app), time(randint(0, 23), randint(0,59)), choice(cmnt))
        arribo(cola, dato)
    print('APLICACION | HORA | MENSAJE')
    barrido_cola(cola)
    print()
    while not cola_vacia(cola):
        aux = atencion(cola)
        # c
        if aux.app == 'Instagram':
            arribo(cola_ig, aux)
        # b
        if aux.app == 'Twitter' and aux.msj == 'Python':
            print('Notificaciones de Twitter que lleve la palabra Python:')
            print(aux)
        # a
        if aux.app != 'Facebook':
            arribo(nueva_cola, aux)
    print()
    print('Cola de notificaciones sin Facebook')
    barrido_cola(nueva_cola)
    print()
    print('Notificaciones de instagram almacenadas temporalmente')
    barrido_cola(cola_ig)


# punto 3
class Traje():
    def __init__(self, modelo, estado, peli):
        self.modelo = modelo
        self.estado = estado
        self.peli = peli

    def __str__(self):
        return self.modelo + ' | ' + self.estado + ' | ' + self.peli


def punto_3():
    pila, nueva_pila = Pila(), Pila()
    estado = ['Dañado', 'Impecable', 'Destruido']
    modelo = ['Mark XLIV', 'Mark XV', 'Mark I', 'Mark V']
    peli = ['Iron Man', 'Iron Man 2', 'Iron Man 3', 'Avengers']
    for i in range(8):
        dato = Traje(choice(modelo), choice(estado), choice(peli))
        apilar(pila, dato)
    print('MODELO | ESTADO | PELICULA')
    barrido_pila(pila)
    print()

    while not pila_vacia(pila):
        aux = desapilar(pila)
        # a
        if aux.modelo == 'Mark XLIV':
            print('El modelo Mark XLIV fue utilizado en', aux.peli)
        # b
        if aux.estado == 'Dañado':
            print(aux.modelo, 'dañado')
        # d
        if aux.peli == 'Avengers':
            print(aux.modelo, 'apareció en avengers')
        # c
        if aux.estado == 'Destruido':
            print('Se elimino', aux.modelo, 'estado:', aux.estado)
        if aux.estado != 'Destruido':
            apilar(nueva_pila, aux)
    print()
    print('Pila sin trajes dañados')
    barrido_pila(nueva_pila)


# punto 4
def punto_4():
    lista, laux = Lista(), Lista()
    avengers = ['Spider-Man', 'X-Men', 'Dr. Strange', 'Groot']
    insertar(laux, 'Iron Man')
    insertar(laux, 'Groot')
    insertar(laux, 'Falcon')
    insertar(laux, 'Vision')
    for i in range(5):
        insertar(lista, choice(avengers))
    print('Personajes de Avengers:')
    barrido_lista(lista)
    print()
    # barrido_lista(laux)
    # print()
    aux = lista.inicio
    cont = 0
    while aux is not None:
        # a
        if aux.info == 'Spider-Man':
            print('Spider-Man se encuentra en la posicion', cont)
        # b
        if aux.info == 'Dr. Strange':
            aux.info = 'Doctor Strange'
        cont += 1
        aux = aux.sig

    aux = laux.inicio
    while aux is not None:
        # c
        if busqueda_lista(lista, aux.info, 'nombre') is None:
            insertar(lista, aux.info)
        aux = aux.sig
    print()
    print('NUEVA LISTA')
    barrido_lista(lista)


# punto 5
# print('La notacion O determina el orden de complejidad de un algoritmo')
# print('La busqueda secuencial es de O(n)')
# print('n determina la cantidad de elementos a recorrer, ya que la busqueda secuecial los compara uno por uno')


#punto_1a(avengers, 0)
#punto_1b(avengers, 0, 'Iron Man')
#punto_2()
#punto_3()
punto_4()
