from multimethod import multimethod
import math
class PoligonoRegular:
    @multimethod
    def __init__(self):
        self.__n = 3
        self.__lado = 1
        self.__x = 0
        self.__y = 0
    @multimethod
    def __init__(self,n: int, lado: float):
        self.__n = n
        self.__lado = lado
        self.__x = 0
        self.__y = 0
    @multimethod
    def __init__(self,n: int, lado: float, x: float, y: float):
        self.__n = n
        self.__lado = lado
        self.__x = x
        self.__y = y
    def getPerimetro(self):
        return self.__n * self.__lado
    def getArea(self):
        return (self.__n * (self.__lado**2)) / (4 * math.tan(math.pi/self.__n))
class Main:
    p1 = PoligonoRegular()
    print(p1.getPerimetro())
    print(p1.getArea())
    p2 = PoligonoRegular(6, 4.0)
    print(p2.getPerimetro())
    print(p2.getArea())
    p3 = PoligonoRegular(10, 4.0, 5.6, 7.8)
    print(p3.getPerimetro())
    print(p3.getArea())    