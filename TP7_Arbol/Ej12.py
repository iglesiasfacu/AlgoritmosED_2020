from TDA_ArbolBin_AVL import insertar_nodo, altura, cortar_por_nivel, contar_nodos
from TDA_ArbolBin_AVL import preorden

print('EJERCICIO 12')
print()

arbol = None

# a
for i in range(1,1024):
    arbol = insertar_nodo(arbol, i)

cantidad = [0]
contar_nodos(arbol, cantidad)
print('Cantidad de nodos:', cantidad[0])
print('Altura del arbol:', altura(arbol))
print()

bosque = []
cortar_por_nivel(arbol, bosque)
print('Cortando el arbol...')
print('Tamaño del bosque:', len(bosque))
print()

for arbol in bosque:
    print('Raiz del arbol:', arbol.info)
    cantidad = [0]
    #preorden(arbol)
    contar_nodos(arbol, cantidad)
    print('Cantidad de nodos del arbol:', cantidad[0])
    print()