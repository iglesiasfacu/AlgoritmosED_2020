from TDA_ArbolBin import insertar_nodo_morse, por_nivel, descifrar_morse

print('EJERCICIO 14')
print()

arbol = None
mensaje = ''
alfabeto = [[200, ''], [120,'e'], [290,'t'], [70,'i'], [150,'a'], [250,'n'], [340,'m'],
            [40,'s'], [90,'u'], [130,'r'], [170,'w'], [230,'d'], [270,'k'], [320,'g'], 
            [370,'o'], [20,'h'], [50,'v'], [80,'f'], [100,''], [120,'l'], [140,''], 
            [160,'p'], [180,'j'], [220,'b'], [240,'x'], [260,'c'], [280,'y'], [310,'z'],
            [330,'q'], [360,''], [390,''], [10,'5'], [30,'4'], [60,'3'], [110,'2'],
            [190,'1'], [210,'6'], [300,'7'], [350,'8'], [380,'9'], [400,'0']]


for letra in alfabeto:
    arbol = insertar_nodo_morse(arbol, letra)

print('Abecedario Morse')
por_nivel(arbol)
print()


m1 = '.--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- / .--. .-. --- -- . - .- -- . / .- .-.. --. --- / --.- ..- . / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. --- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- / ... .. -. --- / ..- -. / -... ..- . -. / .... --- -- -... .-. . .-.-.'
m2 = '-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-.'
m3 = '-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... .. / . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-.'
m4 = '-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- / ..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-.'
m5 = '.--. --- -.. .-. .. .- / .... .- -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. / -.. .. .- .-.-.'

print('Mensaje de Dr. Abraham Erskine:', descifrar_morse(arbol, m1, mensaje))
print()
print('Mensaje de Rocket Raccoon:', descifrar_morse(arbol, m2, mensaje))
print()
print('Mensaje de Natasha Romanoff:', descifrar_morse(arbol, m3, mensaje))
print()
print('Mensaje de Tony Stark:', descifrar_morse(arbol, m4, mensaje))
print()
print('Mensaje de Steve Rogers:', descifrar_morse(arbol, m5, mensaje))
