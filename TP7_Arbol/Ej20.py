from TDA_ArbolBin_AVL import insertar_nodo_clima, inorden, preorden

print('EJERCICIO 20')
print()

arbol = None

#temperatura, presión, humedad, visibilidad, viento
#datos = ['id', 24, 1021, 90, 25, 7]

datos = [500, '']
arbol = insertar_nodo_clima(arbol, datos, 4, 15)
datos = [600, 'Despejado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [250, '']
arbol = insertar_nodo_clima(arbol, datos, 3, 70)
datos = [125, '']
arbol = insertar_nodo_clima(arbol, datos, 5, 8.7)
datos = [130, 'Parcialmente nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [60, '']
arbol = insertar_nodo_clima(arbol, datos, 5, 5)
datos = [40, 'Despejado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [80, 'Nublado']
arbol = insertar_nodo_clima(arbol, datos)

preorden(arbol)
print()
inorden(arbol)

# def barrido(raiz):
#     if raiz.info[raiz.campo] > raiz.umbral:
#         pass