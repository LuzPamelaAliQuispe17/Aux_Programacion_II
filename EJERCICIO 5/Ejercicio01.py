class Libro:
    def __init__(self, nombre, autor, anio):
        self.__nombre = nombre
        self.__autor = autor
        self.__anio = anio

    def getNombre(self):
        return self.__nombre

    def __str__(self):
        return f"Libro: {self.__nombre}, Autor: {self.__autor}, Año: {self.__anio}"
class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__cantLibros = 0
        self.__libros = []

    def agregarLibro(self, libro):
        if self.__cantLibros < 100:
            self.__libros.append(libro)
            self.__cantLibros += 1
        else:
            print("No se pueden agregar más libros")

    def verificarLibro(self, nombre):
        for libro in self.__libros:
            if libro.getNombre() == nombre:
                print("Libro encontrado:")
                print(libro)
                return
        print("Libro no encontrado")

    def getCantLibros(self):
        return self.__cantLibros

    def __str__(self):
        return f"Biblioteca: {self.__nombre}, Cantidad de libros: {self.__cantLibros}"
class Main():
    l1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    l2 = Libro("1984", "George Orwell", 1949)
    l3 = Libro("El principito", "Antoine de Saint-Exupéry", 1943)
    l4 = Libro("Don Quijote", "Miguel de Cervantes", 1605)
    l5 = Libro("Informatica basica", "Carlos", 2000)
    
    biblio1 = Biblioteca("Biblioteca Central")
    biblio2 = Biblioteca("Biblioteca Informatica")
    
    biblio1.agregarLibro(l1)
    biblio1.agregarLibro(l2)
    
    biblio2.agregarLibro(l3)
    biblio2.agregarLibro(l4)
    biblio2.agregarLibro(l5)
    
    biblio1.verificarLibro("1984")

    
    if biblio1.getCantLibros() > biblio2.getCantLibros():
        print("Biblioteca con más libros:")
        print(biblio1)
    elif biblio2.getCantLibros() > biblio1.getCantLibros():
        print("Biblioteca con más libros:")
        print(biblio2)
    else:
        print("Hay empate entre las bibliotecas:")
        print(biblio1)
        print(biblio2)