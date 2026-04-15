import random
class Juego:
    def __init__(self, numeroDeVidas: int, record: int):
        self.__numeroDeVidas = numeroDeVidas
        self.__record = record
        self.vidasIni = self.__numeroDeVidas
        self.recordini = self.__record
    def reiniciarPartida(self):
        self.__numeroDeVidas = self.vidasIni
    def actualizaRecord(self):
        if self.__record >= self.recordini:
           self.__record = self.__record + 1
    def quitaVida(self):
        self.__numeroDeVidas = self.__numeroDeVidas - 1
        if self.__numeroDeVidas > 0:
            return True
        else:
            return False
    def getVidas(self):
        return self.__numeroDeVidas
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas, record, numeroAAdivinar=0):
        super().__init__(numeroDeVidas, record)
        self.__numeroAAdivinar = numeroAAdivinar 
    def juega(self):
        self.reiniciarPartida()
        self.__numeroAAdivinar = random.randint(1,10)
        print("adivina el numero entre el 1 y 10") 
        while True:
            x = int(input())
            if x ==  self.__numeroAAdivinar:
                print("ACERTASTE :)")
                self.actualizaRecord()
                return
            else:
                print("FALLASTE :(")
                if self.quitaVida() == True:
                    if self.__numeroAAdivinar > x:
                        print("te quedan", self.getVidas(), "vidas. El numero a adivinar es mayor. Intenta de nuevo")
                    else:
                        print("te quedan", self.getVidas(), "vidas. El numero a adivinar es menor. Intenta de nuevo")
                else: 
                    print("YA NO TE QUEDAN MAS VIDAS F")
                    return

class Aplicacion:
    def main():
        juego = JuegoAdivinaNumero(3, 0)
        juego.juega()                 

Aplicacion.main()