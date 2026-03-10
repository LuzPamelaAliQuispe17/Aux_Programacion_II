class Televisor:
    def __init__(self, marca="", resolucion=0, tipo=""):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo

    def __str__(self):
        return "Televisor [{} , {} , {}]".format(self.__marca, self.__resolucion, self.__tipo)

class Main():
    T1 = Televisor("Samsung", 4, "OLED")
    print(T1)

    T2 = Televisor("LG", 8, "IPS")
    print(T2)

    T3 = Televisor()
    print(T3)
