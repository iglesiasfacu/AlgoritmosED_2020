# EJ 1
def fibonacci(n):
    '''Sucesion de fibonacci'''
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# EJ 2
def suma(n):
    '''Sumatoria entre 0 y un numero dado'''
    if n == 0:
        return n
    else:
        return n + suma(n-1)


# EJ 3
def prod(n1, n2):
    '''Producto entre dos numeros'''
    if n2 == 1:
        return n1
    else:
        return n1 + prod(n1, n2-1)


# EJ 4
def potencia(base, exp):
    '''Potencia ingresando base y exponente'''
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp-1)


# EJ 5
def invertir_cadena(cad):
    '''Invierte el contenido de una cadena'''
    if len(cad) == 1:
        return cad
    else:
        return cad[len(cad)-1] + invertir_cadena(cad[0:len(cad)-1])


# EJ 6
def serie(n):
    '''Calculo de la serie h(n) = 1 + 1/2 + 1/3 +...+ 1/n'''
    if n == 1:
        return 1
    else:
        return 1/n + serie(n-1)


# EJ 7
def binario(n):
    '''Conversion de un numero decimal a binario'''
    if n <= 1:
        return str(n)
    else:
        return binario(n//2) + str(n % 2)


# EJ 8
def log(n, b):
    '''Logaritmo entero de un numero n en una base b'''
    if n <= b:
        return 1
    else:
        return 1 + log(n/b, b)


# EJ 9
def contador(n):
    '''Cantidad de digitos de un numero'''
    if n == 0:
        return 0
    else:
        return 1 + contador(n//10)


# EJ 10
def invertir_num(n):
    '''Numero invertido'''
    if n < 10:
        return n
    else:
        return ((n % 10)*(10**contador(n//10))) + invertir_num(n//10)


# EJ 11
def mcd(a, b):
    '''Maximo comun divisor'''
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


# EJ 12
def mcm(a, b):
    '''Minimo comun multiplo'''
    if b % a == 0:
        return b
    else:
        return mcm(b, a * b)


# EJ 13
def suma_digitos(n):
    '''Suma de los digitos de un numero'''
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n//10)


# EJ 14
def raizcuadrada(n1, n2):
    '''Funcion interna de raiz(n)'''
    if((n1 * n1) <= n2):
        return n1
    else:
        return raizcuadrada(n1-1, n2)


def raiz(n):
    '''Raiz cuadrada entera de un numero entero'''
    if n == 0:
        return n
    else:
        return raizcuadrada(n, n)


# EJ 15
def suc_geo(n):
    '''Sucesion geometrica ejercicio 15'''
    if n == 1:
        return 2
    else:
        return (-3 * suc_geo(n-1))


# EJ 16
def vector_inverso(vec, pos):
    '''Valores invertidos de un vector'''
    if pos == -1:
        return vec[pos]
    else:
        print(vec[pos])
        return vector_inverso(vec, pos-1)


# EJ 17
def matriz(i, j, m):
    '''Funcion interna de barrido_matriz(m)'''
    if i == len(m)-1 and j == len(m)-1:
        return m[i][j]
    else:
        if j == len(m)-1:
            print(m[i][j])
            j = 0
            return matriz(i+1, j, m)
        else:
            print(m[i][j])
            return matriz(i, j+1, m)


def barrido_matriz(m):
    '''Recorrido de una matriz y sus valores'''
    i = 0
    j = 0
    return matriz(i, j, m)


# EJ 18
def sucesion(n):
    '''Sucesion recursiva ejercicio 18'''
    if n == 1:
        return 2
    elif n >= 2:
        return n + (1/sucesion(n-1))


# EJ 19
def bsecuencial(vec, pos, busc):
    '''Busqueda secuencial'''
    tam = len(vec)
    if vec[pos] == busc:
        return pos
    elif pos == tam-1:
        return None
    else:
        return bsecuencial(vec, pos+1, busc)


# EJ 20
def bbin(vec, pri, ult, busc):
    '''Busqueda binaria'''
    if pri < ult:
        med = (pri + ult)//2
        if vec[med] == busc:
            return med
        else:
            if vec[med] > busc:
                return bbin(vec, pri, med-1, busc)
            else:
                return bbin(vec, med+1, ult, busc)


# EJ 21
def naves_rebeldes(vec):
    '''Informe del stormtrooper de asalto'''
    if len(vec) == 0:
        return 0
    else:
        if vec[-1][2] == 'Derribado':
            return 1 + naves_rebeldes(vec[0:-1])
        else:
            return 0 + naves_rebeldes(vec[0:-1])


# EJ 22
def matriz_lab(i, j, m):
    '''Funcion interna de barrido_laberinto(m)'''
    mat = len(m)
    if i == mat-1 and j == mat-1:
        return 'Salio del laberinto'
    else:
        if i == mat-1:
            if m[i][j+1] == 0:
                print('Derecha')
                return matriz_lab(i, j+1, m)
            else:
                if m[i-1][j] == 0:
                    print('Arriba')
                    m[i][j] = 1
                    return matriz_lab(i-1, j, m)
        else:
            if j == mat-1:
                if m[i+1][j] == 0:
                    print('Abajo')
                    return matriz_lab(i+1, j, m)
                else:
                    if m[i][j-1] == 0:
                        print('Izquierda')
                        m[i][j] = 1
                        return matriz_lab(i, j-1, m)
            else:
                if m[i+1][j] == 0:
                    print('Abajo')
                    return matriz_lab(i+1, j, m)
                else:
                    if m[i][j+1] == 0:
                        print('Derecha')
                        return matriz_lab(i, j+1, m)
                    else:
                        m[i][j] = 1
                        if m[i-1][j] == 0:
                            print('Arriba')
                            return matriz_lab(i-1, j, m)


def barrido_laberinto(m):
    '''Recorrido del laberinto'''
    i = 0
    j = 0
    return matriz_lab(i, j, m)


# EJ 23
def hanoi(D, A1, A2, A3):
    '''Torres de Hanoi'''
    if D > 0:
        hanoi(D-1, A1, A3, A2)
        print('Se mueve de la torre ' + A1 + ' a la aguja ' + A3)
        hanoi(D-1, A2, A1, A3)


# EJ 24
def suc_geo2(n):
    '''Sucesion geometrica ejercicio 24'''
    if n == 1:
        return 5.25
    else:
        return 4 * suc_geo2(n-1)


def barrido_sucesion():
    for i in range(10, 0, -1):
        print(suc_geo2(i))


# EJ 25
def sucesion2(n):
    '''Sucesion recursiva ejercicio 25'''
    if n == 1:
        return 3
    elif n >= 2:
        return (sucesion2(n-1)) + 2*n
