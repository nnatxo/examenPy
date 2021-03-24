from autor import *
from libro import *

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

def mas_antiguos(book_list, year):
    if year > 2021 or year < 1900:
        raise ValueError("Year is not valid.")
    ar = [x.get_data()[1] for x in book_list if x.get_data()[2] <= year]
    return ar
def ejercicio1():
    print("------ Ejercicio 1 -------")
    try:
        get_list("palabras.txt")
    except ValueError:
        print("File is empty.")

def ejercicio2():
    print("------ Ejercicio 2 -------")
    autor1 = Autor("AA123","Pedro","Ramirez Espinosa")
    autor2 = Autor("BA443","Julio","Mendez Ramirez")
    autor3 = Autor("AG553","Fabio","Espinola Jimenez")
    lista_libros=[Libro(autor1,"Cómo hacerse rico con inmuebles", 1992), Libro(autor2,"Geranios y sus misterios", 2007), Libro(autor3,"El temible hombre pollo", 2021), Libro(autor1,"Cómo perdí mi casa y mi familia", 2014)]

    try:
        lista_titulos = mas_antiguos(lista_libros, 2021)
        for i in lista_titulos:
            print i
    except ValueError:
        print("Year is not valid.")

ejercicio1()
ejercicio2()