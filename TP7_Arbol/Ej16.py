from TDA_ArbolBin_AVL import insertar_nodo, Nodo_ArbolHuffman, por_nivel

print('EJERCICIO 16')
print()

tabla = []

archivo = open('valores')

linea = archivo.readline()

print('archivo')
while linea:
    linea = linea.replace('\n', '')
    tabla.append(linea.split(';'))
    linea = archivo.readline()

dic = {}


def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = Nodo_ArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

# for elemento in bosque:
#     print(elemento.info, elemento.valor)
# print()

while(len(bosque) > 1):
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = Nodo_ArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


#por_nivel(bosque[0])

def generar_tabla(raiz, dic, cadena=''):
    if(raiz is not None):
        if(raiz.izq is None):
            dic[raiz.info] = cadena
            #print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, dic, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, dic, cadena)


generar_tabla(bosque[0],dic)
print(dic)
a = input()

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if(raiz_aux.izq is None):
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena.split('-'):
        cadena_cod += dic[caracter]
    return cadena_cod

cadena = "Nublado-Baja-1-5-7"
cadena_cod = codificar(cadena, dic)
print(cadena_cod)
print('cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)