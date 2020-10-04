from TDA_ArbolBin import insertar_nodo, inorden
from TDA_ArbolBin import inorden_lightsaber
from TDA_Archivo import abrir, cerrar, leer

print('EJERCICIO 6')
print()

class Jedi():
    def __init__(self, nombre, especie, año_nacimiento, color_sable, ranking, maestro):
        self.nombre = nombre
        self.especie = especie
        self.año_nacimiento = año_nacimiento
        self.color_sable = color_sable
        self.ranking = ranking
        self.maestro = maestro


arbol_nombre = None
arbol_ranking = None
arbol_especie = None

file = abrir('jedis')
pos = 0
while pos < len(file):
    jedi = leer(file, pos)
    arbol_nombre = insertar_nodo(arbol_nombre, jedi[0], pos)
    arbol_ranking = insertar_nodo(arbol_ranking, jedi[1], pos)
    arbol_especie = insertar_nodo(arbol_especie , jedi[2], pos)
    pos += 1
cerrar(file)

# a
file = abrir('jedis')
inorden_lightsaber(arbol_nombre, file)
cerrar(file)
inorden(arbol_nombre)
a=input()