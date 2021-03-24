
"""
2. Crea una clase Libro en un fichero libro.py que tenga un campo autor, un campo titulo
y un campo anyo con estos nombres. 

    Crea tambi´en una clase Autor en un fichero autor.py
que tenga un campo id_autor, un campo nombre y un campo apellido.

En el main de examen.py se crear´a una lista de varios objetos Libro y se llamar´a a
una funci´on mas_antiguos pas´andole esta lista y un a˜no. La funci´on devolver´a una lista
de los t´ıtulos de libros (´unicamente el t´ıtulo) cuyo a˜no es igual o anterior al pasado
por par´ametro. Si se le pasa un a˜no menor que 1900 o mayor que 2021, se emitir´a una
excepci´on ValueError indicando que el a˜no no es v´alido.
Se pide tambi´en hacer por lo menos 3 tests significativos para probar la funcionalidad
de mas_antiguos

"""
class Autor:
    def __init__(self, id_autor, nombre, apellido):
        """Create an instance of a Passenger

        Args:
            id_autor (string): id del autor
            nombre (string): nombre del autor
            apellido (int): apellido del autor
        """
        self.__id_autor = id_autor
        self.__nombre = nombre
        self.__apellido = apellido

    def get_data(self):
        """
        Obtains the data of the book
        Returns: tuple of (id_autor, nombre, apellido)
        """
        return (self.__id_autor, self.__nombre, self.__apellido)
    