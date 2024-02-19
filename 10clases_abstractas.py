from abc import ABC,abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    @abstractclassmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        print(f"Hola , me llamo: {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"estoy estudiande:{self.actividad}")

class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
    
    def hacer_actividad(self):
        print(f"Estoy trabajando en:{self.actividad}")


dalto = Estudiante("lukas",21,"MAsc","Programacion")
pedro = Trabajador("Pedro",25,"Wom","Albañil")
dalto.presentarse()
dalto.hacer_actividad()
pedro.presentarse()
pedro.hacer_actividad()



class Figura(ABC):

    

    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado
    
    def area(self):
        return self.lado*self.lado
    
    def perimetro(self):
        return self.lado*4
    

class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio
    
    def area(self):
        return 3.14159*self.radio*self.radio
    def perimetro(self):
        return 2*3.14169*self.radio
    
# f1=Figura()
    
c1=Cuadrado(5)

print('el area es',c1.area())
print('el perimetro es',c1.perimetro())

c2=Circulo(5)
print('el radio es',c2.area())
print('el perimetro es',c2.perimetro())