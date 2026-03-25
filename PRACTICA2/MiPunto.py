from multimethod import multimethod
import math
class MiPunto: 
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    @multimethod
    def __init__(self):
        self.__x = 0
        self.__y = 0
    @multimethod
    def __init__(self, x: float, y:float):
        self.__x = x
        self.__y = y
    @multimethod
    def distancia(self, otroPunto: MiPunto):
        d = math.sqrt((self.__x - otroPunto.__x)**2 + (self.__y - otroPunto.__y)**2) 
        return d
    @multimethod
    def distancia(self, a: float, b: float):
        d = math.sqrt((self.__x - a)**2 + (self.__y - b)**2)
        return d
    def __str__(self):
        return f"x: {self.getX()}, y: {self.getY()}"

class Main:
    p1 = MiPunto()
    print(p1)
    p2 = MiPunto(10.0, 30.5)
    print(p2)
    print("distancia p1-p2:", p1.distancia(p2))   

    