from TDA_ArbolBin_AVL import insertar_nodo, busqueda_arbol, por_nivel, hijo_der, hijo_izq
from random import randint

print('EJERCICIO 4')
print()

arbol = None
for i in range(0, 10):
    arbol = insertar_nodo(arbol, randint(0, 100))
print('Barrido por nivel')
por_nivel(arbol)
print()

buscado = int(input('Ingrese valor a buscar: '))
pos = busqueda_arbol(arbol, buscado)
if pos is not None:
    print('hijo izquierdo')
    hijo_izq(arbol)
    print('hijo derecho')
    hijo_der(arbol)
else:
    print('El numero no existe')
print()