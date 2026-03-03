class Anime():
    def __init__(self,nombre, genero, nroEpisodios):
        self.nombre=nombre
        self.genero=genero
        self.__nroEpisodios= nroEpisodios
        self.__episodios=[]

    def __str__(self):
        return "Anime [{} , {} , {}]".format(self.nombre, self.genero, self.__nroEpisodios)

class Main():
    A1 = Anime("Naruto", "Shonen", 220)
    print(A1)
    A2 = Anime("Haikyuu!!", "Deportes", 85)
    print(A2)