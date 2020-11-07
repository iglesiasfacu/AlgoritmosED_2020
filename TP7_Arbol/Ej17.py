from TDA_ArbolBin_AVL import insertar_nodo, inorden
from TDA_Archivo import abrir, cerrar, leer

print('EJERCICIO 17')
print()

class Pokemon():
    def __init__(self, nombre, numero , tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad


arbol_nombre = None
arbol_numero = None
arbol_tipo = None

file = abrir('pokemon')
pos = 0
while pos < len(file):
    poke = leer(file, pos)
    arbol_nombre = insertar_nodo(arbol_nombre, poke[0], pos)
    arbol_numero = insertar_nodo(arbol_numero, poke[1], pos)
    arbol_tipo = insertar_nodo(arbol_tipo, poke[2], pos)
    pos += 1
cerrar(file)


