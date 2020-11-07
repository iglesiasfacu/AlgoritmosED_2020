from TDA_ArbolBin_AVL import busqueda_arbol, insertar_nodo, eliminar_nodo, por_nivel
from TDA_ArbolBin_AVL import inorden_altura, inorden_peso
from TDA_Archivo import abrir, leer, cerrar, guardar, modificar

print('EJERCICIO 15')
print()

class Personaje():
    def __init__(self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

arbol = None
datos = [['Darth Vader', 1.85, 93], ['Chewbacca', 2.04, 113], ['C-3PO', 1.67, 72],
         ['Yoda', 0.9, 47], ['Boba Fett', 1.83, 78], ['Han Solo', 1.77, 83],
         ['Jabba el Hutt', 3.9, 531], ['Darth Maul', 1.78, 74]]

# se guarda datos en archivo
file = abrir('starwars')
for dato in datos:
    x = Personaje(dato[0], dato[1], dato[2])
    guardar(file, x)

# a
# se inserta nombres en arbol
pos = 0
while pos < len(datos):
    personaje = leer(file, pos)
    arbol = insertar_nodo(arbol, personaje.nombre, pos)
    #print(personaje.nombre, 'anadido en la posicion:', pos)
    pos += 1
cerrar(file)

print('Arbol de personajes:')
por_nivel(arbol)
print()


# b
print('1) Alta')
print('2) Baja')
print('3) Modificacion')
print('4) Salir')
control = input('Que desea hacer: ')
print()


def alta_sw(arbol):
    file = abrir('starwars')
    nom = input('Ingrese un nombre: ')
    alt = int(input('Ingrese su altura: '))
    peso = int(input('Ingrese su peso: '))
    dato = Personaje(nom, alt, peso)
    insertar_nodo(arbol, dato.nombre)
    guardar(file, dato)
    cerrar(file)
    datos.append([nom, alt, peso])

def baja_sw(arbol):
    file = abrir('starwars')
    buscado = input('Ingrese nombre del personaje a dar de baja: ')
    arbol, x = eliminar_nodo(arbol, buscado)
    print('Se ha eliminado:', x)

def modif_sw(arbol):
    file = abrir('starwars')
    busc = input('Ingrese nombre del personaje a modificar: ')
    val = busqueda_arbol(arbol, busc)
    if val is not None:
        print('1) Nombre')
        print('2) Altura')
        print('3) Peso')
        mod = input('Elija campo a modificar: ')
        sw = leer(file, pos)
        if mod == '1':
            nom = input('Ingrese el nuevo nombre: ')
            dato = Personaje(nom, sw.altura, sw.peso)
            modificar(file, pos, dato)
            sw = leer(file, pos)
            arbol = insertar_nodo(arbol, sw.nombre, pos)
        elif mod == '2':
            alt = int(input('Ingrese la nueva altura: '))
            dato = Personaje(sw.nombre, alt, sw.peso)
            modificar(file, pos, dato)
            sw = leer(file, pos)
            arbol = insertar_nodo(arbol, sw.nombre, pos)
        elif mod == '3':
            peso = int(input('Ingrese el nuevo peso: '))
            dato = Personaje(sw.nombre, sw.altura, peso)
            modificar(file, pos, dato)
            sw = leer(file, pos)
            arbol = insertar_nodo(arbol, sw.nombre, pos)
        else:
            print('ERROR')
    else:
        print('El personaje no existe')
    cerrar(file)


if control == '1':
    alta_sw(arbol)
elif control == '2':
    baja_sw(arbol)
elif control == '3':
    modif_sw(arbol)
elif control == '4':
    print()
else:
    print('ERROR')
print()

# c
file = abrir('starwars')
for i in range(len(datos)):
    val = leer(file, i)
    if val.nombre == 'Yoda':
        print('Datos de Yoda:')
        print('Nombre:', val.nombre)
        print('Altura:', val.altura)
        print('Peso:', val.peso)
print()
for i in range(len(datos)):
    val = leer(file, i)
    if val.nombre == 'Boba Fett':
        print('Datos de Boba Fett:')
        print('Nombre:', val.nombre)
        print('Altura:', val.altura)
        print('Peso:', val.peso)
cerrar(file)
print()

# d
print('Personajes que miden mas de un metro')
file = abrir('starwars')
inorden_altura(arbol, file)
cerrar(file)
print()

# e
print('Personajes que pesan menos de 75kg')
file = abrir('starwars')
inorden_peso(arbol, file)
cerrar(file)
print()


print(datos)
print()
print('Arbol de personajes:')
por_nivel(arbol)
print()
