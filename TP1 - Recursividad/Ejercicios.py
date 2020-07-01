from Funciones_Recursivas import fibonacci, suma, prod, potencia, suma_digitos
from Funciones_Recursivas import invertir_cadena, serie, binario, log, contador
from Funciones_Recursivas import invertir_num, mcd, mcm, vector_inverso, raiz
from Funciones_Recursivas import barrido_matriz, suc_geo, bbin, bsecuencial
from Funciones_Recursivas import naves_rebeldes, barrido_laberinto, hanoi
from Funciones_Recursivas import sucesion, sucesion2, barrido_sucesion

print('TP1 - RECURSIVIDAD')
print('')

# Declaraciones para ejercicios
vector = [1, 2, 3, 4, 5, 6, 7, 8, 9]
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
laberinto = [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 1, 1, 0, 0],
             [1, 1, 1, 0, 1],
             [1, 1, 1, 0, 0]]
cajanegra = [['Coordenada: 45.54.32.86.04', 'Arma: Torpedo', 'Derribado'],
             ['Coordenada: 76.84.12.05.37', 'Arma: Antiaereo', 'Escapo'],
             ['Coordenada: 32.02.85.01.55', 'Arma: Rifle laser', 'Derribado']]

print('Ejercicio 1')
print(fibonacci(10))
print('')

print('Ejercicio 2')
print(suma(5))
print('')

print('Ejercicio 3')
print(prod(5, 5))
print('')

print('Ejercicio 4')
print(potencia(3, 3))
print('')

print('Ejercicio 5')
print(invertir_cadena('python'))
print('')

print('Ejercicio 6')
print(serie(5))
print('')

print('Ejercicio 7')
print(binario(5))
print('')

print('Ejercicio 8')
print(log(4, 2))
print('')

print('Ejercicio 9')
print(contador(12345))
print('')

print('Ejercicio 10')
print(invertir_num(912))
print('')

print('Ejercicio 11')
print(mcd(40, 80))
print('')

print('Ejercicio 12')
print(mcm(4, 8))
print('')

print('Ejercicio 13')
print(suma_digitos(912))
print('')

print('Ejercicio 14')
print(raiz(25))
print('')

print('Ejercicio 15')
print(suc_geo(5))
print('')

print('Ejercicio 16')
vector_inverso(vector, 8)
print('')

print('Ejercicio 17')
print('Matriz:')
print(barrido_matriz(matriz))
print('')

print('Ejercicio 18')
print(sucesion(10))
print('')

print('Ejercicio 19')
print(bsecuencial(vector, 0, 5))
print('')

print('Ejercicio 20')
print(bbin(vector, 0, 8, 5))
print('')

print('Ejercicio 21')
print('Se derrribaron ' + str(naves_rebeldes(cajanegra)) + ' naves rebeldes')
print('')

print('Ejercicio 22')
print('Laberinto')
print(barrido_laberinto(laberinto))
print('')

print('Ejercicio 23')
hanoi(5, '1', '2', '3')
print('')

print('Ejercicio 24')
barrido_sucesion()
print('')


print('Ejercicio 25')
print(sucesion2(5))
print('')
