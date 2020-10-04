from TDA_ColaDin import Cola, arribo, atencion, cola_vacia
from TDA_Archivo import abrir, leer
# No van: 2 3 7 10 13 18 22 24

class Nodo_Arbol():
    def __init__(self, info, nrr=None):
        self.info = info
        self.izq = None
        self.der = None
        self.nrr = nrr
        self.altura = 0

class Nodo_ArbolHuffman(): 
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor


def insertar_nodo(raiz, dato, nrr=None):
    'Agrega elementos a un arbol'
    if raiz is None:
        raiz = Nodo_Arbol(dato, nrr)
    else:
        if raiz.info > dato:
            raiz.izq = insertar_nodo(raiz.izq, dato, nrr)
        else:
            raiz.der = insertar_nodo(raiz.der, dato, nrr)
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz


def busqueda_arbol(raiz, buscado):
    'Busca un elemento en un arbol'
    if raiz is not None:
        if raiz.info == buscado:
            return raiz
        else:
            if buscado < raiz.info:
                return busqueda_arbol(raiz.izq, buscado)
            else:
                return busqueda_arbol(raiz.der, buscado)


def busqueda_proximidad(raiz, buscado):
    if raiz is not None:
        if raiz.info[0:len(buscado)] == buscado:
            print('Se encontro:', raiz.info)
        busqueda_proximidad(raiz.izq, buscado)
        busqueda_proximidad(raiz.der, buscado)


def reemplazar(raiz):
    aux = None
    if raiz.der is None:
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = reemplazar(raiz.der)
    return raiz, aux


def eliminar_nodo(raiz, clave):
    'Elimina un elemento de un arbol'
    x = None   # x elemento a eliminar
    if raiz is not None:
        if clave < raiz.info:
            raiz.izq, x = eliminar_nodo(raiz.izq, clave)
        elif clave > raiz.info:
            raiz.der, x = eliminar_nodo(raiz.der, clave)
        else:
            x = raiz.info
            if raiz.izq is None:
                raiz = raiz.der
            elif raiz.der is None:
                x = raiz.info
                raiz = raiz.izq
            else:
                raiz.izq, aux = reemplazar(raiz.izq)
                raiz.info = aux.info
    raiz = balancear(raiz)
    actualizar_altura(raiz)
    return raiz, x


def arbol_vacio(raiz):
    'Devuelve True si el arbol esta vacio'
    return raiz is None


def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)


def postorden(raiz):
    if raiz is not None:
        postorden(raiz.der)
        print(raiz.info)
        postorden(raiz.izq)


def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def por_nivel(raiz):
    'Barrido por nivel'
    cola = Cola()
    arribo(cola, raiz)
    while not cola_vacia(cola):
        nodo = atencion(cola)
        print(nodo.info)
        if nodo.izq is not None:
            arribo(cola, nodo.izq)
        if nodo.der is not None:
            arribo(cola, nodo.der)


def inorden_marvel(raiz):
    if raiz is not None:
        inorden_marvel(raiz.izq)
        print(raiz.info, raiz.nrr)
        inorden_marvel(raiz.der)


def inorden_villanos(raiz):
    if raiz is not None:
        inorden_villanos(raiz.izq)
        if raiz.nrr is False:
            print(raiz.info)
        inorden_villanos(raiz.der)


def superheroes_c(raiz):
    if raiz is not None:
        superheroes_c(raiz.izq)
        if raiz.nrr is True and raiz.info[0][0] == 'C':
            print(raiz.info)
        superheroes_c(raiz.der)


def generar_bosque(arbol, arbol_superheroes, arbol_villanos):
    if arbol is not None:
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.izq, arbol_superheroes, arbol_villanos)
        if arbol.nrr is True:
            arbol_superheroes = insertar_nodo(arbol_superheroes, arbol.info)
        else:
            arbol_villanos = insertar_nodo(arbol_villanos, arbol.info)
        arbol_superheroes, arbol_villanos = generar_bosque(arbol.der, arbol_superheroes, arbol_villanos)
    return arbol_superheroes, arbol_villanos


def cantidad_nodos(arbol, cont=0):
    'Devuelve la cantidad de nodos de un arbol'
    if arbol is not None:
        cont = cantidad_nodos(arbol.izq, cont)
        cont += 1
        cont = cantidad_nodos(arbol.der, cont)
    return cont


def altura(raiz):
    '''Devuelve la altura de un nodo'''
    if raiz is None:
        return -1
    else:
        return raiz.altura


def actualizar_altura(raiz):
    if raiz is not None:
        alt_izq = altura(raiz.izq)
        alt_der = altura(raiz.der)
        raiz.altura = (alt_izq if alt_izq > alt_der else alt_der) + 1


def rotar_simple(raiz, control):
    '''Realiza una rotación simple de nodos a la derecha o a la izquierda'''
    if control:
        aux = raiz.izq
        raiz.izq = aux.der
        aux.der = raiz
    else:
        aux = raiz.der
        raiz.der = aux.izq
        aux.izq = raiz
    actualizar_altura(raiz)
    actualizar_altura(aux)
    raiz = aux
    return raiz


def rotar_doble(raiz, control):
    '''Realiza una rotación doble de nodos a la derecha o a la izquierda'''
    if control:
        raiz.izq = rotar_simple(raiz.izq, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.der = rotar_simple(raiz.der, True)
        raiz = rotar_simple(raiz, False)
    return raiz


def balancear(raiz):
    '''Determina que rotación hay que hacer para balancear el árbol'''
    if raiz is not None:
        if altura(raiz.izq)-altura(raiz.der) == 2:
            if altura(raiz.izq.izq) >= altura(raiz.izq.der):
                raiz = rotar_simple(raiz, True)
            else:
                raiz = rotar_doble(raiz, True)
        elif altura(raiz.der)-altura(raiz.izq) == 2:
            if altura(raiz.der.der) >= altura(raiz.der.izq):
                raiz = rotar_simple(raiz, False)
            else:
                raiz = rotar_doble(raiz, False)
    return raiz


def hijo_der(arbol):
    if arbol.der is None:
        print(arbol.der)
    else:
        print(arbol.der.info)


def hijo_izq(arbol):
    if arbol.izq is None:
        print(arbol.izq)
    else:
        print(arbol.izq.info)


def par_impar(raiz, cp, ci):
    'Cuenta la cantidad de numeros pares e impares de un arbol'
    if raiz is not None:
        if raiz.info % 2 == 0:
            cp += 1
        else:
            ci += 1
        cp, ci = par_impar(raiz.izq, cp, ci)
        cp, ci = par_impar(raiz.der, cp, ci)
    return cp, ci


def contar_ocurrencias(raiz, buscado, cantidad):
    'Determina la cantidad de ocurrencias de un determinado numero'
    if raiz is not None:
        if raiz.info == buscado:
            cantidad += 1
            cantidad = contar_ocurrencias(raiz.der, buscado, cantidad)
        else:
            cantidad = contar_ocurrencias(raiz.izq, buscado, cantidad)
    return cantidad


def inorden_lightsaber(raiz, archivo):
    if raiz is not None:
        inorden_lightsaber(raiz.izq, archivo)
        jedi = leer(archivo, raiz.nrr)
        if jedi[4].find('green') > -1:
            print(raiz.info, jedi[4])
        inorden_lightsaber(raiz.der, archivo)


def inorden_name(raiz, archivo, jedis):
    if raiz is not None:
        inorden_name(raiz.izq, archivo, jedis)
        jedi = leer(archivo, raiz.nrr)
        jedis.append(jedi)
        inorden_name(raiz.der, archivo, jedis)


def padre(raiz, buscado):
    if raiz is not None:
        if raiz.der is not None and raiz.der.info == buscado or raiz.izq is not None and raiz.izq.info == buscado:
            print('el padre de buscado es', raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


def nodo_minimo(raiz):
    '''Obtiene el nodo minimo de un arbol'''
    if raiz.izq is not None:
        raiz = nodo_minimo(raiz.izq)
    return raiz


def nodo_maximo(raiz):
    '''Obtiene el nodo maximo de un arbol'''
    if raiz.der is not None:
        raiz = nodo_maximo(raiz.der)
    return raiz



'''
arbol = None
arbol = insertar_nodo(arbol, 5)
arbol = insertar_nodo(arbol, 3)
arbol = insertar_nodo(arbol, 4)
arbol = insertar_nodo(arbol, 7)
arbol = insertar_nodo(arbol, 9)
arbol = insertar_nodo(arbol, 0)
arbol = insertar_nodo(arbol, 1)
arbol = insertar_nodo(arbol, 6)

arbol, dato = eliminar_nodo(arbol, 5)
inorden(arbol)'''