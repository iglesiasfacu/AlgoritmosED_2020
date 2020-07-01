from TDA_Hash import crear_tabla, agregar_ta, agregar_tc, quitar_ta, quitar_tc
from TDA_Hash import buscar_tc, buscar_ta, cantidad_ta, cantidad_tc
from TDA_Hash import hash_division, hash_diccionario, bernstein
from TDA_Hash import barrido_ta, barrido_tc
from TDA_Hash import hash_division_guiatel, hash_division_catedra, bernstein_contactos
from TDA_Hash import bernstein_troopers, hash_division_troopers, bernstein_star_wars
from TDA_Hash import bernstein_pokemones
from TDA_Lista import barrido_lista
from random import randint, choice


print('TP6 - HASH')
print()


# EJ 1
class Palabra():
    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado

    def __str__(self):
        return self.palabra + ', ' + self.significado


def diccionario():
    tabla = crear_tabla(26)

    # a
    palabra = Palabra('Hola', 'Es un saludo')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    palabra = Palabra('Hielo', 'Agua congelada')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    palabra = Palabra('Arbol', 'Parte de la naturaleza')
    agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
    barrido_ta(tabla)
    print()

    # b
    pos = buscar_ta(tabla, hash_diccionario, Palabra('Hola', ''), 'palabra')
    if(pos is not None):
        print('Palabra', pos.info.palabra, 'significado', pos.info.significado)
    print()

    # c
    print('Elemento eliminado:', quitar_ta(tabla, hash_diccionario, Palabra('Hielo', ''), 'palabra'))
    barrido_ta(tabla)


# EJ 2
class Guia_Tel():
    def __init__(self, numero, apellido, nombre, direccion):
        self.numero = numero
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        return str(self.numero) + ' | ' + self.apellido + ' | ' + self.nombre + ' | ' + self.direccion


def guia_telefono():
    tabla = crear_tabla(20)
    guiatel = Guia_Tel(randint(400000, 499999), 'Juan Fernando', 'Quintero', 'Bogota 543')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Marcelo', 'Gallardo', 'Figueroa Alcorta 57')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Gonzalo', 'Martínez', 'Madrid 912')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    guiatel = Guia_Tel(randint(400000, 499999), 'Rodolfo', 'D´Onofrio', 'Dubai 2142')
    agregar_ta(tabla, hash_division_guiatel, guiatel, 'numero')
    print('NUMERO DE TELEFONO | NOMBRE | APELLIDO | DIRECCION')
    barrido_ta(tabla)


# EJ 3
class Catedras():
    def __init__(self, codigo, nombre, modalidad, cant_horas, docente):
        self.codigo = codigo
        self.nombre = nombre
        self.modalidad = modalidad
        self.cant_horas = cant_horas
        self.docente = docente

    def __str__(self):
        return str(self.codigo) + ' | ' + self.nombre + ' | ' + self.modalidad + ' | ' + str(self.cant_horas) + ' | ' + self.docente


def catedras_universidad():
    tabla = crear_tabla(25)
    modalidad = ['Anual', 'Cuatrimestral']
    profe = ['Ing. Rodríguez', 'Prof. Gómez', 'Lic. García', 'Dr. Nuñez']
    datos = Catedras(randint(1, 1000), 'Algorimtos y Estr. de Datos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, datos)
    datos = Catedras(randint(1, 1000), 'Base de Datos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, datos)
    datos = Catedras(randint(1, 1000), 'Prog. Orientada a Objetos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, datos)
    datos = Catedras(randint(1, 1000), 'Diseño UX/UI', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, datos)
    datos = Catedras(randint(1, 1000), 'Analisis Matemático', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, datos)
    print('CODIGO | CATEDRA | MODALIDAD | CANT. HORAS | DOCENTE')
    barrido_tc(tabla)


# EJ 4
class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


def personajes_sw():
    tabla = crear_tabla(20)
    dato_sw = Personaje('Han Solo')
    agregar_tc(tabla, bernstein_star_wars, dato_sw)
    dato_sw = Personaje('Darth Vader')
    agregar_tc(tabla, bernstein_star_wars, dato_sw)
    dato_sw = Personaje('Jar Jar Binks')
    agregar_tc(tabla, bernstein_star_wars, dato_sw)
    dato_sw = Personaje('Yoda')
    agregar_tc(tabla, bernstein_star_wars, dato_sw)
    dato_sw = Personaje('Emperador Palpatine')
    agregar_tc(tabla, bernstein_star_wars, dato_sw)
    print('PERSONAJES DE STAR WARS')
    barrido_tc(tabla)


# EJ 5
class Contacto():
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return self.nombre + ' | ' + self.apellido + ' | ' + self.correo


def contactos_personas():
    tabla = crear_tabla(20)
    datos = Contacto('Gordon', 'Freeman', 'elgordofr@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Barney', 'Calhoun', 'barney1972@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Alyx', 'Vance', 'alyxuwu@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Eli', 'Vance', 'eli_vance@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    datos = Contacto('Isaac', 'Kleiner', 'drisaackleiner@valve.com')
    agregar_tc(tabla, bernstein_contactos, datos)
    print('NOMBRE | APELLIDO | CORREO ELECTRÓNICO')
    barrido_tc(tabla)


# EJ 6
class Stormtroopers():
    def __init__(self, legion, codigo):
        self.legion = legion
        self.codigo = codigo

    def __str__(self):
        return self.legion + ' ' + str(self.codigo)


def imperio_galactico():
    tabla_legion = crear_tabla(10)
    tabla_codigos = crear_tabla(1000)
    legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']
    # a
    for i in range(2000):
        legion = choice(legiones)
        codigo = randint(1000, 9999)
        trooper = Stormtroopers(legion, codigo)
        agregar_ta(tabla_legion, bernstein_troopers, trooper, 'legion')
        agregar_ta(tabla_codigos, hash_division_troopers, trooper, 'codigo')
    # b
    print('Troopers ordenados por legion')
    barrido_ta(tabla_legion)
    print()
    print('Troopers ordenados por código')
    barrido_ta(tabla_codigos)
    print()
    # c
    posc = hash_division(537, tabla_codigos)
    if tabla_codigos[posc]:
        print('Trooper designados para una misión de exploración')
        barrido_lista(tabla_codigos[posc])
    print()
    posc = hash_division(781, tabla_codigos)
    if tabla_codigos[posc]:
        print('Trooper designados para una misión de asalto')
        barrido_lista(tabla_codigos[posc])
    print()
    # d
    posl = bernstein('FN', tabla_legion)
    if tabla_legion[posl]:
        print('Troopers de la Legión FN')
        barrido_lista(tabla_legion[posl])
    print()
    posl = bernstein('CT', tabla_legion)
    if tabla_legion[posl]:
        print('Troopers de la Legión CT')
        barrido_lista(tabla_legion[posl])


# EJ 7
class Pokemon():
    def __init__(self, numero, nombre, tipo, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def __str__(self):
        return str(self.numero) + ' | ' + self.nombre + ' | ' + self.tipo + ' | ' + str(self.nivel)


def tabla_pokemon():
    tabla_principal = crear_tabla(20)
    tabla_secundaria = crear_tabla(20)
    tipo = ['Normal', 'Volador', 'Veneno', 'Tierra', 'Roca', 'Bicho',  'Agua',
            'Fantasma', 'Acero', 'Fuego', 'Planta', 'Electrico', 'Psiquico']
    pokemon = Pokemon(randint(1, 500), 'Alfa', choice(tipo), randint(1, 20))
    agregar_tc(tabla_principal, bernstein_pokemones, pokemon)
    pokemon = Pokemon(randint(1, 500), 'Beta', choice(tipo), randint(1, 20))
    agregar_tc(tabla_principal, bernstein_pokemones, pokemon)
    pokemon = Pokemon(randint(1, 500), 'Gama', choice(tipo), randint(1, 20))
    agregar_tc(tabla_principal, bernstein_pokemones, pokemon)
    pokemon = Pokemon(randint(1, 500), 'Epsilon', choice(tipo), randint(1, 20))
    agregar_tc(tabla_principal, bernstein_pokemones, pokemon)
    pokemon = Pokemon(randint(1, 500), 'Lambda', choice(tipo), randint(1, 20))
    agregar_tc(tabla_principal, bernstein_pokemones, pokemon)
    print('NUMERO | NOMBRE | TIPO | NIVEL')
    barrido_tc(tabla_principal)


# EJ 8
def alianza_rebelde():
    pass


# EJ 9
def mensaje_cifrado():
    pass


# EJ 10
def agencia_shield():
    pass


# diccionario()
# guia_telefono()
# catedras_universidad()
# personajes_sw()
# contactos_personas()
# imperio_galactico()
tabla_pokemon()
