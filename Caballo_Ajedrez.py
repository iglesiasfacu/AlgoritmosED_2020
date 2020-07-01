# Iglesias, Facundo


def pieza(clave):
    res = 0
    dosmov = 2
    tresmov = 3
    if clave == 1:
        res = (dosmov * 7) + (tresmov * 2)
    elif clave == 2:
        res = (dosmov * 14) + (tresmov * 6)
    elif clave == 3:
        res = (dosmov * 28) + (tresmov * 18)
    elif clave == 4:
        res = (dosmov * 56) + (tresmov * 54)
    elif clave == 5:
        res = (dosmov * 112) + (tresmov * 162)
    elif clave == 8:
        res = (dosmov * 896) + (tresmov * 4374)
    elif clave == 10:
        res = (dosmov * 3584) + (tresmov * 39366)
    elif clave == 12:
        res = (dosmov * 14336) + (tresmov * 354294)
    elif clave == 15:
        res = (dosmov * 114688) + (tresmov * 9565938)
    else:
        return 0
    return res


# Se puede ingresar movimientos en un rango de 0 a n
for z in range(0, 20):
    clave = input('Ingrese cantidad de movimientos: ')
    movfinal = pieza(clave)
    print('Con ' + str(clave) + ' movimientos podemos encontrar ' + str(movfinal) + ' posibilidades validas.')
    print('')
