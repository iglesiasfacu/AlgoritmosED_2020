from TDA_ArbolBin import insertar_nodo, eliminar_nodo, busqueda_arbol, contar_ocurrencias, par_impar
from TDA_ArbolBin import inorden, postorden, preorden, por_nivel
from random import randint

print('EJERCICIO 1')
print()

arbol = None
for i in range(0, 10):
    arbol = insertar_nodo(arbol, randint(0, 100))

# a
print('Barrido inorden')
inorden(arbol)
print()
print('Barrido preorden')
preorden(arbol)
print()
print('Barrido postorden')
postorden(arbol)
print()
print('Barrido por nivel')
por_nivel(arbol)
print()

# b
buscado = int(input('Ingrese valor a buscar: '))
pos = busqueda_arbol(arbol, buscado)
if pos is not None:
    print('El numero se encuentra en el arbol')
else:
    print('El numero no existe')
print()

# c
eliminado = int(input('Ingrese valor a eliminar: '))
pos = busqueda_arbol(arbol, eliminado)
if pos is not None:
    arbol, eliminado = eliminar_nodo(arbol, eliminado)
    print('Se elimino:', eliminado)
else:
    print('El numero no existe')
print()
print('Nuevo arbol')
por_nivel(arbol)
print()

# e
ocurrencia = int(input('Ingrese valor para determinar sus ocurrencias: '))
pos = busqueda_arbol(arbol, ocurrencia)
if pos is not None:
    print('Cantidad de ocurrencias:', contar_ocurrencias(pos, ocurrencia, 0))
else:
    print('El numero no existe')
print()

# f
pares, impares = 0, 0
pares, impares = par_impar(arbol, pares, impares)
print('Cantidad de pares:', pares)
print('Cantidad de impares:', impares)
print()