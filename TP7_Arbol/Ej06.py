from TDA_ArbolBin_AVL import insertar_nodo, por_nivel, busqueda_arbol
from TDA_ArbolBin_AVL import inorden_nombrank, inorden_lightsaber, inorden_jedimaster
from TDA_ArbolBin_AVL import inorden_especie, inorden_ayguion
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

# a
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

# lee archivo jedis
print('NOMBRE | RANKING | ESPECIE | MAESTRO | COLOR DE SABLE | ORIGEN | AÑO DE NACIMIENTO | ALTURA')
arch = abrir('jedis')
for i in range(0, len(arch)):
    print(leer(arch, i))
cerrar(arch)
print()

# b
print('INORDEN POR NOMBRE Y RANKING')
file = abrir('jedis')
inorden_nombrank(arbol_nombre, file)
cerrar(file)
print()

# c
print('BARRIDO RANKING POR NIVEL')
por_nivel(arbol_ranking)
print()
print('BARRIDO ESPECIE POR NIVEL')
por_nivel(arbol_especie)
print()

# d
print('Info de Luke Skywalker')
print('NOMBRE | RANKING | ESPECIE | MAESTRO | COLOR DE SABLE | ORIGEN | AÑO DE NACIMIENTO | ALTURA')
pos = busqueda_arbol(arbol_nombre, 'luke skywalker')
if pos is not None:
    file = abrir('jedis')
    jedi = leer(file, pos.nrr)
    cerrar(file)
    print(jedi)
print()

print('Info de Yoda')
print('NOMBRE | RANKING | ESPECIE | MAESTRO | COLOR DE SABLE | ORIGEN | AÑO DE NACIMIENTO | ALTURA')
pos = busqueda_arbol(arbol_nombre, 'yoda')
if pos is not None:
    file = abrir('jedis')
    jedi = leer(file, pos.nrr)
    cerrar(file)
    print(jedi)
print()

# e
print('JEDIS CON RANKING: "JEDI MASTER"')
file = abrir('jedis')
inorden_jedimaster(arbol_nombre, file)
cerrar(file)
print()

# f
print('JEDIS CON SABLE COLOR VERDE')
file = abrir('jedis')
inorden_lightsaber(arbol_nombre, file)
cerrar(file)
print()

# h
print('JEDIS DE ESPECIE TOGRUTA O CEREAN')
file = abrir('jedis')
inorden_especie(arbol_nombre, file)
cerrar(file)
print()

# i
print('JEDIS QUE COMIENZAN CON LA LETRA A Y CONTIENEN UN "-"')
file = abrir('jedis')
inorden_ayguion(arbol_nombre, file)
cerrar(file)
print()
