from TDA_ArbolBin import insertar_nodo_clima, por_nivel_meteorolgico
from random import choice

print('EJERCICIO 20')
print()

arbol = None


datos = [260, '']
arbol = insertar_nodo_clima(arbol, datos, 'visibilidad', 15)
datos = [60, '']
arbol = insertar_nodo_clima(arbol, datos, 'humedad', 70)
datos = [270, 'Despejado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [40, '']
arbol = insertar_nodo_clima(arbol, datos, 'viento', 8.7)
datos = [20, '']
arbol = insertar_nodo_clima(arbol, datos, 'viento', 5)
datos = [50, 'Parcialmente nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [10, 'Despejado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [30, 'Nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [180, '']
arbol = insertar_nodo_clima(arbol, datos, 'visibilidad', 8)
datos = [100, '']
arbol = insertar_nodo_clima(arbol, datos, 'presión', 1013)
datos = [80, '']
arbol = insertar_nodo_clima(arbol, datos, 'humedad', 96)
datos = [70, 'Nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [90, 'Mayormente Nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [160, '']
arbol = insertar_nodo_clima(arbol, datos, 'viento', 7.2)
datos = [140, '']
arbol = insertar_nodo_clima(arbol, datos, 'presión', 1018)
datos = [170, 'Nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [120, '']
arbol = insertar_nodo_clima(arbol, datos, 'visibilidad', 1)
datos = [150, 'Nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [110, 'Lluvia']
arbol = insertar_nodo_clima(arbol, datos)
datos = [130, 'Nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [220, '']
arbol = insertar_nodo_clima(arbol, datos, 'humedad', 92)
datos = [200, '']
arbol = insertar_nodo_clima(arbol, datos, 'visibilidad', 12)
datos = [190, 'Despejado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [210, 'Mayormente Nublado']
arbol = insertar_nodo_clima(arbol, datos)
datos = [240, '']
arbol = insertar_nodo_clima(arbol, datos, 'viento', 12.2)
datos = [230, 'Lluvia']
arbol = insertar_nodo_clima(arbol, datos)
datos = [250, 'Nublado']
arbol = insertar_nodo_clima(arbol, datos)


print('ARBOL DE DECISION METEOROLOGICO')
print()
print('CODIGO | ESTADO FINAL | CAMPO | UMBRAL')
por_nivel_meteorolgico(arbol)
print()

presión = float(input('Ingrese presión: '))
humedad = float(input('Ingrese humedad: '))
visibilidad = float(input('Ingrese visibilidad: '))
viento = float(input('Ingrese velocidad del viento: '))

datos = {'presión': presión, 'humedad': humedad, 'visibilidad': visibilidad,
         'viento': viento}
print(datos)
print()

pronostico = ''
while arbol is not None and pronostico == '':
    if datos[arbol.campo] <= arbol.umbral:
        if arbol.izq.izq is not None:
            arbol = arbol.izq
        else:
            pronostico = arbol.izq.info
            print('Estado del tiempo:', pronostico[1])
    else:
        if arbol.der.der is not None:
            arbol = arbol.der
        else:
            pronostico = arbol.der.info
            print('Estado del tiempo:', pronostico[1])



#def barrido(raiz):
#    if raiz.info[raiz.campo] > raiz.umbral:
#        pass