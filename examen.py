from autor import *
from libro import *
"""
2. Crea una clase Libro en un fichero libro.py que tenga un campo autor, un campo titulo
y un campo anyo con estos nombres. Crea tambi´en una clase Autor en un fichero autor.py
que tenga un campo id_autor, un campo nombre y un campo apellido.
En el main de examen.py se crear´a una lista de varios objetos Libro y se llamar´a a
una funci´on mas_antiguos pas´andole esta lista y un a˜no. La funci´on devolver´a una lista
de los t´ıtulos de libros (´unicamente el t´ıtulo) cuyo a˜no es igual o anterior al pasado
por par´ametro. Si se le pasa un a˜no menor que 1900 o mayor que 2021, se emitir´a una
excepci´on ValueError indicando que el a˜no no es v´alido.
Se pide tambi´en hacer por lo menos 3 tests significativos para probar la funcionalidad
de mas_antiguos

"""

def get_list(filename):
    word_dic = {}
    f = open(filename, mode="rt", encoding="utf-8")
    file_isempty = True
    for linea in f:
        l = linea.split(" ")
        for word in l:    
            file_isempty = False
            word = word.strip()
            word_length = len(word)
            if str(word_length) in word_dic:
                if word not in word_dic[str(word_length)]:
                    word_dic[str(word_length)].append(word)
            else:
                word_dic[str(word_length)] = [word]
    if file_isempty:
        raise ValueError("File is empty.")
    print(word_dic)
    f.close()

def ejercicio1():
    try:
        get_list("palabras.txt")
    except ValueError:
        print("File is empty.")

def ejercicio2():
    autor1 = Autor("AA123","Pedro","Ramirez Espinosa")
    autor2 = Autor("BA443","Julio","Mendez Ramirez")
    autor3 = Autor("AG553","Fabio","Espinola Jimenez")

    lista_libros=[]
    lista_libros.append(Libro(autor1,"Cómo ser rico", 1992), autor2,"Geranios y sus misterios", 1992), autor3,"El temible pollo", 1992),)

    try:
        get_list("palabras.txt")
    except ValueError:
        print("File is empty.")

ejercicio1()
ejercicio2()