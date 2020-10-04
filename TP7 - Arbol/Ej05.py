from TDA_ArbolBin import insertar_nodo, inorden, postorden, generar_bosque
from TDA_ArbolBin import inorden_marvel, inorden_villanos, superheroes_c
from TDA_ArbolBin import busqueda_proximidad, cantidad_nodos

print('EJERCICIO 5')
print()

class Personaje():
    def __init__(self, nombre):
        self.nombre = nombre


arbol = None
arbol_superheroes = None
arbol_villanos = None

# a
arbol = insertar_nodo(arbol, 'Batman', True)
arbol = insertar_nodo(arbol, 'Joker', False)
arbol = insertar_nodo(arbol, 'Iron Man', True)
arbol = insertar_nodo(arbol, 'Lex Luthor', False)
arbol = insertar_nodo(arbol, 'Doctor Extraño', True)
arbol = insertar_nodo(arbol, 'Magneto', False)
arbol = insertar_nodo(arbol, 'Capitán America', True)
arbol = insertar_nodo(arbol, 'Thanos', False)

print('PERSONAJE | BANDO')
inorden_marvel(arbol)
print()

# b
print('Villanos listados alfabeticamente')
inorden_villanos(arbol)
print()

# c
print('Superheores que empiecen con "C"')
superheroes_c(arbol)
print()

# e
busqueda_proximidad(arbol, 'Doctor')
print()

# g
arbol_superheroes, arbol_villanos = generar_bosque(arbol, arbol_superheroes, arbol_villanos)
print('Arbol Superheroes')
inorden(arbol_superheroes)
print()
print('Arbol Villanos')
inorden(arbol_villanos)
print()

# d
print('Cantidad de superheroes en el arbol:', cantidad_nodos(arbol_superheroes))
print()

# f
print('Superheroes ordenados de manera descendente')
postorden(arbol_superheroes)
print()