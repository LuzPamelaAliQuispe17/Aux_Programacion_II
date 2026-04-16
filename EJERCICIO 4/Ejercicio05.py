from abc import ABC, abstractmethod
import math


class Figura(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def obtenerArea(self):
        pass

    def __str__(self):
        return f"Color: {self._color}"


class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado

    def obtenerArea(self):
        return self.__lado ** 2

    def __str__(self):
        return super().__str__() + f"\nLado: {self.__lado}\nÁrea: {self.obtenerArea()}\n------------------------"


class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def obtenerArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))

    def __str__(self):
        return super().__str__() + f"\nLados: {self.__lado1}, {self.__lado2}, {self.__lado3}\nÁrea: {self.obtenerArea()}\n------------------------"


class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    def obtenerArea(self):
        return math.pi * (self.__radio ** 2)

    def __str__(self):
        return super().__str__()+f"\nRadio: {self.__radio}\nÁrea: {self.obtenerArea()}\n------------------------"


def mayor_area(f1, f2):
    if f1.obtenerArea() > f2.obtenerArea():
        print(f"La figura con mayor área es de color {f1._color}")
    else:
        print(f"La figura con mayor área es de color {f2._color}")


c1 = Cuadrado("Rojo", 4)
c2 = Cuadrado("Azul", 6)

t1 = Triangulo("Verde", 3, 4, 5)
t2 = Triangulo("Amarillo", 5, 5, 6)

r1 = Redondo("Negro", 3)
r2 = Redondo("Blanco", 5)

print("___ CUADRADOS ___")
print(c1)
print(c2)

print("___ TRIANGULOS ___")
print(t1)
print(t2)

print("___ REDONDOS ___")
print(r1)
print(r2)

mayor_area(c1, t1)