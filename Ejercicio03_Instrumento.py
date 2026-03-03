class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return "Instrumento [{} , {} , {}]".format(self.nombre, self.__material, self.__tipo)

class Main():
    I1 = Instrumento("Guitarra", "Madera", "Cuerda")
    print(I1)
    
    I2 = Instrumento("Flauta", "Metal", "Aire")
    print(I2)