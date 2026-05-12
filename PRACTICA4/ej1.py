class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__librosDisp = []
        self.__autoresReg = []
        self.__prestamosActivos = []
        self.__horarioDeAtencion = None
    class Horario:
        def __init__(self, diasDeApertura, horaDeApertura, horaDeCierre):
            self.__diasDeApertura = diasDeApertura
            self.__horaDeApertura = horaDeApertura
            self.__horaDeCierre = horaDeCierre
        def __str__(self):
            return f"dias de apertura {self.__diasDeApertura}, hora de apertura: {self.__horaDeApertura}, hora de cierre : {self.__horaDeCierre}"

    def setHorario(self, diasDeApertura, horaDeApertura, horaDeCierre):
        h = self.Horario(diasDeApertura, horaDeApertura, horaDeCierre)
        self.__horarioDeAtencion = h
    def agregarLibro(self, l: Libro):
        self.__librosDisp.append(l)        
    def agregarAutor(self, a: Autor):
        self.__autoresReg.append(a)
    def prestarLibro(self, p: Prestamo):
        for i in self.__librosDisp:
            if p.getLibro() == i:
                self.__librosDisp.remove(i)
                self.__prestamosActivos.append(p)
                i.cambiarEstado(False)
    def mostrarEstado(self):
        print (f"NOMBRE: {self.__nombre}, HORARIO DE ATENCION: {self.__horarioDeAtencion}, LIBROS DISPONIBLES {self.__librosDisp}, AUTORES REGISTRADOS {self.__autoresReg}, PRESTAMOS ACTIVOS {self.__prestamosActivos}")
    def cerrarBiblioteca(self):
        print("Biblioteca cerrada")
        for i in self.__prestamosActivos:
            self.__prestamosActivos.remove(i)
            self.__librosDisp.append(i.getLibro())
            i.getLibro().cambiarEstado(True)

class Libro:
    def __init__(self, titulo, ISBN):
        self.__titulo = titulo
        self.__isbn = ISBN
        self.__paginas = []
        self.__disponible = True
    class Pagina:
        def __init__(self, nroDePagina, contenidoDePagina):
            self.__nroDePagina = nroDePagina
            self.__contenidoDePagina = contenidoDePagina
        def __repr__(self):
            return f"numero de pagina: {self.__nroDePagina}, contenido de pagina: {self.__contenidoDePagina}"
    def agregarPagina(self, nroDePag, contenidoPag):
        p = self.Pagina(nroDePag, contenidoPag)
        self.__paginas.append(p)
    def leer(self):
        print(self.__paginas)
    def __repr__(self):
        return f"titulo: {self.__titulo}, ISBN: {self.__isbn}, PAGINAS: {self.__paginas}, disponible = {self.__disponible}"
    def getTitulo(self):
        return self.__titulo
    def cambiarEstado(self, x): 
        self.__disponible = x
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.__nombre = nombre 
        self.__nacionalidad = nacionalidad
    def __repr__(self):
        return f"nombre: {self.__nombre}, nacionalidad: {self.__nacionalidad}"
class Estudiante:
    def __init__(self, codigo, nombre):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__prestamoActivo = False
    def mostrarInfo(self):
        print (f"nombre: {self.__nombre}, codigo: {self.__codigo}")
    def cambiarEstado(self, x):
        self.__prestamoActivo = x
    def __str__(self):
        return f"nombre: {self.__nombre}, codigo: {self.__codigo}, prestamo activo = {self.__prestamoActivo}"
class Prestamo:
    def __init__(self, fechaDePrestamo, fechaDeDevolucion, e: Estudiante, l: Libro):
        self.__fechaDePrestamo = fechaDePrestamo
        self.__fechaDeDevolucion = fechaDeDevolucion
        self.__estudiante = e
        e.cambiarEstado(True)
        self.__libro = l
        l.cambiarEstado(False)
    def getLibro(self):
        return self.__libro
    def mostrarInfo(self):
        print (f"fecha de prestamo: {self.__fechaDePrestamo}, fecha de devolucion: {self.__fechaDeDevolucion}, ESTUDIANTE: {self.__estudiante}, LIBRO: {self.__libro.getTitulo()}")
    def __repr__(self):
        return f"fecha de prestamo: {self.__fechaDePrestamo}, fecha de devolucion: {self.__fechaDeDevolucion}, ESTUDIANTE: {self.__estudiante}, LIBRO: {self.__libro.getTitulo()}"

class Main:
    b1 = Biblioteca("Biblioteca de Informatica")
    b1.setHorario("Lunes-Viernes", "10:00", "20:00")
    l1 = Libro("el Principito", 148105)
    l1.agregarPagina(1, "aaaaaaaaa")
    l1.agregarPagina(2, "bbbbbbbbbbbbbb")
    l1.agregarPagina(3, "cccccccccccccc")
    b1.agregarLibro(l1)
    a1 = Autor("Friodor Dostov", "Ruso")
    b1.agregarAutor(a1)
    b1.mostrarEstado()
    e1 = Estudiante(1524, "Brandon")
    p1 = Prestamo("9/05/26", "11/05/26", e1, l1)
    b1.prestarLibro(p1)
    b1.mostrarEstado()
    b1.cerrarBiblioteca()
    b1.mostrarEstado()