import os


class Catalogo:
    ruta_archivo = 'peliculas.txt'

    # Metodo de agregación
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='UTF8') as archivo:
            archivo.write(f'{pelicula._nombre}\n')

    # Listado de Peliculas
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='UTF8') as archivo:
            print(f'Catalogo Peliculas'.center(50, '-'))
            print(archivo.read())

    # Eliminación de archivo
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado -> {cls.ruta_archivo}')
