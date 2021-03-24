class Libro:
    def __init__(self, autor, titulo, anyo):
        """Create an instance of a Passenger

        Args:
            autor (string): autor del libro
            titulo (string): titulo del libro
            anyo (int): año de publicación
        """
        self.__autor = autor
        self.__titulo = titulo
        self.__anyo = anyo

    def get_data(self):
        """
        Obtains the data of the book
        Returns: tuple of (autor, titulo, anyo)
        """
        return (self.__autor, self.__titulo, self.__anyo)
    