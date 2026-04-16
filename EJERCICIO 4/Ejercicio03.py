class Persona:
    def __init__(self, nombre, carnet, edad):
        self._nombre = nombre
        self._carnet = carnet
        self._edad = edad

    def __str__(self):
        return f"Nombre: {self._nombre}\nCarnet: {self._carnet}\nEdad: {self._edad}"


class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.__matricula = matricula
        self.__carrera = carrera

    def __str__(self):
        return super().__str__()+f"\nMatrícula: {self.__matricula}\nCarrera: {self.__carrera}\n------------------------"


class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.__antiguedad = antiguedad
        self.__sueldo = sueldo

    def __str__(self):
        return super().__str__() + f"\nAntigüedad: {self.__antiguedad}\nSueldo: {self.__sueldo}\n------------------------"


def verificar_misma_edad(estudiante, docente):
    if estudiante._edad == docente._edad:
        print(f"El estudiante {estudiante._nombre} tiene la misma edad que el docente {docente._nombre}")


def verificar_misma_carrera(e1, e2):
    if e1._Estudiante__carrera == e2._Estudiante__carrera:
        print("Los estudiantes están en la misma carrera")
    else:
        print("Los estudiantes están en diferentes carreras")

class Main():

    e1 = Estudiante("Ana", 123, 20, 1001, "Ingeniería")
    e2 = Estudiante("Luz", 456, 25, 1002, "Ingeniería")
    d1 = Docente("Mario", 789, 25, 10, 3500)
    
    print("___ ESTUDIANTES ___")
    print(e1)
    print(e2)
    
    print("___ DOCENTE ___")
    print(d1)
    
    verificar_misma_edad(e1, d1)
    verificar_misma_edad(e2, d1)
    
    verificar_misma_carrera(e1, e2)