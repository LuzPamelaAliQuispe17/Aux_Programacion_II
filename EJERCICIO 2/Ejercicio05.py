class Minecraft:
    def __init__(self):
        self.__jugadores = []
        self.__diamantes = []

    def addJugador(self, jugador, diamantes):
        if len(self.__jugadores) < 10:
            self.__jugadores.append(jugador)
            self.__diamantes.append(diamantes)
        else:
            print("Servidor lleno")

    def VerificarStacksDiamantes(self):
        for i in range(len(self.__jugadores)):
            stacks = self.__diamantes[i] // 64
            print("{} tiene {} stack de diamantes".format(self.__jugadores[i], stacks))

    def MayorDiamantes(self):
        MayorDiamantes = -1
        nombre = ""
        for i in range(len(self.__jugadores)):
            if self.__diamantes[i] > MayorDiamantes:
                MayorDiamantes = self.__diamantes[i]
                nombre = self.__jugadores[i]
        print("Jugador con más diamantes: {}".format(nombre))

    def totalDiamantes(self):
        total = sum(self.__diamantes)
        print("Total diamantes:", total)

class Main():

    servidor = Minecraft()
    
    servidor.addJugador("Juan",125)
    servidor.addJugador("Alex",288)
    servidor.addJugador("Maria",30)
    servidor.addJugador("Luis",90)
    servidor.addJugador("Ana",64)
    servidor.addJugador("Pedro",140)
    servidor.addJugador("Sofia",200)
    servidor.addJugador("Carlos",50)
    servidor.addJugador("Elena",300)
    servidor.addJugador("Mario",75)
    
    servidor.VerificarStacksDiamantes()
    print("--------------------------------")
    servidor.MayorDiamantes()
    servidor.totalDiamantes()