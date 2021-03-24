import unittest
from examen import *

class Pruebas(unittest.TestCase):

    def test_mas_antiguo(self):
        autor1 = Autor("AA123","Pedro","Ramirez Espinosa")
        autor2 = Autor("BA443","Julio","Mendez Ramirez")
        autor3 = Autor("AG553","Fabio","Espinola Jimenez")

        lista_libros=[Libro(autor1,"Cómo ser rico con inmuebles", 1992), Libro(autor2,"Geranios y sus misterios", 2007), Libro(autor3,"El temible hombre pollo", 2021), Libro(autor1,"Cómo perdí mi casa y mi familia", 2014)]
        try:
            mas_antiguos(lista_libros, 2019)
        """
        self.assertIsInstance(flight3, Flight)
        self.assertIsInstance(flight3, Flight)
        self.assertEqual(seating[18]["E"], ("James", "Ford", "56278665F"))
        self.assertRaisesRegex(ValueError, "Seat already occupied.", f1.reallocate_passenger, "12A", "13B")
        self.assertRaisesRegex(ValueError, "Seat already occupied.", f1.reallocate_passenger, "12A", "13B")
        """


class Suite(unittest.TestSuite):
    def __init__(self):
        super(Suite, self).__init__()        
        self.addTest(Pruebas('test_mas_antiguo'))
        
if __name__ == "__main__":    
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)