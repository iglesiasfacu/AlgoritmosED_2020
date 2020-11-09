from TDA_ArbolBin_AVL import insertar_nodo, busqueda_proximidad, inorden_tipo
from TDA_ArbolBin_AVL import inorden_poke_numero, inorden_poke_nombre, por_nivel
from TDA_ArbolBin_AVL import inorden_debilidad
from TDA_Archivo import abrir, cerrar, leer, guardar

print('EJERCICIO 17')
print()

class Pokemon():
    def __init__(self, nombre, numero , tipo, debilidad):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.debilidad = debilidad


datos = [['Bulbasaur', 1, 'planta/veneno', 'fuego/psiquico'],
         ['Bulivysaur', 2, 'planta/veneno', 'fuego/psiquico'], 
         ['Charmander', 4, 'fuego', 'agua/tierra'],
         ['Charizard', 6, 'fuego/volador', 'agua/electrico'], 
         ['Squirtle', 7, 'agua', 'planta/electrico'], 
         ['Butterfree', 12, 'bicho/volador', 'fuego/electrico/hielo'], 
         ['Pidgeotto', 17, 'normal/volador', 'hielo/roca'], 
         ['Rattata', 19, 'normal', 'lucha'], 
         ['Weedle', 13, 'bicho/veneno', 'fuego/psiquico/volador'], 
         ['Pikachu', 25, 'electrico', 'tierra'], 
         ['Raichu', 26, 'electrico', 'tierra'], 
         ['Meowth', 52, 'normal', 'lucha'],
         ['Growlithe', 58, 'fuego', 'agua/roca'], 
         ['Tentacool', 72, 'agua/veneno', 'psiquico/electrico'], 
         ['Weepinbell', 70, 'planta/veneno', 'fuego/volador/hielo']] 


arbol = None
arbol_nombre = None
arbol_numero = None
arbol_tipo = None

file = abrir('pokemon')
for poke in datos:
    x = Pokemon(poke[0], poke[1], poke[2], poke[3])
    guardar(file, x)

# a
pos = 0
while pos < len(datos):
    poke = leer(file, pos)
    arbol = insertar_nodo(arbol, [poke.nombre, poke.numero, poke.tipo, poke.debilidad], pos)
    arbol_nombre = insertar_nodo(arbol_nombre, poke.nombre, pos)
    arbol_numero = insertar_nodo(arbol_numero, poke.numero, pos)
    arbol_tipo = insertar_nodo(arbol_tipo, poke.tipo, pos)
    pos += 1
cerrar(file)

# b
busc = input('Busqueda por nombre del pokemon. Ingrese: ')
busqueda_proximidad(arbol_nombre, busc)
print()

# c, d y e
file = abrir('pokemon')
print('Pokemones de tipo: agua, fuego, planta o electrico')
inorden_tipo(arbol_nombre, file)
print()
print('Barrido pokemon por nombre')
inorden_poke_nombre(arbol_nombre, file)
print()
print('Barrido pokemon por numero')
inorden_poke_numero(arbol_numero, file)
print()
print('Barrido pokemon por nivel')
por_nivel(arbol_nombre)
print()
deb = input('Ingrese tipo de debilidad: ')
inorden_debilidad(arbol_nombre, file, deb)
print()
cerrar(file)


#inorden(arbol)
#inorden(arbol_nombre)
#inorden(arbol_numero)
#inorden(arbol_tipo)
