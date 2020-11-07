from TDA_Hash import crear_tabla, agregar_ta, agregar_tc, quitar_ta, quitar_tc
from TDA_Hash import buscar_tc, buscar_ta, cantidad_ta, cantidad_tc
from TDA_Hash import hash_division, hash_diccionario, bernstein
from TDA_Hash import barrido_ta, barrido_tc
from TDA_Hash import hash_division_guiatel, hash_division_catedra, bernstein_contactos
from TDA_Hash import bernstein_troopers, hash_division_troopers, bernstein_star_wars
from TDA_Hash import bernstein_pokemones, bernstein_palabra
from TDA_Lista import barrido_lista
from random import randint, choice
from math import sqrt


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
    print(tabla)
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
    catedra = Catedras(randint(1, 1000), 'Algorimtos y Estr. de Datos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Base de Datos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Prog. Orientada a Objetos', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Diseño UX/UI', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
    catedra = Catedras(randint(1, 1000), 'Analisis Matemático', choice(modalidad), randint(4, 8), choice(profe))
    agregar_tc(tabla, hash_division_catedra, catedra)
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
    personajes = ['Darth Vader', 'Luke Skywalker', 'Chewbacca', 'Yoda', 'R2D2', 'Jabba el Hutt',
                  'Obi-Wan Keobi', 'Han Solo', 'C3PO', 'Leia Organa', 'Rey', 'Poe Dameron',
                  'Finn', 'Lando Calrissian', 'Jabba el Hutt', 'Boba Fett', 'Jawa', 'Darth Maul',
                  'Anakin Skywalker', 'Bobba Fett', 'Jar Jar Binks', 'Darth Sidious', 'Kylo Ren',
                  'Obi-Wan Kenobi', 'Greddo', 'Wilhuff Tarkin', 'Owen Lars', 'Breha Organa']
    pos = 0
    for i in range(0, len(personajes)):
        nom = personajes[pos]
        dato_sw = Personaje(nom)
        agregar_tc(tabla, bernstein_star_wars, dato_sw)
        pos += 1
    print('Tabla de personajes de Star Wars con', len(tabla), 'posiciones')
    barrido_tc(tabla)

    # porcentaje de personajes cargados
    porc_tabla = (cantidad_tc(tabla)*100)/len(tabla)
    print('Porcentaje usado de la tabla', porc_tabla)
    print()

    if porc_tabla > 75:
        print('El factor de carga de la tabla supero el 75%. Haciendo rehashing...')
        nueva_tabla = crear_tabla(len(tabla)*2)
        for dato in tabla:
            if dato is not None:
                agregar_tc(nueva_tabla, bernstein_star_wars, dato)
        print('Nueva tabla con', len(nueva_tabla), 'posiciones')
        barrido_tc(nueva_tabla)
        porc_nueva_tabla = (cantidad_tc(nueva_tabla)*100)/len(nueva_tabla)
        print('Porcentaje usado de la nueva tabla', porc_nueva_tabla)
    else:
        print('El porcentaje de la tabla es menor a 75%')
        
    

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
    tabla = crear_tabla(50)
    nombres = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Spearow',
               'Dugtrio', 'Primeape', 'Terrakion', 'Tyrantrum', 'Golbat']
    tipos = ['Planta', 'Fuego', 'Agua', 'Eléctrico', 'Volador', 
             'Tierra',  'Lucha', 'Roca', 'Dragón', 'Veneno']
    pos = 0
    for i in range(len(nombres)):
        nom = nombres[pos]
        tip = tipos[pos]
        pokemon = Pokemon(randint(1, 999), nom, tip, randint(1, 50))
        agregar_tc(tabla, bernstein_pokemones, pokemon)
        pos += 1
    print('NUMERO | NOMBRE | TIPO | NIVEL')
    barrido_tc(tabla)


# EJ 8
def alianza_rebelde():
    pass

    def encriptar(oracion):
        clave = ""
        for letra in oracion:
            parte1 = str(ord(letra)*37)
            parte2 = hex(ord(letra)*2)
            clave += parte1[0] + parte2[1] + parte2[3] + parte1[1] + parte1[2] + parte2[0] + parte1[3] + parte2[2]
        return clave

    def desencriptar(clave):
        oracion = ""
        while len(clave) > 0:
            caracter = ""
            caracter += clave[0] + clave[3] + clave[4] + clave[6]
            clave = clave[8:]
            caracter = int(caracter)
            caracter = int(caracter/37)
            caracter = chr(caracter)
            oracion += caracter
        return oracion
    msj = '¡Armani! El taco, no. hace la personal y se va. Se va. Se va Martínez para el gol, y va el tercero y va el tercero y gol de River, gol de River, gol de Riverrrr'
    print('Mensaje a encripar:')
    print(msj)
    print()
    enpr = encriptar(msj)
    print('Mensaje encriptado:')
    print(enpr)
    print()
    dnpr = desencriptar(enpr)
    print('Mensaje desencriptado:')
    print(dnpr)


# EJ 9
def mensajes_cifrados():
    tabla = crear_tabla(10)
    tabla_aux = crear_tabla(10)

    def desifrar(dato):
        dic = {'#?&': '0','abc': '1','def':'2','ghi':'3','jkl':'4','mnñ':'5','opq':'6','rst':'7','uvw':'8','xyz':'9'}
        cadena = ''
        for i in range (0, len(dato), 3):
            cadena += dic[dato[i:i+3]]
        return chr(int(cadena))

    def cifrar(dato):
        valor = str(ord(dato))
        valor_cirado = ['#?&','abc','def','ghi','jkl','mnñ','opq','rst','uvw','xyz']
        cadena = ''
        for num in valor:
            numInt = int(num)
            cadena += valor_cirado[numInt]
        cadena += "%"
        return cadena

    a = 'El hombre adecuado en el sitio equivocad0 puede cambiar el rumbo del mundo. Despierte, Sr. Freeman. Despierte y mire a su alrededor.'
    a_cifrado = ''

    print('Mensaje a cifrar:')
    print(a)
    print()

    # cifrando
    for letra in a:
        valor = buscar_ta(tabla, hash_diccionario, Palabra(letra, ''), 'palabra')
        cifrado = ''
        if valor is None:
            cifrado = cifrar(letra)
            palabra = Palabra(letra, cifrado)
            agregar_ta(tabla, hash_diccionario, palabra, 'palabra')
        else:
            cifrado = valor.info.significado
        a_cifrado += cifrado
    print('Mensaje cifrado:')
    print(a_cifrado)
    print()

    lista = a_cifrado.split('%')
    lista.pop()

    # desifrando
    msj = ''
    for letras in lista:
        valor = buscar_ta(tabla_aux, bernstein_palabra, Palabra(letras, ''), 'palabra')
        decifrado = ''
        if valor is None:
            decifrado = desifrar(letras)
            palabra = Palabra(letras, decifrado)
            agregar_ta(tabla_aux, bernstein_palabra, palabra, 'palabra')
        else:
            decifrado = valor.info.significado
        msj += decifrado
    print('Mensaje decifrado')
    print(msj)


# EJ 10
def agencia_shield():
    pass

    def hash_cadenas(string):
        hash = 5381
        for caracter in string:
            hash = ((hash << 5) + hash) + ord(caracter)
        return hash & 0xFFFFFFFF

    def calculo_complemento(caracter):
        if ord(caracter) <= 78:
            return 79 + ord(caracter) - 32
        else:
            return 32 + ord(caracter) - 79

    # a
    def codifica4dig(caracter):
        caracteres = ''
        caracter_ascii = ord(caracter)
        caracter_ascii *= 37
        complemento = calculo_complemento(caracter)
        caracter_ascii = str(caracter_ascii)
        for digito in caracter_ascii:
            digito = int(digito)
            num = pow(digito, 2) + complemento
            caracter = chr(int(num))
            caracteres += caracter
        caracteres += chr(complemento)
        return caracteres

    def codifica_segm(segmento):
        num_cuatro_digitos = ''
        pri_chr = segmento[:4]
        ult_chr = segmento[4]
        complemento = ord(ult_chr)
        for elemento in pri_chr:
            elemento = ord(elemento) - complemento
            elemento = int(sqrt(elemento))
            elemento = str(elemento)
            num_cuatro_digitos += elemento
        num_cuatro_digitos = int(num_cuatro_digitos)
        chr_ascii = int(num_cuatro_digitos/37)
        caracter = chr(chr_ascii)
        return caracter

    def decodificar(mensaje):
        oracion = ''
        i = 0
        while i < len(mensaje):
            segmento = mensaje[i:i+5]
            indice = hash_cadenas(segmento) % len(tabla)
            if (tabla[indice] is None):
                caracter = codifica_segm(segmento)
                tabla[indice] = caracter
            else:
                caracter = tabla[indice]
            oracion += caracter
            i += 5
        return oracion

    tabla = crear_tabla(240)

    f = open('/home/iglesiasfacu/Facu Lic. en Sistemas/Algoritmos y Estructuras de Datos/TP6 - Hash/mensaje_1.txt', encoding='utf8')
    msj_codificado = f.read()
    f.close()
    msj_decodificado = decodificar(msj_codificado)
    print('Mensaje 1:')
    print(msj_decodificado)
    print()
    
    f = open('/home/iglesiasfacu/Facu Lic. en Sistemas/Algoritmos y Estructuras de Datos/TP6 - Hash/mensaje_2.txt', encoding='utf8')
    msj_codificado = f.read()
    f.close()
    msj_decodificado = decodificar(msj_codificado)
    print('Mensaje 2')
    print(msj_decodificado)
    print()

    f = open('/home/iglesiasfacu/Facu Lic. en Sistemas/Algoritmos y Estructuras de Datos/TP6 - Hash/mensaje_3.txt', encoding='utf8')
    msj_codificado = f.read()
    f.close()
    msj_decodificado = decodificar(msj_codificado)
    print('Mensaje 3')
    print(msj_decodificado)


# diccionario()
# guia_telefono()
# catedras_universidad()
personajes_sw()
# contactos_personas()
# imperio_galactico()
# tabla_pokemon()
# alianza_rebelde()
# mensajes_cifrados()
# agencia_shield()
