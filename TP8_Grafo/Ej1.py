from TDA_Grafo import Grafo, barrido_grafo, buscar_vertice_aero, dijkstra_distancia
from TDA_Grafo import insertar_vertice_aeropuerto, insertar_arista_viaje, prim_red
from TDA_Grafo import dijkstra_duracion, dijkstra_costo, adyacentes, existe_paso_aero
from TDA_PilaDin import desapilar, pila_vacia
from random import randint, choice
from datetime import time

print('EJERCICIO 1')
print()

class Aeropuerto():
    def __init__(self, nombre, latitud, longuitud, num_pistas):
        self.nombre = nombre
        self.latitud = latitud
        self.longuitud = longuitud
        self.num_pistas = num_pistas
    
    def __str__(self):
        return self.nombre + ' | ' + str(self.latitud) + ' | ' + str(self.longuitud) + ' | ' + str(self.num_pistas)


class Viaje():
    def __init__(self, empresa, hora_salida, hora_arribo, costo_pasaje, duracion, distancia):
        self.empresa = empresa
        self.hora_salida = hora_salida
        self.hora_arribo = hora_arribo
        self.costo_pasaje = costo_pasaje
        self.duracion = duracion
        self.distancia = distancia
    
    def __str__(self):
        return '| ' + self.empresa + ' | ' + str(self.hora_salida) + ' | ' + str(self.hora_arribo) + ' | ' + str(self.costo_pasaje) + ' | ' + str(self.duracion)+ ' | ' + str(self.distancia)


grafo = Grafo(False)

# a c y d
dato = Aeropuerto('Alemania', 51, 9, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('Argentina', 34, 64, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('Brasil', 10, 55, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('China', 35, 105, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('EEUU', 38, 97, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('Francia', 46, 2, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('Grecia', 39, 22, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('Jamaica', 18, 77, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('Japón', 36, 138, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)
dato = Aeropuerto('Tailandia', 15, 100, randint(10, 50))
insertar_vertice_aeropuerto(grafo, dato)


# b
europa = ['Alemania', 'Francia', 'Grecia']
america = ['Argentina', 'Brasil', 'EEUU', 'Jamaica']
asia = ['China', 'Japón', 'Tailandia']
empresa = ['Qatar Airways', 'Singapore Airlines', 'Fly Emirates',
        'Iberia', 'Turkish Airlines']
hora = randint(0, 23)
minuto = randint(0, 59)

# no puede haber mas de un camino entre dos vertices
for i in range(3):
    ori = buscar_vertice_aero(grafo, choice(europa))
    des = buscar_vertice_aero(grafo, choice(america))
    dato = Viaje(choice(empresa), time(randint(0, 23), 00), time(randint(0, 23), 00), randint(50000, 100000), randint(5, 12), randint(1000, 5000))
    insertar_arista_viaje(grafo, dato, ori, des)

for i in range(3):
    ori = buscar_vertice_aero(grafo, choice(asia))
    des = buscar_vertice_aero(grafo, choice(europa))
    dato = Viaje(choice(empresa), time(randint(0, 23), 00), time(randint(0, 23), 00), randint(50000, 100000), randint(5, 12), randint(1000, 5000))
    insertar_arista_viaje(grafo, dato, ori, des)

for i in range(3):
    ori = buscar_vertice_aero(grafo, choice(america))
    des = buscar_vertice_aero(grafo, choice(asia))
    dato = Viaje(choice(empresa), time(randint(0, 23), 00), time(randint(0, 23), 00), randint(50000, 100000), randint(5, 12), randint(1000, 5000))
    insertar_arista_viaje(grafo, dato, ori, des)


ori = buscar_vertice_aero(grafo, 'Argentina')
des = buscar_vertice_aero(grafo, 'Tailandia')
dato = Viaje('Aerolineas Argentinas', time(randint(0, 23), 00), time(randint(0, 23), 00), randint(1000000, 10000000), randint(24, 48), 50000)
insertar_arista_viaje(grafo, dato, ori, des)


print('BARRIDO AEROPUERTOS')
print('Nombre | Latitud | Longuitud | Cantidad de pistas')
barrido_grafo(grafo)
print()

# e
print('CAMINOS MAS CORTOS DESDE ARGENTINA A TAILANDIA')
print()

print('i) por menor distancia')
print()
camino_mas_corto = dijkstra_distancia(grafo, 'Argentina', 'Tailandia')
fin = 'Tailandia'
distancia = None
print('---ARRIBO---')
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if distancia is None and fin == dato[1][0].info.nombre:
        distancia = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('---SALIDA---')
print('Distancia mas corta: ' + str(distancia) + 'km')
print()

print('ii) por menor duración de tiempo')
print()
camino_mas_corto = dijkstra_duracion(grafo, 'Argentina', 'Tailandia')
fin = 'Tailandia'
duracion = None
print('---ARRIBO---')
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if duracion is None and fin == dato[1][0].info.nombre:
        duracion = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('---SALIDA---')
print('Camino con menos duracion: ' + str(duracion) + 'hs.')
print()

print('iii) por menor costo')
print()
camino_mas_corto = dijkstra_costo(grafo, 'Argentina', 'Tailandia')
fin = 'Tailandia'
coste_pasaje = None
print('---ARRIBO---')
while not pila_vacia(camino_mas_corto):
    dato = desapilar(camino_mas_corto)
    if coste_pasaje is None and fin == dato[1][0].info.nombre:
        coste_pasaje = dato[0]
    if fin == dato[1][0].info.nombre:
        print(dato[1][0].info.nombre)
        fin = dato[1][1]
print('---SALIDA---')
print('Camino mas barato: $' + str(coste_pasaje))
print()

print('v) Viajes a Grecia de manera directa')
print()

vertices = buscar_vertice_aero(grafo, 'Grecia')
if vertices is not None:
    print('AEROPUERTO | AEROLINEA | HORA DE SALIDA | HORA DE ARRIBO | COSTE($) | HS DE VIAJE | DISTANCIA(KM)')
    adyacentes(vertices)
else:
    print('No hay vuelos a Grecia pa')
print()

print('v) Viajes a Grecia de manera indirecta')
datos = ['Argentina', 'Alemania', 'Brasil', 'China', 'EEUU', 'Francia', 'Japón', 'Jamaica', 'Tailandia']
pos = 0
for i in range(len(datos)):
    ori = buscar_vertice_aero(grafo, datos[pos])
    des = buscar_vertice_aero(grafo, 'Grecia')
    if existe_paso_aero(grafo, ori, des):
        print('Existe paso indirecto a Grecia desde:', datos[pos])
    pos += 1

