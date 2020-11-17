from TDA_Grafo import Grafo, insertar_vertice_maravilla, insertar_arista_maravilla
from TDA_Grafo import buscar_vertice_maravilla, barrido_grafo_maravilla
from TDA_Grafo import prim_arq, prim_nat

print('EJERCICIO 3')
print()

class Maravilla():
    def __init__(self, nombre, ubicacion, tipo):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tipo = tipo
    
    def __str__(self):
        return self.nombre + ' | ' + self.ubicacion + ' | ' + self.tipo


grafo = Grafo(False)

# a
dato = Maravilla('Chichén Itzá', 'México', 'Arquitectónica')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Coliseo de Roma', 'Italia', 'Arquitectónica')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Cristo Redentor', 'Brasil', 'Arquitectónica')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Gran Muralla China', 'China', 'Arquitectónica')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Machu Picchu', 'Perú', 'Arquitectónica')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Petra', 'Jordania', 'Arquitectónica')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Taj Mahal', 'India', 'Arquitectónica')
insertar_vertice_maravilla(grafo, dato)

dato = Maravilla('Amazonia', 'Bolivia/Brasil/Colombia/Ecuador/Guayana Francesa/Guyana/Perú/Surinam/Venezuela', 'Natural')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Bahía de Ha-Long', 'Vietnam', 'Natural')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Cataratas del Iguazú', 'Argentina/Brasil', 'Natural')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Isla Jeju', 'Corea del Sur', 'Natural')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Montaña de la Mesa', 'Sudáfrica', 'Natural')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Parque Nacional de Komodo', 'Indonesia', 'Natural')
insertar_vertice_maravilla(grafo, dato)
dato = Maravilla('Parque Nacional del río subterráneo de Puerto Princesa', 'Filipinas', 'Natural')
insertar_vertice_maravilla(grafo, dato)


# b
ori = buscar_vertice_maravilla(grafo, 'Chichén Itzá')
des = buscar_vertice_maravilla(grafo, 'Coliseo de Roma')
insertar_arista_maravilla(grafo, 10141, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Chichén Itzá')
des = buscar_vertice_maravilla(grafo, 'Cristo Redentor')
insertar_arista_maravilla(grafo, 6924, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Chichén Itzá')
des = buscar_vertice_maravilla(grafo, 'Gran Muralla China')
insertar_arista_maravilla(grafo, 12818, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Chichén Itzá')
des = buscar_vertice_maravilla(grafo, 'Machu Picchu')
insertar_arista_maravilla(grafo, 4717, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Chichén Itzá')
des = buscar_vertice_maravilla(grafo, 'Petra')
insertar_arista_maravilla(grafo, 12548, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Chichén Itzá')
des = buscar_vertice_maravilla(grafo, 'Taj Mahal')
insertar_arista_maravilla(grafo, 15281, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Coliseo de Roma')
des = buscar_vertice_maravilla(grafo, 'Cristo Redentor')
insertar_arista_maravilla(grafo, 9064, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Coliseo de Roma')
des = buscar_vertice_maravilla(grafo, 'Gran Muralla China')
insertar_arista_maravilla(grafo, 7562, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Coliseo de Roma')
des = buscar_vertice_maravilla(grafo, 'Machu Picchu')
insertar_arista_maravilla(grafo, 10483, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Coliseo de Roma')
des = buscar_vertice_maravilla(grafo, 'Petra')
insertar_arista_maravilla(grafo, 4137, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Coliseo de Roma')
des = buscar_vertice_maravilla(grafo, 'Taj Mahal')
insertar_arista_maravilla(grafo, 6565, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cristo Redentor')
des = buscar_vertice_maravilla(grafo, 'Gran Muralla China')
insertar_arista_maravilla(grafo, 16622, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cristo Redentor')
des = buscar_vertice_maravilla(grafo, 'Machu Picchu')
insertar_arista_maravilla(grafo, 2573, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cristo Redentor')
des = buscar_vertice_maravilla(grafo, 'Petra')
insertar_arista_maravilla(grafo, 10634, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cristo Redentor')
des = buscar_vertice_maravilla(grafo, 'Taj Mahal')
insertar_arista_maravilla(grafo, 14766, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Gran Muralla China')
des = buscar_vertice_maravilla(grafo, 'Machu Picchu')
insertar_arista_maravilla(grafo, 17083, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Gran Muralla China')
des = buscar_vertice_maravilla(grafo, 'Petra')
insertar_arista_maravilla(grafo, 6217, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Gran Muralla China')
des = buscar_vertice_maravilla(grafo, 'Taj Mahal')
insertar_arista_maravilla(grafo, 2982, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Machu Picchu')
des = buscar_vertice_maravilla(grafo, 'Petra')
insertar_arista_maravilla(grafo, 12547, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Machu Picchu')
des = buscar_vertice_maravilla(grafo, 'Taj Mahal')
insertar_arista_maravilla(grafo, 16941, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Petra')
des = buscar_vertice_maravilla(grafo, 'Taj Mahal')
insertar_arista_maravilla(grafo, 4396, ori, des)

ori = buscar_vertice_maravilla(grafo, 'Amazonia')
des = buscar_vertice_maravilla(grafo, 'Bahía de Ha-Long')
insertar_arista_maravilla(grafo, 18141, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Amazonia')
des = buscar_vertice_maravilla(grafo, 'Cataratas del Iguazú')
insertar_arista_maravilla(grafo, 979, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Amazonia')
des = buscar_vertice_maravilla(grafo, 'Isla Jeju')
insertar_arista_maravilla(grafo, 16970, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Amazonia')
des = buscar_vertice_maravilla(grafo, 'Montaña de la Mesa')
insertar_arista_maravilla(grafo, 8403, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Amazonia')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional de Komodo')
insertar_arista_maravilla(grafo, 18420, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Amazonia')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional del río subterráneo de Puerto Princesa')
insertar_arista_maravilla(grafo, 19458, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Bahía de Ha-Long')
des = buscar_vertice_maravilla(grafo, 'Cataratas del Iguazú')
insertar_arista_maravilla(grafo, 18141, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Bahía de Ha-Long')
des = buscar_vertice_maravilla(grafo, 'Isla Jeju')
insertar_arista_maravilla(grafo, 3109, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Bahía de Ha-Long')
des = buscar_vertice_maravilla(grafo, 'Montaña de la Mesa')
insertar_arista_maravilla(grafo, 10356, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Bahía de Ha-Long')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional de Komodo')
insertar_arista_maravilla(grafo, 1756, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Bahía de Ha-Long')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional del río subterráneo de Puerto Princesa')
insertar_arista_maravilla(grafo, 1464, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cataratas del Iguazú')
des = buscar_vertice_maravilla(grafo, 'Isla Jeju')
insertar_arista_maravilla(grafo, 16970, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cataratas del Iguazú')
des = buscar_vertice_maravilla(grafo, 'Montaña de la Mesa')
insertar_arista_maravilla(grafo, 8403, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cataratas del Iguazú')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional de Komodo')
insertar_arista_maravilla(grafo, 18420, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Cataratas del Iguazú')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional del río subterráneo de Puerto Princesa')
insertar_arista_maravilla(grafo, 19458, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Isla Jeju')
des = buscar_vertice_maravilla(grafo, 'Montaña de la Mesa')
insertar_arista_maravilla(grafo, 13165, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Isla Jeju')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional de Komodo')
insertar_arista_maravilla(grafo, 4322, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Isla Jeju')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional del río subterráneo de Puerto Princesa')
insertar_arista_maravilla(grafo, 2628, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Montaña de la Mesa')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional de Komodo')
insertar_arista_maravilla(grafo, 10051, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Montaña de la Mesa')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional del río subterráneo de Puerto Princesa')
insertar_arista_maravilla(grafo, 11559, ori, des)
ori = buscar_vertice_maravilla(grafo, 'Parque Nacional de Komodo')
des = buscar_vertice_maravilla(grafo, 'Parque Nacional del río subterráneo de Puerto Princesa')
insertar_arista_maravilla(grafo, 1748, ori, des)

print('BARRIDO MARAVILLAS')
barrido_grafo_maravilla(grafo)

# c
print('Arbol de expansión mínimo de las maravillas Arquitectónicas')
bosque = prim_arq(grafo)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

print('Arbol de expansión mínimo de las maravillas Naturales')
bosque = prim_nat(grafo)
for i in range(0,len(bosque),2):
    print(bosque[i], '|',bosque[i+1])
print()

# d
control = input('Ingrese país a investigar: ')
aux = grafo.inicio
arq, nat = 0, 0
while aux is not None:
    if aux.info.ubicacion.find(control) > -1:
        print(control, 'dispone de la maravilla:', aux.info.nombre, 'del tipo', aux.info.tipo)
        if aux.info.tipo == 'Arquitectónica':
            arq += 1
        else:
            nat += 1
    aux = aux.sig
print()

# e
if arq > 1:
    print(control, 'tiene más de una maravilla del tipo Arquitectónica')
if nat > 1:
    print(control, 'tiene más de una maravilla del tipo Natural')
