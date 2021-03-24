import unittest
from examen import *

class Pruebas(unittest.TestCase):

    def test_mas_antiguo(self):
        autor1 = Autor("AA123","Pedro","Ramirez Espinosa")
        autor2 = Autor("BA443","Julio","Mendez Ramirez")
        autor3 = Autor("AG553","Fabio","Espinola Jimenez")
        lista_libros=[Libro(autor1,"Cómo hacerse rico con inmuebles", 1992), Libro(autor2,"Geranios y sus misterios", 2007), Libro(autor3,"El temible hombre pollo", 2021), Libro(autor1,"Cómo perdí mi casa y mi familia", 2014)]
        
        #Testeamos los años inválidos
        self.assertRaisesRegex(ValueError, "Year is not valid.", mas_antiguos, lista_libros, 1437)
        self.assertRaisesRegex(ValueError, "Year is not valid.", mas_antiguos, lista_libros, 2135)

        #Testeamos que funcione bien
        lista_libros_antes_dosmil = mas_antiguos(lista_libros, 2000)
        self.assertEqual(lista_libros_antes_dosmil[0], "Cómo hacerse rico con inmuebles")


class Suite(unittest.TestSuite):
    def __init__(self):
        super(Suite, self).__init__()        
        self.addTest(Pruebas('test_mas_antiguo'))
        
if __name__ == "__main__":    
    runner = unittest.TextTestRunner()
    my_suite = Suite()
    runner.run(my_suite)