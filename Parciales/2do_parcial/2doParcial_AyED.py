from TDA_ArbolBin_AVL import insertar_nodo, inorden, busqueda_arbol_vec, por_nivel
from TDA_ArbolBin_AVL import eliminar_nodo_vec, insertar_nodo_vec
from TDA_Heap import Heap, arribo_heap, heap_vacio, atencion_heap
from TDA_Grafo import Grafo, barrido_grafo, buscar_vertice, existe_paso, insertar_arista
from TDA_Grafo import insertar_vertice, prim, adyacentes, dijkstra
from TDA_PilaDin import desapilar, pila_vacia
from random import choice, randint


# punto 1
def punto1():
    arbol = None
    # 1
    personajes = ['Dar Vader', 'Yoda', 'Han Solo', 'Leia Organa', 'C-3PO',
                  'Obi-Wan Kenobi', 'Chewbacca', 'R-2D2', 'Luke Skywalker', 'Greedo']
    pos = 0
    for i in range(len(personajes)):
        dato = [personajes[pos], pos] # nombre personaje | nrr
        arbol = insertar_nodo(arbol, dato)
        pos += 1

    # 2
    print('Listado ordenado alfabéticamente de manera ascendente')
    inorden(arbol)
    print()

    # 3
    pos = busqueda_arbol_vec(arbol, 'Yod')
    if pos is not None:
        print(pos.info[0] ,'se encuentra en la posicion', pos.info[1])
    else:
        print('Yoda NO se encuentra en el arbol')
    print()
    
    # 4 // el nivel de obi wan kenobi aparece dentro de la funcion por_nivel()
    print('Barrido por nivel')
    por_nivel(arbol)
    print()
    
    # 5
    x = 'C-3PO'
    arbol, x = eliminar_nodo_vec(arbol, x)
    print('Se eliminó:', x)
    print()
    print('Nuevo arbol sin C-3PO')
    inorden(arbol)
    print()
    
    # 6
    x = 'Dar Vader'
    arbol, x = eliminar_nodo_vec(arbol, x)
    print('Dar Vader esta mal cargado, modificando...')
    print()
    arbol = insertar_nodo_vec(arbol, ['Darth Vader', 0])
    print('NUEVO ARBOL')
    inorden(arbol)



# punto 2
def punto2():
    cola_prioridad = Heap(10)
    # a b y c
    trajes = ['Mark XLIV', 'Mark XV', 'Mark I', 'Mark V', 'Mark IV', 'Mark II', 'Mark VII']
    estado = ['Producir', 'Reparar']
    pos = 0
    for i in range(len(trajes)):
        arribo_heap(cola_prioridad, trajes[pos], randint(1,3), choice(estado))
        pos += 1
    print()
    print('Se atiende los 3 primeros trajes')
    for i in range(3):
        print(atencion_heap(cola_prioridad))
    print()
    print('Inserto 3 trajes nuevos(Mark XLV, XXL y III)')
    print()
    arribo_heap(cola_prioridad, 'Mark XLV', 3, 'Reparar')
    arribo_heap(cola_prioridad, 'Mark XXL', 2, 'Producir')
    arribo_heap(cola_prioridad, 'Mark III', 1, 'Reparar')

    while not heap_vacio(cola_prioridad):
        print(atencion_heap(cola_prioridad))


# punto 3
def punto3():
    grafo = Grafo(False)

    # a
    insertar_vertice(grafo, 'Guido Rossum')
    insertar_vertice(grafo, 'Mark Hamill')
    insertar_vertice(grafo, 'Tom Holland')
    insertar_vertice(grafo, 'Robert Downey')
    insertar_vertice(grafo, 'Daisy Ridley')
    insertar_vertice(grafo, 'Pedro Pascal')
    insertar_vertice(grafo, 'Adam Driver')

    # b
    ori = buscar_vertice(grafo, 'Tom Holland')
    des = buscar_vertice(grafo, 'Robert Downey')
    insertar_arista(grafo, randint(10000, 50000), ori, des)
    ori = buscar_vertice(grafo, 'Daisy Ridley')
    des = buscar_vertice(grafo, 'Pedro Pascal')
    insertar_arista(grafo, randint(10000, 50000), ori, des)
    ori = buscar_vertice(grafo, 'Daisy Ridley')
    des = buscar_vertice(grafo, 'Adam Driver')
    insertar_arista(grafo, randint(10000, 50000), ori, des)
    ori = buscar_vertice(grafo, 'Adam Driver')
    des = buscar_vertice(grafo, 'Robert Downey')
    insertar_arista(grafo, randint(10000, 50000), ori, des)
    ori = buscar_vertice(grafo, 'Guido Rossum')
    des = buscar_vertice(grafo, 'Pedro Pascal')
    insertar_arista(grafo, randint(10000, 50000), ori, des)
    ori = buscar_vertice(grafo, 'Mark Hamill')
    des = buscar_vertice(grafo, 'Pedro Pascal')
    insertar_arista(grafo, randint(10000, 50000), ori, des)
    ori = buscar_vertice(grafo, 'Daisy Ridley')
    des = buscar_vertice(grafo, 'Mark Hamill')
    insertar_arista(grafo, randint(10000, 50000), ori, des)
    '''ori = buscar_vertice(grafo, 'Mark Hamill')
    des = buscar_vertice(grafo, 'Guido Rossum')
    insertar_arista(grafo, randint(10000, 50000), ori, des)'''

    barrido_grafo(grafo)
    print()

    # c
    print('Arbol de expresion Minimo')
    bosque = prim(grafo)

    for i in range(0,len(bosque),2):
        print(bosque[i], '|', bosque[i+1])
    print()

    # d
    def adyacentes_a(vertice):
        aux = vertice.adyacentes.inicio
        while aux is not None:
            if aux.destino == 'Mark Hamill':
                print('Hay paso entre Guido Rossum y Mark Hamill')
                break
            else:
                print('NO hay paso entre Guido Rossum y Mark Hamill')
            aux = aux.sig
    
    def adyacentes_b(vertice):
        aux = vertice.adyacentes.inicio
        while aux is not None:
            if aux.destino == 'Robert Downey':
                print('Hay paso directo entre Tom Holland y Robert Downey')
                break
            else:
                print('NO hay paso entre Tom Holland y Robert Downey')
            aux = aux.sig

    ori = buscar_vertice(grafo, 'Guido Rossum')
    if ori is not None:
        adyacentes_a(ori)
    print()

    ori = buscar_vertice(grafo, 'Tom Holland')
    if ori is not None:
        adyacentes_b(ori)
    print()

    ori = buscar_vertice(grafo, 'Tom Holland')
    des = buscar_vertice(grafo, 'Robert Downey')
    if existe_paso(grafo, ori, des):
        print('Existe paso indirecto entre Tom Holland y Robert Downey')
    else:
        print('NO')
    print()
    
    # e
    vertice = buscar_vertice(grafo, 'Daisy Ridley')
    if vertice is not None:
        print('Amigos de Daisy Ridley')
        adyacentes(vertice)
    print()
    
    # f
    print('Camino con menor cantidad de me gusta partiendo desde Pedro Pascal hasta Adam Driver.')
    camino_mas_corto = dijkstra(grafo, 'Pedro Pascal', 'Adam Driver')
    fin = 'Adam Driver'
    mg = None
    while not pila_vacia(camino_mas_corto):
        dato = desapilar(camino_mas_corto)
        if mg is None and fin == dato[1][0].info:
            mg = dato[0]
        if fin == dato[1][0].info:
            print(dato[1][0].info)
            fin = dato[1][1]
    print('Cantidad de MG:', mg)



punto1()
#punto2()
#punto3()
