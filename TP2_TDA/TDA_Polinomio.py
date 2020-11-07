def crear_polinomio(grado):
    '''Crea un polinomio de grado termino'''
    return [0] * (grado + 1)


def multiplicar(pol1, pol2):
    '''Multiplica dos polinomios'''
    pass


def modificar_termino(pol, termino, valor):
    pol[termino] = valor


def sumar_polinomios(pol1, pol2):
    '''Suma dos polinomios'''
    vaux = None
    if (len(pol1) > len(pol2)):
        vaux = crear_polinomio(len(pol1) - 1)
    else:
        vaux = crear_polinomio(len(pol2) - 1)
    for i in range(0, len(vaux)):
        if (i < len(pol1) and i < len(pol2)):
            vaux[i] = pol1[i] + pol2[i]
        elif (i < len(pol1)):
            vaux[i] = pol1[i]
        else:
            vaux[i] = pol2[i]
    return vaux
