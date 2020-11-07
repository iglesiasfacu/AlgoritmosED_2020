from TDA_ArbolBin_AVL import insertar_nodo, inorden, nodo_minimo, nodo_maximo
from random import randint

print('EJERCICIO 8')
print()

arbol = None
for i in range(0, 10):
    arbol = insertar_nodo(arbol, randint(0, 100))
print('Arbol')
inorden(arbol)
print()

min = nodo_minimo(arbol)
max = nodo_maximo(arbol)
print('Nodo minimo del arbol:', min.info)
print('Nodo maximo del arbol:', max.info)
