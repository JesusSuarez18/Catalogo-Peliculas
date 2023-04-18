class Pelicula:

    # Metodo inicializador
    def __init__(self, nombre):
        self._nombre = nombre

    # Metodo Get
    @property
    def nombre(self):
        return self._nombre

    # Metodo Set
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Metodo de retorno tipo String
    def __str__(self):
        return f'Nombre: {self._nombre}'


# Creación de Objetos
if __name__ == '__main__':
    pelicula1 = Pelicula('Cars')
    pelicula2 = Pelicula('Max Steel')
    print(pelicula1)
    print(pelicula2)
