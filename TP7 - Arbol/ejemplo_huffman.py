from TDA_ArbolBin import Nodo_ArbolHuffman, insertar_nodo, por_nivel
from sys import getsizeof

tabla = [['A', 0.2], ['F', 0.17], ['1', 0.13], ['3', 0.21], ['0', 0.05], ['M', 0.09], ['T', 0.15]]

dic = {'A' : '00', '3': '01', '1' : '100', 'T': '110', 'F' : '111', '0': '1010', 'M' : '1011'}


def como_comparo(elemento):
    return elemento[1]

def como_comparo_nodo(elemento):
    return elemento.valor

tabla.sort(key=como_comparo)

bosque = []

for elemento in tabla:
    nodo = Nodo_ArbolHuffman(elemento[0], elemento[1])
    bosque.append(nodo)

for elemento in bosque:
    print(elemento.info, elemento.valor)
print()
while len(bosque) > 1:
    elemento1 = bosque.pop(0)
    elemento2 = bosque.pop(0)
    nodo = Nodo_ArbolHuffman('', elemento1.valor+elemento2.valor)
    nodo.izq = elemento1
    nodo.der = elemento2
    bosque.append(nodo)
    bosque.sort(key=como_comparo_nodo)


#por_nivel(bosque[0])

def generar_tabla(raiz, cadena=''):
    if raiz is not None:
        if raiz.izq is None:
            print(raiz.info, cadena)
        else:
            cadena += '0'
            generar_tabla(raiz.izq, cadena)
            cadena = cadena[0:-1]
            cadena += '1'
            generar_tabla(raiz.der, cadena)


generar_tabla(bosque[0])

def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while pos < len(cadena):
        if cadena[pos] == '0':
            raiz_aux = raiz_aux.izq
        else:
            raiz_aux = raiz_aux.der
        pos += 1
        if raiz_aux.izq is None:
            cadena_deco += raiz_aux.info
            raiz_aux = arbol_huff
        cadena_deco
    return cadena_deco


def codificar(cadena, dic):
    cadena_cod = ''
    for caracter in cadena:
        cadena_cod += dic[caracter]
    return cadena_cod


print()
cadena = "AA31TF0AAMMMMMM0000"
cadena_cod = codificar(cadena, dic)
print(cadena_cod)
print(getsizeof(cadena_cod), getsizeof(b'000001100110111101000001011101110111011101110111010101010101010'))
print('cadena decodificada')
cadena_deco = decodificar(cadena_cod, bosque[0])
print(cadena_deco)
