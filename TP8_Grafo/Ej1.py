from TDA_Grafo import Grafo, barrido_vertices, buscar_vertice, insertar_arista
from TDA_Grafo import insertar_vertice_aeropuerto, insertar_arista_viaje, buscar_vertice_aero
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

europa = ['Alemania', 'Francia', 'Grecia']
america = ['Argentina', 'Brasil', 'EEUU', 'Jamaica']
asia = ['China', 'Japón', 'Tailandia']
empresa = ['Qatar Airways', 'Singapore Airlines', 'Fly Emirates',
        'Iberia', 'Turkish Airlines', 'Aerolineas Argentinas']
hora = randint(0, 23)
minuto = randint(0, 59)

for i in range(3):
    ori = buscar_vertice_aero(grafo, choice(europa))
    des = buscar_vertice_aero(grafo, choice(america))
    dato = Viaje(choice(empresa), time(randint(0, 23), 00), time(randint(0, 23), 00), randint(50000, 100000), time(randint(0, 23), 00), randint(1000, 5000))
    insertar_arista_viaje(grafo, dato, ori, des)


print('BARRIDO AEROPUERTOS')
print('Nombre | Latitud | Longuitud | Cantidad de pistas')
barrido_vertices(grafo)
