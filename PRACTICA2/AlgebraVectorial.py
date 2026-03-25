from multimethod import multimethod
import math
class AlgebraVectorial:
    @multimethod
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__z = 0
    @multimethod
    def __init__(self, x: int, y: int, z: int):
        self.__x = x
        self.__y = y  
        self.__z = z  
    @multimethod
    def norma(self):
        n = math.sqrt((self.__x)**2 + (self.__y)**2 + (self.__z)**2) 
        return n
    @multimethod
    def norma(self, otroV: AlgebraVectorial):
        n = math.sqrt((otroV.__x)**2 + (otroV.__y)**2 + (otroV.__z)**2) 
        return n
    @multimethod
    def perpendicular(self, otroV: AlgebraVectorial):
            v1 = [self.__x + otroV.__x, self.__y + otroV.__y, self.__z + otroV.__z]
            v2 = [self.__x - otroV.__x, self.__y - otroV.__y, self.__z - otroV.__z]
            if v1 == v2:
                return f"son perpendiculares"
            else:
                return f"no son perpendiculares"
    @multimethod
    def perpendicular(self, otroV: AlgebraVectorial, x: str):
            v1 = [self.__x - otroV.__x, self.__y - otroV.__y, self.__z - otroV.__z]
            v2 = [otroV.__x - self.__x, otroV.__y - self.__y, otroV.__z - self.__z]
            if v1 == v2:
                return f"son perpendiculares"
            else:
                return f"no son perpendiculares"
    @multimethod
    def perpendicular(self, otroV: AlgebraVectorial, x: int):
            p = self.__x * otroV.__x + self.__y * otroV.__y + self.__z * otroV.__z
            if p == 0:
                return f"son perpendiculares"
            else:
                return f"no son perpendiculares"
    @multimethod
    def perpendicular(self, otroV: AlgebraVectorial, x: float):
            suma = AlgebraVectorial(self.__x + otroV.__x, self.__y + otroV.__y, self.__z + otroV.__z)
            v1 = suma.norma()**2
            v2 = self.norma()**2 + otroV.norma()**2
            if v1 == v2:
                return f"son perpendiculares"
            else:
                return f"no son perpendiculares"
    @multimethod
    def paralelo(self, otroV: AlgebraVectorial):
        if otroV.__x != 0:
            esc = self.__x / otroV.__x
        elif(otroV.__y != 0):    
            esc = self.__y / otroV.__y
        elif(otroV.__z != 0):
            esc = self.__z / otroV.__z
        else:
            return "vector nulo"
        if (self.__x == esc * otroV.__x and self.__y == esc * otroV.__y and self.__z == esc * otroV.__z):
            return "son paralelos"
        else:
            return "no son paralelos"
    @multimethod
    def paralelo(self, otroV: AlgebraVectorial, x: str):
        i = self.__y * otroV.__z - self.__z * otroV.__y
        j = self.__x * otroV.__z - self.__z * otroV.__x
        k = self.__x * otroV.__y - self.__y * otroV.__x
        if i==0 and j==0 and k==0:
            return f"son paralelos"
        else: 
            return f"no son paralelos"
    def proyeccion(self, otroV: AlgebraVectorial):
        esc = (self.__x * otroV.__x + self.__y * otroV.__y + self.__z * otroV.__z)/(self.norma(otroV)**2)
        proya = []
        proya.append(esc*otroV.__x)
        proya.append(esc*otroV.__y)
        proya.append(esc*otroV.__z)
        return proya
    def componente(self, otroV: AlgebraVectorial):
        comp = (self.__x * otroV.__x + self.__y * otroV.__y + self.__z * otroV.__z)/ self.norma(otroV)
        return comp
    def __str__(self):
        return f"x: {self.__x}, y: {self.__y}, z: {self.__z}"
class Main:
    a = AlgebraVectorial()
    print("a: ", a)
    b = AlgebraVectorial(2,4,6)
    print("b: ", b)
    c = AlgebraVectorial(1,2,3)
    print("c: ", c)
    print(a.perpendicular(b))    
    print(a.perpendicular(b, ""))    
    print(a.perpendicular(b, 1))    
    print(a.perpendicular(b, 1.0))    
    print(b.paralelo(c))
    print(b.paralelo(c, ""))
    print(b.proyeccion(c))
    print(b.componente(c))
    
