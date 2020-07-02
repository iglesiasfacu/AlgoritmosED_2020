from TDA_Lista import Lista, Nodo_Lista, insertar, eliminar, lista_vacia
from TDA_Lista import barrido_lista, barrido_sublista, tamanio_lista
from TDA_Lista import busqueda_lista, busqueda_lista_vec, listaint, listastring
from random import randint, choice
from datetime import time, date


print('TP5 - LISTA')
print()

# Declaraciones para ejercicios
L1 = Lista()
listaint(L1, 20)
print('Lista de numeros enteros')
barrido_lista(L1)
print()

L2 = Lista()
listaint(L2, 20)
print('Lista de numeros enteros')
barrido_lista(L2)
print()

LS = Lista()
listastring(LS, 20)
print('Lista de letras')
barrido_lista(LS)
print()


# EJ 1
def cont_nodos(l):
    '''Muestra la cantidad de nodos de una lista'''
    c = 0
    aux = l.inicio
    while aux is not None:
        aux = aux.sig
        c += 1
    print('La lista posee',  c, 'nodos')


# EJ 2
def vocales(l):
    '''Elimina las vocales de una lista'''
    dato = None
    dato = eliminar(l, 'A')
    while dato is not None:
        dato = eliminar(l, 'A')
    dato = eliminar(l, 'a')
    while dato is not None:
        dato = eliminar(l, 'a')
    dato = eliminar(l, 'E')
    while dato is not None:
        dato = eliminar(l, 'E')
    dato = eliminar(l, 'e')
    while dato is not None:
        dato = eliminar(l, 'e')
    dato = eliminar(l, 'I')
    while dato is not None:
        dato = eliminar(l, 'I')
    dato = eliminar(l, 'i')
    while dato is not None:
        dato = eliminar(l, 'i')
    dato = eliminar(l, 'O')
    while dato is not None:
        dato = eliminar(l, 'O')
    dato = eliminar(l, 'o')
    while dato is not None:
        dato = eliminar(l, 'o')
    dato = eliminar(l, 'U')
    while dato is not None:
        dato = eliminar(l, 'U')
    dato = eliminar(l, 'u')
    while dato is not None:
        dato = eliminar(l, 'u')
    print('Cola sin vocales')
    barrido_lista(l)


# EJ 3
def parimpar(l):
    '''Dividie una lista dada en dos, una con numeros pares y otra
    con numeros impares'''
    lista_par, lista_impar = Lista(), Lista()
    aux = l.inicio
    while aux is not None:
        if aux.info % 2 == 0:
            insertar(lista_par, aux.info)
        else:
            insertar(lista_impar, aux.info)
        aux = aux.sig
    print('Lista par')
    barrido_lista(lista_par)
    print('Lista impar')
    barrido_lista(lista_impar)


# EJ 4
def i_esimo_lista(l, pos):
    '''Inserta un nodo en la i-esima posicion de una lista'''
    nodo = Nodo_Lista()
    nodo.info = 1999
    aux = l.inicio
    if pos >= 0 and pos <= l.tamanio:
        if pos < l.tamanio:
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
        else:
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo
    barrido_lista(l)


# EJ 5
def es_primo(num):
    '''Devuelve True si un numero es primo'''
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def elimina_primos(l):
    '''Elimina los numeros primos de una lista'''
    aux = l.inicio
    while aux is not None:
        if es_primo(aux.info):
            eliminar(l, aux.info)
        aux = aux.sig
    print('Lista sin primos')
    barrido_lista(l)


# EJ 6
def comics():
    '''Lista de superheroes de comics'''
    comic = Lista()
    nombre = ['Linterna Verde', 'Wolverine', 'Dr. Strange', 'Capitana Marvel',
              'Mujer Maravilla', 'Flash', 'Star-Lord', 'Joker']
    anio = [1940, 1974, 1963, 1968, 1941, 1940, 1976, 1940]
    casacomic = ['DC', 'Marvel', 'DC', 'Marvel', 'DC', 'DC', 'Marvel', 'DC']
    biografia = ['traje : color verde, arma : anillo de poder',
                 'poderosa capacidad de regeneracion, tres garras retractiles en cada mano',
                 'hechicero supremo', 'guerrera extraterrestre de la civilizacion Kree',
                 'princesa guerrera de las Amazonas',
                 'capacidad de correr, moverse y pensar extremadamente rapido',
                 'policia interplanetario', 'criminal mas notable de Gotham City']
    marvel, dc = 0, 0
    for i in range(len(nombre)):
        insertar(comic, [nombre[i], anio[i], casacomic[i], biografia[i]])
    barrido_lista(comic)
    print()
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[0] == 'Linterna Verde':
            eliminar(comic, aux.info)
            print('Se elimino:', dato[0])
        if dato[0] == 'Wolverine':
            print(dato[0], ': aparecio en el anio', str(dato[1]))
        if dato[0] == 'Dr. Strange':
            dato[2] = 'Marvel'
            print(dato)
        if dato[3].find('traje') >= 0 or dato[3].find('armadura') >= 0:
            print(dato[0], 'lleva la palabra armadura/traje en su bio')
        if dato[1] < 1963:
            print('El personaje', dato[0], 'de la casa ',
                  dato[2], 'aparecio antes del anio 1963')
        if dato[0] == 'Capitana Marvel' or dato[0] == 'Mujer Maravilla':
            print(dato[0], 'pertenece a la casa', dato[2])
        if dato[0] == 'Flash' or dato[0] == 'Star-Lord':
            print('Info de', dato[0], ':', dato[3])
        cad = dato[0]
        if cad[0] == 'B' or cad[0] == 'M' or cad[0] == 'S':
            print(dato[0], 'comienza con la letra B, M o S')
        if dato[2] == 'Marvel':
            marvel += 1
        if dato[2] == 'DC':
            dc += 1
        aux = aux.sig
    print('En la casa DC hay', dc, 'personajes')
    print('En la casa Marvel hay', marvel, 'personajes')


# EJ 7
def dos_listas(l1, l2):
    print('Lista 1')
    barrido_lista(l1)
    print('Lista 2')
    barrido_lista(l2)

    # a)
    def lista_concatenada(l1, l2):
        '''Concatena dos listas, una atras de la otra'''
        lconc = Lista()
        lconc = l1
        aux = lconc.inicio
        while aux.sig is not None:
            aux = aux.sig
        aux.sig = l2.inicio
        print('Lista concantenada')
        barrido_lista(lconc)

    # b) y c)
    def lista_sin_repetidos(l1, l2):
        '''Concatena dos listas en una sola omitiendo los datos repetidos'''
        lsr = Lista()
        aux = l1.inicio
        while aux is not None:
            if busqueda_lista(lsr, aux.info) is None:
                insertar(lsr, aux.info)
            aux = aux.sig
        aux = l2.inicio
        while aux is not None:
            if busqueda_lista(lsr, aux.info) is None:
                insertar(lsr, aux.info)
            aux = aux.sig
        print('Lista concatenada sin repetidos')
        barrido_lista(lsr)
        print('Datos repetidos:', tamanio_lista(lsr))

    # d)
    def eliminar_nodos(l1):
        '''Elimina los nodos de una lista'''
        aux = l1.inicio
        while aux is not None:
            eliminar(l1, aux.info)
            print('Se elimino:', aux.info)
            aux = aux.sig

    lista_concatenada(l1, l2)
    lista_sin_repetidos(l1, l2)
    eliminar_nodos(l1)


# EJ 9
class Alumno():
    def __init__(self, apellido, nombre, legajo):
        self.apellido = apellido
        self.nombre = nombre
        self.legajo = legajo

    def __str__(self):
        return self.apellido + ' | ' + self.nombre + ' | ' + str(self.legajo)


class Parcial():
    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return self.materia + ' | ' + str(self.nota) + ' | ' + str(self.fecha)


def lista_alumnos():
    lista = Lista()
    materias = ['Estiramiento', 'Cardio', 'Juego con los pies', 'Retención',
                'Saque abajo', 'Saque arriba', 'Centros', 'Psicología']
    dato = Alumno('Armani', 'Franco', 1)
    insertar(lista, dato, 'apellido')
    dato = Alumno('Lux', 'Germán', 14)
    insertar(lista, dato, 'apellido')
    dato = Alumno('Bologna', 'Enrique', 25)
    insertar(lista, dato, 'apellido')
    dato = Alumno('Centurión', 'Ezequiel', 12)
    insertar(lista, dato, 'apellido')
    for i in range(3):
        datos = Parcial(choice(materias), randint(9, 10), date(2020, 12, 9))
        pos = busqueda_lista(lista, 1, 'legajo')
        insertar(pos.sublista, datos, 'materia')
    for i in range(3):
        datos = Parcial(choice(materias), randint(4, 8), date(2020, 12, 9))
        pos = busqueda_lista(lista, 12, 'legajo')
        insertar(pos.sublista, datos, 'materia')
    for i in range(3):
        datos = Parcial(choice(materias), randint(2, 7), date(2020, 12, 9))
        pos = busqueda_lista(lista, 14, 'legajo')
        insertar(pos.sublista, datos, 'materia')
    for i in range(3):
        datos = Parcial(choice(materias), randint(5, 10), date(2020, 12, 9))
        pos = busqueda_lista(lista, 25, 'legajo')
        insertar(pos.sublista, datos, 'materia')

    # a
    print('APELLIDO | NOMBRE | LEGAJO')
    barrido_lista(lista)
    print()

    # sublista
    aux = lista.inicio
    while aux is not None:
        print('Alumno:', aux.info.apellido + ', ' + aux.info.nombre)
        print('MATERIA | NOTA | FECHA')
        barrido_sublista(aux.sublista)
        aux = aux.sig
        print()

    aux = lista.inicio
    while aux is not None:
        # b
        promedio = 0
        sublista = aux.sublista.inicio
        control = True
        while sublista is not None:
            if sublista.info.nota < 6:
                control = False
            promedio += sublista.info.nota
            sublista = sublista.sig
        if control and tamanio_lista(aux.sublista) > 0:
            print('Aprobo todos los examenes:', aux.info.apellido, aux.info.nombre)
        # e
        if tamanio_lista(aux.sublista) > 0:
            promedio = promedio / tamanio_lista(aux.sublista)
            print(aux.info.apellido, aux.info.nombre, 'promedio:', round(promedio, 2))
        # c
        if(promedio > 8.89):
            print('Promedio mayor a 8.89:', aux.info.apellido, aux.info.nombre, round(promedio, 2))
        # d
        if(aux.info.apellido[0].upper() == 'L'):
            print(aux.info.apellido, aux.info.nombre, 'empieza con la letra L')

        aux = aux.sig


# EJ 10
class Cancion():
    def __init__(self, nombre, artista, duracion, reproducciones):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
        self.reproducciones = reproducciones

    def __str__(self):
        return self.nombre + ' | ' + self.artista + ' | ' + str(self.duracion) + ' | ' + str(self.reproducciones)


def spotify():
    '''Lista de canciones de Spotify'''
    lista = Lista()
    datos = Cancion('Habia una vez...', 'Indio Solari', 4.47, randint(100000, 100000000))
    insertar(lista, datos, 'nombre')
    datos = Cancion('Los Dinosaurios', 'Charly García', 3.28, randint(100000, 100000000))
    insertar(lista, datos, 'nombre')
    datos = Cancion('Crimen', 'Gustavo Cerati', 3.52, randint(100000, 100000000))
    insertar(lista, datos, 'nombre')
    datos = Cancion('Frijolero', 'Molotov', 3.30, randint(100000, 100000000))
    insertar(lista, datos, 'nombre')
    datos = Cancion('Figuración', 'Almendra', 3.33, randint(100000, 100000000))
    insertar(lista, datos, 'nombre')
    print()
    print('NOMBRE | ARTISTA | DURACION | REPRODUCCIONES')
    barrido_lista(lista)
    print()
    larga = 0
    aux = lista.inicio
    while aux is not None:
        if aux.info.duracion > larga:
            info = aux.info
            larga = aux.info.duracion
        if aux.info.artista == 'Artic Monkeys':
            print('La cancion', aux.info.nombre, 'pertenece a Artic Monkeys')
        if len(aux.info.artista.split()) == 1:
            print(aux.info.artista, 'lleva una sola palabra')
        aux = aux.sig
    print()
    print('La cancion mas larga es:', info.nombre)
    print('Artista:', info.artista)
    print('Duracion:', info.duracion)
    print('Reproducciones:', info.reproducciones)


# EJ 11
class Personaje():
    def __init__(self, nombre, altura, edad, genero, especie, planeta_natal, episodios):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta_natal = planeta_natal
        self.episodios = episodios

    def __str__(self):
        return self.nombre + ' | ' + str(self.altura) + ' | ' + str(self.edad) + ' | ' + self.genero + ' | ' + self.especie  + ' | ' + self.planeta_natal + ' | ' + str(self.episodios)


def saga_starwars():
    lista = Lista()
    datos = Personaje('Darth Vader', 2.03, 37, 'M', 'Humano', 'Polis Massa', [3, 4, 5, 6])
    insertar(lista, datos, 'nombre')
    datos = Personaje('Han Solo', 1.85, 66, 'M', 'Humano', 'Corellia', [1, 2, 3, 4, 5, 6, 7, 8])
    insertar(lista, datos, 'nombre')
    datos = Personaje('R2D2', 1.09, 67, 'M', 'Droide', 'Naboo', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    insertar(lista, datos, 'nombre')
    datos = Personaje('C3PO', 1.75, 54, 'M', 'Droide', 'Tatooine', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    insertar(lista, datos, 'nombre')
    datos = Personaje('Yoda', 0.66, 900, 'M', 'Yoda', 'Desconocido', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    insertar(lista, datos, 'nombre')
    datos = Personaje('Rey Skywalker', 1.70, 20, 'F', 'Humano', 'Jakku', [7, 8, 9])
    insertar(lista, datos, 'nombre')
    datos = Personaje('Chewbacca', 2.30, 140, 'M', 'Wookiee', 'Kashyyyk', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    insertar(lista, datos, 'nombre')
    datos = Personaje('Breha Organa', 1.63, 38, 'F', 'Humano', 'Alderaan', [1, 2, 3, 4, 5, 6, 7, 8, 9])
    insertar(lista, datos, 'nombre')
    print('NOMBRE | ALTURA | EDAD | GENERO | ESPECIE | PLANETA NATAL | APARICIONES')
    barrido_lista(lista)
    print()

    # a
    aux = lista.inicio
    while aux is not None:
        if aux.info.genero == 'F':
            print(aux.info.nombre, 'personaje femenino')
        aux = aux.sig
    print()

    # b
    aux = lista.inicio
    while aux is not None:
        if aux.info.especie == 'Droide' and len(aux.info.episodios) >= 6:
            print(aux.info.nombre, 'es un droide')
        aux = aux.sig
    print()

    # c
    aux = lista.inicio
    while aux is not None:
        if aux.info.nombre == 'Darth Vader' or aux.info.nombre == 'Han Solo':
            print('NOMBRE:', aux.info.nombre)
            print('ALTURA:', aux.info.altura)
            print('EDAD:', aux.info.edad)
            print('GENERO:', aux.info.genero)
            print('ESPECIE:', aux.info.especie)
            print('PLANETA NATAL:', aux.info.planeta_natal)
            print('APARICIONES:', aux.info.episodios)
            print()
        aux = aux.sig
    print()

    # d
    aux = lista.inicio
    while aux is not None:
        aux = aux.sig
        if 4 in aux.info.episodios and 5 in aux.info.episodios and 6 in aux.info.episodios and 7 in aux.info.episodios:
            print(aux.info.nombre, 'aparece en al menos un episodio desde el IV al VII')
        aux = aux.sig
    print()

    # e
    mayor = 0
    aux = lista.inicio
    while aux is not None:
        if aux.info.edad >= 850 and aux.info.edad > mayor:
            print(aux.info.nombre, 'tiene mas de 850 anios')
            info = aux.info
            mayor = aux.info.edad
        aux = aux.sig
    print(info.nombre, 'es el personaje mas antiguo, con', info.edad, 'anios')
    print()

    # g
    aux = lista.inicio
    while aux is not None:
        if aux.info.planeta_natal == 'Alderaan':
            print(aux.info.nombre, 'pertenece a Alderaan')
        aux = aux.sig
    print()

    # h
    aux = lista.inicio
    while aux is not None:
        if aux.info.altura < 0.70:
            print(aux.info.nombre, 'mide menos de 70 centimetros')
        aux = aux.sig
    print()

    # i (inc)
    aux = lista.inicio
    while aux is not None:
        if aux.info.nombre == 'Chewbacca':
            print('NOMBRE:', aux.info.nombre)
            print('ALTURA:', aux.info.altura)
            print('EDAD:', aux.info.edad)
            print('GENERO:', aux.info.genero)
            print('ESPECIE:', aux.info.especie)
            print('PLANETA NATAL:', aux.info.planeta_natal)
            print('APARICIONES:', aux.info.episodios)
            print()
        aux = aux.sig
    print()

    # f
    aux = lista.inicio
    while aux is not None:
        if 4 in aux.info.episodios and 5 in aux.info.episodios and 6 in aux.info.episodios and len(aux.info.episodios) == 3:
            elim = eliminar(lista, aux.info)
            print('Eliminado:', elim.nombre)
        aux = aux.sig
    print()


# EJ 12
def anteultimo(l):
    '''Elimina el anteultimo nodo de una lista'''
    aux = l.inicio
    if aux is None or tamanio_lista(l) <= 1:
        supr = eliminar(l, aux.info)
        print('Se elimino:', supr)
        aux = aux.sig
    else:
        actual = l.inicio.sig
        anterior = l.inicio
        while actual is not None:
            actual = actual.sig
            anterior = anterior.sig
        if actual is None:
            supr = eliminar(l, aux.info)
            print('Se elimino:', supr)
    aux = aux.sig
    barrido_lista(l)


# EJ 14
def dados():
    '''Juego de dados'''
    amigos = Lista()
    nombre = ['Marcelo Gallardo', 'Juanfer Quintero', 'Franco Armani',
              'Nacho Scocco', 'Burrito Ortega', 'Enzo Francescoli',
              'Javier Pinola', 'Matias Biscay']
    dato = ['']
    for i in range(len(nombre)):
        dato[0] = nombre[i]
        dato[1] = randint(0, 100)
        insertar(amigos, dato)
    barrido_lista(amigos)


# EJ 15
class Entrenador():
    def __init__(self, entrandor, t_ganados, b_ganadas, b_perdidas):
        self.entrenador = entrandor
        self.t_ganados = t_ganados
        self.b_ganadas = b_ganadas
        self.b_perdidas = b_perdidas

    def __str__(self):
        return self.entrenador + ' | ' + str(self.t_ganados) + ' | ' + str(self.b_ganadas) + ' | ' + str(self.b_perdidas)


class Pokemon():
    def __init__(self, pokemon, nivel, tipo, subtipo):
        self.pokemon = pokemon
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return self.pokemon + ' | ' + str(self.nivel) + ' | ' + self.tipo + ' | ' + self.subtipo


def pokemon():
    lista = Lista()
    pokemon = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Spearow',
               'Dugtrio', 'Primeape', 'Terrakion', 'Tyrantrum', 'Wingull']
    tipo = ['Fuego', 'Agua', 'Electrico', 'Normal', 'Veneno']
    subtipo = ['Tierra', '-', 'Planta', 'Agua', '-', 'Volador']
    dato = Entrenador('Ranchero', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Alevin', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Pescador', randint(0, 10), randint(50, 200), randint(0, 100))
    insertar(lista, dato, 'entrenador')
    for i in range(2):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Ranchero', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(3):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Alevin', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(4):
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Pescador', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    # d
    print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
    barrido_lista(lista)
    print()
    aux = lista.inicio
    # barrido sublista
    while aux is not None:
        print('Entrenador:', aux.info.entrenador)
        print('NOMBRE | NIVEL | TIPO | SUBTIPO')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig

    # a
    aux = lista.inicio
    print('Cantidad de Pokemons de un determinado entrenador')
    entr = input('Ingrese nombre del entrenador: ')
    while aux is not None:
        pos = busqueda_lista(lista, entr, 'entrenador')
        if pos is not None:
            print(aux.info.entrenador, 'posee', tamanio_lista(aux.sublista), 'pokemones')
        else:
            print('El entrenador no existe')
            break
        aux = aux.sig
    print()

    # b
    aux = lista.inicio
    print('Entrenadores que ganaron mas de 3 torneos')
    while aux is not None:
        if aux.info.t_ganados >= 3:
            print(aux.info.entrenador + ':', aux.info.t_ganados, 'torneos')
        aux = aux.sig
    print()

    # c
    aux = lista.inicio
    mg, mn = 0, 0
    while aux is not None:
        if aux.info.t_ganados > mg:
            mg = aux.info.t_ganados
            mas_ganador = aux.info.entrenador
        buscado = busqueda_lista(aux.info.entrenador, mas_ganador, 'entrenador')
        if buscado is not None:
            sublista = aux.sublista.inicio
            while sublista is not None:
                if sublista.info.nivel > mn:
                    mn = sublista.info.nivel
                    mayor_nivel = sublista.info.pokemon
                sublista = sublista.sig
        aux = aux.sig
    print('El entrenador mas ganador es', mas_ganador, 'con', mg, 'torneos')
    print('Su pokemon de mayor nivel es', mayor_nivel, 'con nivel', mn)
    print()

    # e
    aux = lista.inicio
    while aux is not None:
        batallas_totales = aux.info.b_ganadas + aux.info.b_perdidas
        porcentaje_batallas = (aux.info.b_ganadas * 100)/batallas_totales
        if porcentaje_batallas > 79:
            print(aux.info.entrenador, 'tiene un porcentaje de batalladas ganadas mayor a 79%')
        aux = aux.sig
    print()

    # f
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.tipo == 'Fuego' and sublista.info.subtipo == 'Planta':
                print(aux.info.entrenador, 'posee un pokemon tipo fuego y subtipo planta, llamado', sublista.info.pokemon)
            if sublista.info.tipo == 'Agua' and sublista.info.subtipo == 'Volador':
                print(aux.info.entrenador, 'posee un pokemon tipo agua y subtipo volador, llamado', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # g
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        cont_nivel = 0
        while sublista is not None:
            cont_nivel += sublista.info.nivel
            prom_nivel = cont_nivel / tamanio_lista(aux.sublista)
            sublista = sublista.sig
        # round redondea el valor prom_nivel a 2 digitos despues de la coma
        print(aux.info.entrenador + ', promedio de nivel de sus pokemons:', round(prom_nivel, 2))
        aux = aux.sig
    print()

    # h
    aux = lista.inicio
    cont = 0
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        pos = busqueda_lista(aux.sublista, poke, 'pokemon')
        if pos is not None:
            cont += 1
        aux = aux.sig
    print(cont, 'entrenadores tienen al pokemon', poke)
    print()

    # j
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.pokemon == 'Tyrantrum' or sublista.info.pokemon == 'Terrakion' or sublista.info.pokemon == 'Wingull':
                print(aux.info.entrenador, 'tiene al pokemon', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # k
    aux = lista.inicio
    print('Busca un entrenador y sus pokemones')
    entr = input('Ingrese nombre de entrenador a buscar: ')
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if entr == aux.info.entrenador and poke == sublista.info.pokemon:
                print()
                print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
                print(aux.info)
                print()
                print('NOMBRE | NIVEL | TIPO | SUBTIPO')
                print(sublista.info)
            sublista = sublista.sig
        aux = aux.sig


# EJ 16
def proyecto_software():
    '''Actividades de un proyecto de software'''
    lista, en_tiempo, fuera_tiempo = Lista(), Lista(), Lista()
    persona = ['Gerardo', 'Martina', 'Lucia', 'Geovanni', 'Jessica', 'Laura']
    prom_tareas, costo_total = 0, 0
    df = ''
    for i in range(5):
        costo = randint(0, 50000)
        tde = randint(1, 10)
        fdi = [2020, randint(1, 12), randint(1, 31)]
        fdfest = [2020, randint(1, 12), randint(1, 31)]
        fdfefc = [2020, randint(1, 12), randint(1, 31)]
        pac = choice(persona)
        tarea = [costo, tde, fdi, fdfest, fdfefc, pac]
        insertar(lista, tarea)
    print('Costo | Tiempo de ejec. | Fecha de inicio | Fecha de fin estimada | Fecha de fin efectiva | Persona a cargo')
    barrido_lista(lista)
    print()
    aux = lista.inicio
    while aux is not None:
        dato = aux.info
        # a
        prom_tareas += dato[1]
        # b
        costo_total += dato[0]
        # c
        if dato[5]:
            print()
            print('Persona:', dato[5])
            print('Actividades que realiza:')
            print('Coste de la actividad:', dato[0], 'ARS')
            print('Tiempo de ejecucion:', dato[1])
        # d
        if dato[2][1] > 5 and dato[3][1] > 5:
            df = [dato[0], dato[1], dato[2], dato[3]]
        # e
        if dato[3][0] > dato[4][0] and dato[3][1] > dato[4][1]:
            insertar(fuera_tiempo, [dato[0], dato[1], dato[5]])
        else:
            insertar(en_tiempo, [dato[0], dato[1], dato[5]])
        aux = aux.sig
    prom_tareas = prom_tareas / tamanio_lista(lista)
    print()
    print('Tiempo promedio de tareas', prom_tareas)
    print('Costo total del proyecto', costo_total, 'ARS')
    print('Tareas a realizar entre dos fechas dadas(a partir de Junio):')
    print(df)
    print()
    print('Tareas finalizadas en tiempo estipulado')
    barrido_lista(en_tiempo)
    print()
    if not lista_vacia(fuera_tiempo):
        print('Tareas fuera de tiempo')
        barrido_lista(fuera_tiempo)
    else:
        print('No hay tareas fuera de tiempo')


# EJ 17
def aeropuerto_creta():
    '''Vuelos del aeropuerto de Heraklion en Creta'''
    vuelos, vuelos_destinos, turista_disponible = Lista(), Lista(), Lista()
    monto_vuelos, vuelos_junio, lista_aux = Lista(), Lista(), Lista()
    nom_empr = ['Qatar Airways', 'Singapore Airlines', 'Fly Emirates',
                'Iberia', 'Turkish Airlines']
    ciudad_dest = ['Atenas', 'Miconos', 'Rodas', 'Tailandia', 'Nicosia',
                   'Ulan Bator', 'Yakarta', 'El Brillante']
    estado = ['Ocupado', 'Desocupado']
    clase = ['Primera Clase', 'Turista']
    nro = 1
    for i in range(len(nom_empr)):
        empresa = nom_empr[i]
        num_vuelo = randint(1000, 10000)
        asientos = randint(40, 80)
        fds = [2020, randint(1, 12), randint(1, 31)]
        destino = choice(ciudad_dest)
        kms_vuelo = randint(400, 5000)
        datos_avion = [empresa, num_vuelo, asientos, fds, destino, kms_vuelo]
        insertar(vuelos, datos_avion)
        for j in range(asientos):
            as_avion = busqueda_lista_vec(vuelos, empresa, 0)
            if as_avion is not None:
                as_nro = nro
                nro += 1
                as_estado = choice(estado)
                as_clase = choice(clase)
                datos_asientos = [as_nro, as_estado, as_clase]
                insertar(as_avion.sublista, datos_asientos)
    print('EMPRESA | NUM. VUELO | ASIENTOS | FECHA DE SALIDA | DESTINO | KMS. VUELO')
    barrido_lista(vuelos)
    print()
    aux = vuelos.inicio
    km = aux.info[5]
    monto_turista, monto_pc = 0, 0
    while aux is not None:
        print('Datos de asientos:', aux.info[0])
        print('Cantidad de asientos:', tamanio_lista(aux.sublista))
        # print('ASIENTOS TOTALES | ESTADO | CLASE')
        # barrido_sublista(aux.sublista)
        print()
        # a
        if aux.info[4] == 'Atenas' or aux.info[4] == 'Miconos' or aux.info[4] == 'Rodas':
            insertar(vuelos_destinos, aux.info)
        # d
        # vuelos disponibles desde junio en adelante
        if aux.info[3][1] >= 6:
            insertar(vuelos_junio, aux.info)
        # b
        avion = aux.sublista.inicio
        while avion is not None:
            if avion.info[1] == 'Desocupado' and avion.info[2] == 'Turista':
                insertar(turista_disponible, aux.info)
                break
        # c
            if avion.info[1] == 'Ocupado':
                if avion.info[2] == 'Turista':
                    monto_turista += (75*km)
                else:
                    monto_pc += (203*km)
            avion = avion.sig
        montos = [aux.info[0], aux.info[1], monto_turista, monto_pc]
        insertar(monto_vuelos, montos)
        aux = aux.sig
    # e
    nro_vuelo = int(input('Ingrese el numero de vuelo: '))
    nro_as = int(input('Ingrese el numero del asiento: '))
    clase = input('Ingrese la clase: ')
    estado_asiento = 'Ocupado'
    datos_venta_pasaje = [nro_as, estado_asiento, clase]
    pos = busqueda_lista_vec(vuelos, nro_vuelo, 1)
    if pos is None:
        print('El vuelo no existe')
    else:
        aux = vuelos.inicio
        insertar(as_avion.sublista, datos_venta_pasaje)
        print('**** Se ha vendido el pasaje ****')
        print('N°Vuelo | N°Asiento | Clase')
        print(datos_venta_pasaje)
        print()
        aux = aux.sig
    # f
    eliminar_vuelo = int(input('Ingrese el numero de vuelo que desea eliminar: '))
    pos = busqueda_lista_vec(vuelos, eliminar_vuelo, 1)
    if pos is None:
        print('El vuelo no existe')
    else:
        aux = vuelos.inicio
        eliminar(vuelos, eliminar_vuelo, 1)
        lista_aux = as_avion.sublista
        print('Vuelo eliminado')
        aux = aux.sig
    print()
    print('Vuelos con destino a Atenas, Miconos o Rodas:')
    barrido_lista(vuelos_destinos)
    print()
    print('Vuelos con asientos clase turista disponible:')
    barrido_lista(turista_disponible)
    print()
    print('Recaudado por cada vuelo, turista $75 x km y primera clase $203 x km')
    print('EMPRESA | NUM. VUELO | $ TURISTA | $ PRIMERA CLASE')
    barrido_lista(monto_vuelos)
    print()
    print('Vuelos disponibles entre junio y diciembre:')
    barrido_lista(vuelos_junio)
    print()
    print('Se elimino el vuelo', eliminar_vuelo)
    print('Pasajeros del vuelo eliminado:')
    barrido_lista(lista_aux)
    print()


# EJ 18
class Usuario():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Commit():
    def __init__(self, archivo, timestamp, mensaje, cant_lineas):
        self.archivo = archivo
        self.timestamp = timestamp
        self.mensaje = mensaje
        self.cant_lineas = cant_lineas

    def __str__(self):
        return self.archivo + ' | ' + self.timestamp + ' | ' + self.mensaje + ' | ' + str(self.cant_lineas)


def github():
    repositorio = Lista()
    user = Usuario('elchiche32')
    insertar(repositorio, user, 'nombre')
    user = Usuario('taunus99')
    insertar(repositorio, user, 'nombre')
    user = Usuario('rickyfort')
    insertar(repositorio, user, 'nombre')
    user = Usuario('oktubr3')
    insertar(repositorio, user, 'nombre')
    commit = Commit('test.py', '11-11-20 19:00', 'testeo de la app', 46)
    pos = busqueda_lista(repositorio, 'elchiche32', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('data.py', '11-11-20 19:00', 'correccion error', 120)
    pos = busqueda_lista(repositorio, 'elchiche32', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('object.java', '11-11-20 19:00', 'modelado del objeto', 0)
    pos = busqueda_lista(repositorio, 'taunus99', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('app.py', '11-11-20 19:00', 'basta chicos', -34)
    pos = busqueda_lista(repositorio, 'rickyfort', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('front.html', '11-11-20 19:00', 'update', 87)
    pos = busqueda_lista(repositorio, 'oktubr3', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('vista.css', '11-11-20 19:00', 'update', -2)
    pos = busqueda_lista(repositorio, 'oktubr3', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    # barrido lista
    print('COLABORADORES')
    barrido_lista(repositorio)
    print()
    aux = repositorio.inicio
    # barrido sublista
    while aux is not None:
        print('Colaborador:', aux.info)
        print('ARCHIVO | TIMESTAMP | COMENTARIO | LINEAS MODIFICADAS')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig

    # a
    aux = repositorio.inicio
    mayor_commit = 0
    while aux is not None:
        if tamanio_lista(aux.sublista) > mayor_commit:
            mayor_commit = tamanio_lista(aux.sublista)
        aux = aux.sig
    aux = repositorio.inicio
    while aux is not None:
        if tamanio_lista(aux.sublista) == mayor_commit:
            print('Colaborador con mayor cantidad de commits:', aux.info)
            print('Cantidad de commits:', mayor_commit)
        aux = aux.sig
    print()

    # b
    mayor = 0
    usuario_mayor = ''
    aux = repositorio.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        mayor_aux = 0
        while sublista is not None:
            mayor_aux += sublista.info.cant_lineas
            sublista = sublista.sig
        if mayor_aux > mayor:
            mayor = mayor_aux
            usuario_mayor = aux.info.nombre
        aux = aux.sig
    print('El usuario', usuario_mayor, 'agrego la mayor cantidad de lineas:', mayor)

    menor = 0
    usuario_menor = ''
    aux = repositorio.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        menor_aux = 0
        while sublista is not None:
            menor_aux += sublista.info.cant_lineas
            sublista = sublista.sig
        if menor_aux < menor:
            menor = menor_aux
            usuario_menor = aux.info.nombre
        aux = aux.sig
    print('El usuario', usuario_menor, 'elimino la mayor cantidad de lineas:', menor)

    # c
    aux = repositorio.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista, 'test.py', 'archivo')
        if pos is not None:
            print('El usuario', aux.info, 'realizo cambios en test.py')
        aux = aux.sig

    # d
    aux = repositorio.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista, 0, 'cant_lineas')
        if pos is not None:
            print('El usuario', aux.info, 'realizo un commit con 0 lineas')
        aux = aux.sig
    print()

    # e
    aux = repositorio.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista, 'app.py', 'archivo')
        if pos is not None:
            print('El usuario', aux.info, 'realizo cambios en app.py')
            print('ARCHIVO | TIMESTAMP | COMENTARIO | LINEAS MODIFICADAS')
            barrido_sublista(aux.sublista)
        aux = aux.sig


# EJ 19
class Ventas_Naves():
    def __init__(self, codigo, producto, precio, reciclado, cliente):
        self.codigo = codigo
        self.producto = producto
        self.precio = precio
        self.reciclado = reciclado
        self.cliente = cliente

    def __str__(self):
        return str(self.codigo) + ' ; ' + self.producto + ' ; ' + str(self.precio) + ' ; ' + str(self.reciclado) + ' ; ' + self.cliente


def astillero():
    lista, lista_clientes, lista_anonimos = Lista(), Lista(), Lista()
    nombre_clientes = Lista()
    producto = ['Caza TIE', 'Destructor Estelar', 'Transporte Acorazado AT-AT',
                'Transporte de Exploración AT-ST', 'Ejecutor Táctico AT-TE']
    reciclado = [True, False]
    comprador = ['Darth Vader', 'Lando Calrissian', 'Boba Fett',
                 'Flia. Organa', 'Han Solo', 'Desconocido']
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    venta = Ventas_Naves(randint(1, 1000), choice(producto), randint(1000, 100000), choice(reciclado), choice(comprador))
    insertar(lista, venta, 'codigo')
    # a
    print('LISTA PRINCIPAL')
    print('CODIGO | PRODUCTO | PRECIO | RECIADO(V/F) | COMPRADOR')
    barrido_lista(lista)
    print()

    # b
    aux = lista.inicio
    while aux is not None:
        if aux.info.cliente == 'Desconocido':
            insertar(lista_anonimos, aux.info, 'codigo')
        else:
            insertar(lista_clientes, aux.info, 'codigo')
        aux = aux.sig
    print('Ventas a clientes habituales')
    barrido_lista(lista_clientes)
    print()
    print('Ventas a clientes desconocidos')
    if not lista_vacia(lista_anonimos):
        barrido_lista(lista_anonimos)
    else:
        print('No hay compradores anonimos')
    print()

    # c pendiente

    # d
    aux = lista.inicio
    total_ingresos = 0
    while aux is not None:
        total_ingresos += aux.info.precio
        aux = aux.sig
    print('Cantidad de unidades vendidas:', tamanio_lista(lista))
    print('Ingresos totales:', total_ingresos, 'creditos galácticos')
    print()

    # e
    aux = lista.inicio
    while aux is not None:
        nombre = aux.info.cliente
        pos = busqueda_lista(nombre_clientes, nombre)
        if pos is None:
            insertar(nombre_clientes, nombre)
        aux = aux.sig
    print('Listado de clientes:')
    barrido_lista(nombre_clientes)
    print()

    # f
    aux = lista.inicio
    print('Compras realizadas por Darth Vader')
    while aux is not None:
        if aux.info.cliente == 'Darth Vader':
            print(aux.info)
        aux = aux.sig
    print()

    # g
    aux = lista.inicio
    print('Descuento del 15% a los clientes que compraron naves con partes recicladas')
    while aux is not None:
        if aux.info.reciclado is True:
            descuento = aux.info.precio * 15 / 100
            print('Al cliente', aux.info.cliente, 'se le deben reintegrar', descuento, 'creditos')
        aux = aux.sig
    print()

    # h
    aux = lista.inicio
    ingresos_at = 0
    while aux is not None:
        pos = busqueda_lista(lista, 'AT', 'producto')
        if pos is None:
            ingresos_at += aux.info.precio
        aux = aux.sig
    print('La venta de naves modelo AT generó', ingresos_at, 'creditos')


# EJ 20
class Estacion():
    def __init__(self, estacion, pais, latitud, longitud, altitud):
        self.estacion = estacion
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def __str__(self):
        return self.estacion + '  |  ' + self.pais + '  |  ' + str(self.latitud) + '  |  ' + str(self.longitud) + '  |  ' + str(self.altitud)


class Medicion():
    def __init__(self, temperatura, presion, humedad, estado, fecha, hora):
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.estado = estado
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return str(self.temperatura) + '  |  ' + str(self.presion) + '  |  ' + str(self.humedad) + ' | ' + self.estado + ' | ' + str(self.fecha) + ' | ' + str(self.hora)


def empresa_meteorologica():
    lista = Lista()
    paises = ['Myanmar', 'Laos', 'Vietnam', 'Indonesia', 'Malasia',
              'Singapur', 'Brunei', 'Sri Lanka']
    estado = ['soleado', 'nublado', 'lloviendo', 'nevando', 'tormenta eléctrica', 'huracanes']
    datos = Estacion('Invierno', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    datos = Estacion('Otoño', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    datos = Estacion('Primavera', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    datos = Estacion('Verano', choice(paises), randint(-90, 90), randint(-180, 180), randint(0, 2000))
    insertar(lista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(0, 10), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Invierno', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(10, 25), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Otoño', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(15, 30), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Primavera', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    for i in range(1):
        datos = Medicion(randint(20, 40), randint(700, 800), randint(0, 100), choice(estado), date(2020, randint(1, 12), randint(1, 30)), time((randint(00, 23)), (randint(00, 59))))
        pos = busqueda_lista(lista, 'Verano', 'estacion')
        insertar(pos.sublista, datos, 'estacion')
    # a
    print(' ESTACION | PAIS | LATITUD | LONGUITD | ALTITUD')
    barrido_lista(lista)
    print()

    # b
    aux = lista.inicio
    while aux is not None:
        print('Estacion:', aux.info.estacion)
        print('Pais:', aux.info.pais)
        print('TEMP. | PRESION | HUMEDAD | ESTADO |   FECHA   |   HORA   ')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig
    print()

    # c
    aux = lista.inicio
    prom_temperatura = 0
    prom_humedad = 0
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            prom_temperatura += sublista.info.temperatura
            prom_humedad += sublista.info.humedad
            sublista = sublista.sig
        aux = aux.sig
    print('Promedio de temperatura:', prom_temperatura / tamanio_lista(lista))
    print('Promedio de humedad:', prom_humedad / tamanio_lista(lista))
    print()

    # d
    aux = lista.inicio
    while aux is not None:
        lluvia = busqueda_lista(aux.sublista, 'lloviendo', 'estado')
        if lluvia is not None:
            print('En', aux.info.pais, 'esta lloviendo')
        nieve = busqueda_lista(aux.sublista, 'nevando', 'estado')
        if nieve is not None:
            print('En', aux.info.pais, 'esta nevando')
        aux = aux.sig
    print()

    # e
    aux = lista.inicio
    while aux is not None:
        tormenta = busqueda_lista(aux.sublista, 'tormenta eléctrica', 'estado')
        if tormenta is not None:
            print(' ESTACION | PAIS | LATITUD | LONGUITD | ALTITUD')
            print(aux.info, ', se registraron tormentas eléctricas')
            print()
        huracan = busqueda_lista(aux.sublista, 'huracanes', 'estado')
        if huracan is not None:
            print(' ESTACION | PAIS | LATITUD | LONGUITD | ALTITUD')
            print(aux.info, ' , se registraron huracanes')
            print()
        aux = aux.sig
    print()


# EJ 21
class Peliculas():
    def __init__(self, nombre, valoracion, año_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.año_estreno = año_estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return self.nombre + '  |  ' + str(self.valoracion) + '  |  ' + str(self.año_estreno) + ' | ' + str(self.recaudacion)


def lista_peliculas():
    lista, lista_ranking = Lista(), Lista()
    datos = Peliculas('El Padrino', randint(0, 10), 1972, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Goodfellas', randint(0, 10), 1990, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('El Irlandés', randint(0, 10), 2019, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Casino', randint(0, 10), 1995, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Sicario', randint(0, 10), 2015, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    print('   NOMBRE   |  VALORACION(0-10) |  AÑO DE ESTRENO | RECAUDACION(USD)')
    barrido_lista(lista)
    print()

    # a
    aux = lista.inicio
    buscado = int(input('Ingrese un año de estreno: '))
    while aux is not None:
        if buscado == aux.info.año_estreno:
            print(aux.info.nombre, 'se estreno en el año', buscado)
        aux = aux.sig
    print()

    # b
    mas_recuadacion = 0
    mayor_peli = ''
    aux = lista.inicio
    while aux is not None:
        if aux.info.recaudacion > mas_recuadacion:
            mayor_peli = aux.info
        aux = aux.sig
    print('Pelicula que mas recaudo y sus datos')
    print(' NOMBRE  | VALORACION(0-10)| AÑO DE ESTRENO | RECAUDACION(USD)')
    print(mayor_peli)
    print()

    # c
    aux = lista.inicio
    mas_valor = 0
    while aux is not None:
        if aux.info.valoracion > mas_valor:
            mas_valor = aux.info.valoracion
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if aux.info.valoracion == mas_valor:
            print(aux.info.nombre, 'tiene la valoracion mas alta,', mas_valor, 'puntos')
        aux = aux.sig
    print()

    # d
    print('Ingrese criterio de orden: ')
    print('* nombre')
    print('* valoracion')
    print('* año_estreno')
    print('* recaudacion')
    criterio = input()
    aux = lista.inicio
    while aux is not None:
        insertar(lista_ranking, aux.info, criterio)
        aux = aux.sig
    print()
    if criterio == 'nombre':
        print('Lista ordenada por nombre:')
        barrido_lista(lista_ranking)
    elif criterio == 'valoracion':
        print('Lista ordenada por valoracion:')
        barrido_lista(lista_ranking)
    elif criterio == 'año_estreno':
        print('Lista ordenada por año de estreno:')
        barrido_lista(lista_ranking)
    elif criterio == 'recaudacion':
        print('Lista ordenada por recaudacion:')
        barrido_lista(lista_ranking)


# cont_nodos(L1)
# vocales(LS)
# parimpar(L1)
# i_esimo_lista(L1, 5)
# elimina_primos(L1)
# comics()
# dos_listas(L1, L2)
# lista_alumnos()
# spotify()
# saga_starwars()
# anteultimo(L1)
pokemon()
# proyecto_software()
# aeropuerto_creta()
# github()
# astillero()
# empresa_meteorologica()
# lista_peliculas()
