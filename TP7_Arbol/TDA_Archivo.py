import shelve


def abrir(ruta):
    '''Crea un nuevo archivo'''
    return shelve.open(ruta)


def cerrar(archivo):
    '''Cierra un archivo existente'''
    archivo.close()


def leer(archivo, pos):
    '''Lee una posicion en el archivo'''
    return archivo[str(pos)]


def guardar(archivo, reg):
    '''Guarda un nuevo registro'''
    archivo[str(len(archivo))] = reg


def modificar(archivo, pos, reg):
    '''Modifica un registro existente'''
    archivo[str(pos)] = reg


'''
arch = abrir('datos')
guardar(arch, 32)
guardar(arch, 99)
for i in range(0, len(arch)):
    print(leer(arch, i))

cerrar(arch)'''
