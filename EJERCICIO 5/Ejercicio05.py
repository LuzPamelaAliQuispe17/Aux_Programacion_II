class Animal:
    def __init__(self, nombre, edad, nombreDueno):
        self._nombre = nombre
        self._edad = edad
        self._nombreDueno = nombreDueno

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getDueno(self):
        return self._nombreDueno

    def __str__(self):
        return f"Animal: {self._nombre}, Edad: {self._edad}, Dueño: {self._nombreDueno}"


class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueno, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueno)
        self.__requiereBosal = requiereBosal
        self.__ladraFuerte = ladraFuerte

    def __str__(self):
        return super().__str__() + f" requiere bosal: {self.__requiereBosal}, ladra fuerte: {self.__ladraFuerte}"


class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueno, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueno)
        self.__cazaRatones = cazaRatones
        self.__tomaLeche = tomaLeche

    def tomaLeche(self):
        return self.__tomaLeche

    def __str__(self):
        return super().__str__() + f" cazador de ratones: {self.__cazaRatones}, toma leche: {self.__tomaLeche}"


class CentroVeterinario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__perros = []
        self.__gatos = []
        self.__cantPerros = 0
        self.__cantGatos = 0
   
    def getNombre(self):
        return self.__nombre


    def agregarPerro(self, perro):
        if len(self.__perros) < 100:
            self.__perros.append(perro)
            self.__cantPerros += 1

    def agregarGato(self, gato):
        if len(self.__gatos) < 100:
            self.__gatos.append(gato)
            self.__cantGatos += 1

    def ordenarPerros(self):
        n = len(self.__perros)
        for i in range(n):
            for j in range(0, n - i - 1):

                if self.__perros[j].getEdad() > self.__perros[j + 1].getEdad():
                    aux = self.__perros[j]
                    self.__perros[j] = self.__perros[j + 1]
                    self.__perros[j + 1] = aux

                elif self.__perros[j].getEdad() == self.__perros[j + 1].getEdad():

                    if self.__perros[j].getDueno() > self.__perros[j + 1].getDueno():
                        aux = self.__perros[j]
                        self.__perros[j] = self.__perros[j + 1]
                        self.__perros[j + 1] = aux

                    elif self.__perros[j].getDueno() == self.__perros[j + 1].getDueno():

                        if self.__perros[j].getNombre() > self.__perros[j + 1].getNombre():
                            aux = self.__perros[j]
                            self.__perros[j] = self.__perros[j + 1]
                            self.__perros[j + 1] = aux

    def ordenarGatos(self):
        n = len(self.__gatos)
        for i in range(n):
            for j in range(0, n - i - 1):

                if self.__gatos[j].tomaLeche() == False and self.__gatos[j + 1].tomaLeche() == True:
                    aux = self.__gatos[j]
                    self.__gatos[j] = self.__gatos[j + 1]
                    self.__gatos[j + 1] = aux

                elif self.__gatos[j].tomaLeche() == self.__gatos[j + 1].tomaLeche():

                    if self.__gatos[j].getEdad() < self.__gatos[j + 1].getEdad():
                        aux = self.__gatos[j]
                        self.__gatos[j] = self.__gatos[j + 1]
                        self.__gatos[j + 1] = aux

                    elif self.__gatos[j].getEdad() == self.__gatos[j + 1].getEdad():

                        if self.__gatos[j].getNombre() > self.__gatos[j + 1].getNombre():
                            aux = self.__gatos[j]
                            self.__gatos[j] = self.__gatos[j + 1]
                            self.__gatos[j + 1] = aux

    def verificarDueno(self):
        animales = self.__perros + self.__gatos
   
        for i in range(len(animales)):
   
            contador = 0
   
            for j in range(len(animales)):
                if animales[j].getDueno() == animales[i].getDueno():
                    contador += 1
   
            repetido = False
            for k in range(i):
                if animales[k].getDueno() == animales[i].getDueno():
                    repetido = True
   
            if contador > 1 and repetido == False:
                print(f"{animales[i].getDueno()} tiene {contador} animales")  
           

class Main():
    cv1 = CentroVeterinario("Veterinaria Huellas")

    p1 = Perro("Max", 5, "Juan", True, True)
    p2 = Perro("Rocky", 3, "Ana", False, True)

    g1 = Gato("Michi", 2, "Juan", True, True)
    g2 = Gato("Luna", 4, "Carlos", False, False)

    cv1.agregarPerro(p1)
    cv1.agregarPerro(p2)
    cv1.agregarGato(g1)
    cv1.agregarGato(g2)

    cv1.ordenarPerros()
    cv1.ordenarGatos()
    cv1.verificarDueno()

    print(cv1.getNombre())

    print("Cantidad de perros:", cv1._CentroVeterinario__cantPerros)
    print("Cantidad de gatos:", cv1._CentroVeterinario__cantGatos)
    print("Total de animales:", cv1._CentroVeterinario__cantPerros + cv1._CentroVeterinario__cantGatos)
   


    cv2 = CentroVeterinario("Veterinaria La Paz")

    p3 = Perro("Toby", 2, "Luis", False, False)
    p4 = Perro("Firulais", 6, "Ana", True, True)

    g3 = Gato("Nina", 1, "Luis", True, True)
    g4 = Gato("Pelusa", 3, "Ana", False, True)

    cv2.agregarPerro(p3)
    cv2.agregarPerro(p4)
    cv2.agregarGato(g3)
    cv2.agregarGato(g4)
    cv2.ordenarPerros()
    cv2.ordenarGatos()
    cv2.verificarDueno()

    print(cv2.getNombre())
    print("Cantidad de perros:", cv2._CentroVeterinario__cantPerros)
    print("Cantidad de gatos:", cv2._CentroVeterinario__cantGatos)
    print("Total de animales:", cv2._CentroVeterinario__cantPerros + cv2._CentroVeterinario__cantGatos)

