from TDA_Grafo import Grafo, buscar_vertice_red, insertar_vertice_red, insertar_arista_red
from TDA_Grafo import barrido_grafo_red, barrido_amplitud_red, barrido_profundidad_red
from TDA_Grafo import marcar_no_visitado, dijkstra_red, prim_red, eliminar_arista_red
from TDA_PilaDin import desapilar, pila_vacia

print('EJERCICIO 2')
print()

class Red():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def __str__(self):
        return self.nombre + ' | ' + self.tipo


grafo = Grafo(False)

# a
dato = Red('Switch 1', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Switch 2', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Ubuntu', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Mint', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Manjaro', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Fedora', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Parrot', 'PC')
insertar_vertice_red(grafo, dato)
dato = Red('Debian', 'Notebook')
insertar_vertice_red(grafo, dato)
dato = Red('Red Hat', 'Notebook')
insertar_vertice_red(grafo, dato)
dato = Red('Arch', 'Notebook')
insertar_vertice_red(grafo, dato)
dato = Red('Router 1', 'Router')
insertar_vertice_red(grafo, dato)
dato = Red('Router 2', 'Router')
insertar_vertice_red(grafo, dato)
dato = Red('Router 3', 'Router')
insertar_vertice_red(grafo, dato)
dato = Red('Guaraní', 'Servidor')
insertar_vertice_red(grafo, dato)
dato = Red('MongoDB', 'Servidor')
insertar_vertice_red(grafo, dato)
dato = Red('Impresora', 'Impresora')
insertar_vertice_red(grafo, dato)

ori = buscar_vertice_red(grafo, 'Switch 1')
des = buscar_vertice_red(grafo, 'Debian')
insertar_arista_red(grafo, 17, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 1')
des = buscar_vertice_red(grafo, 'Ubuntu')
insertar_arista_red(grafo, 18, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 1')
des = buscar_vertice_red(grafo, 'Impresora')
insertar_arista_red(grafo, 22, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 1')
des = buscar_vertice_red(grafo, 'Mint')
insertar_arista_red(grafo, 80, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 1')
des = buscar_vertice_red(grafo, 'Router 1')
insertar_arista_red(grafo, 29, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 2')
des = buscar_vertice_red(grafo, 'Manjaro')
insertar_arista_red(grafo, 40, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 2')
des = buscar_vertice_red(grafo, 'Fedora')
insertar_arista_red(grafo, 3, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 2')
des = buscar_vertice_red(grafo, 'Parrot')
insertar_arista_red(grafo, 12, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 2')
des = buscar_vertice_red(grafo, 'Router 3')
insertar_arista_red(grafo, 61, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 2')
des = buscar_vertice_red(grafo, 'Arch')
insertar_arista_red(grafo, 56, ori, des)
ori = buscar_vertice_red(grafo, 'Switch 2')
des = buscar_vertice_red(grafo, 'MongoDB')
insertar_arista_red(grafo, 5, ori, des)
ori = buscar_vertice_red(grafo, 'Router 1')
des = buscar_vertice_red(grafo, 'Router 2')
insertar_arista_red(grafo, 37, ori, des)
ori = buscar_vertice_red(grafo, 'Router 1')
des = buscar_vertice_red(grafo, 'Router 3')
insertar_arista_red(grafo, 43, ori, des)
ori = buscar_vertice_red(grafo, 'Router 2')
des = buscar_vertice_red(grafo, 'Router 3')
insertar_arista_red(grafo, 50, ori, des)
ori = buscar_vertice_red(grafo, 'Router 2')
des = buscar_vertice_red(grafo, 'Guaraní')
insertar_arista_red(grafo, 9, ori, des)
ori = buscar_vertice_red(grafo, 'Router 2')
des = buscar_vertice_red(grafo, 'Red Hat')
insertar_arista_red(grafo, 25, ori, des)

print('ESQUEMA DE RED')
barrido_grafo_red(grafo)
print()

# b
note = ['Red Hat', 'Debian', 'Arch']
pos = 0
for i in range(len(note)):
    dato = note[pos]
    print('Barrido profundidad:', dato)
    ori = buscar_vertice_red(grafo, 'Red Hat')
    barrido_profundidad_red(grafo, ori)
    marcar_no_visitado(grafo)
    print()
    print('Barrido amplitud:', dato)
    ori = buscar_vertice_red(grafo, 'Red Hat')
    barrido_amplitud_red(grafo, ori)
    marcar_no_visitado(grafo)
    print()
    pos += 1


# c
pc = ['Manjaro', 'Parrot', 'Fedora']
pos = 0
for i in range(len(pc)):
    dato = pc[pos]
    pila = dijkstra_red(grafo, dato, 'Impresora')
    fin = 'Impresora'
    peso = None
    print('Camino mas corto desde', dato, 'hasta Impresora')
    print('---ARRIBO---')
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if peso is None and fin == dato[1][0].info.nombre:
            peso = dato[0]
        if fin == dato[1][0].info.nombre:
            print(dato[1][0].info.nombre)
            fin = dato[1][1]
    print('---SALIDA---')
    print('Distancia mas corta:', peso, 'mb')
    print()
    pos += 1


# d
print('Algoritmo de Prim para encontrar el arbol de expansión mínimo')
bosque = prim_red(grafo)

for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()


# e
pc2 = ['Manjaro', 'Parrot', 'Fedora', 'Ubuntu', 'Mint']
pos = 0
camino_mas_corto = None
for i in range(len(pc2)):
    dato = pc2[pos]
    pila = dijkstra_red(grafo, dato, 'Guaraní')
    fin = 'Guaraní'
    peso = None
    print('Peso de camino desde', dato, 'hasta Guaraní')
    print('---ARRIBO---')
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if peso is None and fin == dato[1][0].info.nombre:
            peso = dato[0]
            if camino_mas_corto is None:
                camino_mas_corto = [pc2[pos], peso]
            else:
                if peso < camino_mas_corto[1]:
                    camino_mas_corto = [pc2[pos], peso]
        if fin == dato[1][0].info.nombre:
            print(dato[1][0].info.nombre)
            fin = dato[1][1]
    print('---SALIDA---')
    print('Peso total:', peso)
    print()
    pos += 1

print('Distancia mas corta hacia Guaraní:', camino_mas_corto)
print()


# f
compu = ['Debian', 'Ubuntu', 'Mint']
pos = 0
camino_mas_corto = None
for i in range(len(compu)):
    dato = compu[pos]
    pila = dijkstra_red(grafo, dato, 'MongoDB')
    fin = 'MongoDB'
    peso = None
    print('Peso de camino desde', dato, 'hasta MongoDB')
    print('---ARRIBO---')
    while not pila_vacia(pila):
        dato = desapilar(pila)
        if peso is None and fin == dato[1][0].info.nombre:
            peso = dato[0]
            if camino_mas_corto is None:
                camino_mas_corto = [compu[pos], peso]
            else:
                if peso < camino_mas_corto[1]:
                    camino_mas_corto = [compu[pos], peso]
        if fin == dato[1][0].info.nombre:
            print(dato[1][0].info.nombre)
            fin = dato[1][1]
    print('---SALIDA---')
    print('Peso total:', peso)
    print()
    pos += 1

print('Distancia mas corta hacia MongoDB:', camino_mas_corto)
print()


# g
ori = buscar_vertice_red(grafo, 'Switch 1')
x = eliminar_arista_red(grafo, ori, 'Impresora')
ori = buscar_vertice_red(grafo, 'Impresora')
x = eliminar_arista_red(grafo, ori, 'Switch 1')
print('se elimino la arista de peso:', x)
print()
ori = buscar_vertice_red(grafo, 'Impresora')
des = buscar_vertice_red(grafo, 'Router 2')
insertar_arista_red(grafo, 22, ori, des)

note = ['Red Hat', 'Debian', 'Arch']
pos = 0
for i in range(len(note)):
    dato = note[pos]
    print('Barrido profundidad:', dato)
    ori = buscar_vertice_red(grafo, 'Red Hat')
    barrido_profundidad_red(grafo, ori)
    marcar_no_visitado(grafo)
    print()
    print('Barrido amplitud:', dato)
    ori = buscar_vertice_red(grafo, 'Red Hat')
    barrido_amplitud_red(grafo, ori)
    marcar_no_visitado(grafo)
    print()
    pos += 1
