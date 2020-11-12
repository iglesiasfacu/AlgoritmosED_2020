from TDA_ArbolBin import Nodo_Greek, insertar_nario, inorden, preorden
from TDA_ArbolBin import busqueda_nario, por_nivel_nario

print('EJERCICIO 21')
print()

arbol = None

archivo = open('greek_gods')

linea = archivo.readline()

while linea:        
    linea = linea.replace('\n', '')
    dios = linea.split(';')
    nodo = Nodo_Greek(dios[0], dios[2])
    #print('insertar', dios[0])
    if(arbol is None):
        arbol = nodo
    else:
        pos = []
        busqueda_nario(arbol, dios[1], pos)
        #print('resultado de busqueda', pos[0].info)
        insertar_nario(pos[0], nodo)

    linea = archivo.readline()


archivo.close()

print('ARBOL DIOSES')
por_nivel_nario(arbol)
print()

#pos = []
#busqueda_nario(arbol, 'zeus', pos)

#hijo = pos[0].izq

#while hijo is not None:
#    print(hijo.info)
#    hijo = hijo.der

bosque = []
hijo = arbol.izq

while hijo is not None:
    aux = hijo.der
    hijo.der = None
    bosque.append(hijo)
    hijo = aux

print('cantidad de arboles del bosque', len(bosque))
for arbol in bosque:
    print('raiz ------------------>', arbol.info)
    inorden(arbol)
    print()
