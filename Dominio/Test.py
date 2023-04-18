from Dominio.Peliculas import Pelicula
from Servicio.Catalogo import Catalogo

op = None
while op != 4:
    try:
        print('Opciones'.center(30, '-'))
        print('1- Agregar peliculas')
        print('2- Listar')
        print('3- Eliminar')
        print('4 Salir')
        op = int(input(' Seleccione una opcion: '))

        if op == 1:
            nombre_pelicula = input('Ingrese el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            Catalogo.agregar_pelicula(pelicula)

        elif op == 2:
            Catalogo.listar_peliculas()

        elif op == 3:
            Catalogo.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error {e}')
        op = None
else:
    print('Gracias por usar el programa')
