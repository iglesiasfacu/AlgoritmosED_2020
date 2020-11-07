from TDA_ArbolBin_AVL import insertar_nodo, busqueda_arbol, inorden, cantidad_nodos
from TDA_ArbolBin_AVL import cantidad_hojas, padre, altura
from random import randint

print('EJERCICIO 11')
print()

arbol = None
for i in range(0, 10):
    arbol = insertar_nodo(arbol, randint(0, 100))
print('Arbol')
inorden(arbol)
print()

#a
print('El arbol contiene', cantidad_nodos(arbol),'nodos')
print()

#byc
print('El arbol contiene', cantidad_hojas(arbol),'hojas')
print()

#d
busc = int(input('Ingrese nodo para determinar su padre: '))
pos = busqueda_arbol(arbol, busc)
if pos is not None:
    print('El padre es', padre(arbol, pos))
else:
    print('El numero no existe')
print()

#e
print('La altura del arbol es:', altura(arbol))
print()