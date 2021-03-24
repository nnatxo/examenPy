"""
Crea una funci´on llamada get_list que reciba el nombre de un fichero de palabras y devuelva
un diccionario donde la clave de cada elemento sea un n´umero 1, 2, 3 y el valor sea una lista
con las palabras del fichero que tienen esa longitud. Si una palabra aparece repetida, solo se
tendr´a en cuenta una. En cada l´ınea del fichero puede haber m´as de una palabra. Si se le
pasa un fichero que no tiene ninguna palabra, la funci´on emitir´a una excepci´on ValueError
indicando que el fichero est´a vac´ıo.
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
            word = word.strip()
            word_length = len(word)
            if str(word_length) in word_dic:
                if word not in word_dic[str(word_length)]:
                    word_dic[str(word_length)].append(word)
            else:
                word_dic[str(word_length)] = [word]

    print(word_dic)
    f.close()

get_list("palabras.txt")