# class MiClase:
#     def __init__(self):
#         self.__atributo_privado = "Valor"

#     def __hablar(self):
#         print("Hi")

# objeto = MiClase()
# print(objeto.__hablar())



class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self,edad):
        if edad > 0:
            self.__edad = edad
    def get_edad(self):
        return self.__edad

    def __metodo_privado(self):
        print("ESte es un metodo privado")

persona = Persona("JUa",30)
print(persona.get_nombre())

persona.set_edad(10)
print(persona.get_edad())
