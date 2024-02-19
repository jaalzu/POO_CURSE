# Una clase en Python es una estructura de programación que permite definir un conjunto de métodos y atributos que describen un objeto o entidad. Las clases son un concepto fundamental en la programación orientada a objetos, que se utilizan para modelar entidades del mundo real o abstracto en un programa de computadora.




















# La instancia de una clase es un objeto específico creado a partir de la definición de esa clase. Cuando creas una clase en Python, estás esencialmente creando un "molde" o un "plano" para crear objetos. Una vez que tienes esa definición de clase, puedes crear múltiples objetos, que son instancias de esa clase.

# Por ejemplo, considera la siguiente definición de clase en Python:


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
# En este caso, la clase Persona define propiedades como nombre y edad, así como un método llamado saludar().

# Para crear una instancia u objeto de esta clase, simplemente usas el nombre de la clase seguido de paréntesis:


persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)
# Ahora, persona1 y persona2 son instancias u objetos de la clase Persona. Cada una de estas instancias tiene su propio estado (los valores de nombre y edad), y también pueden tener comportamientos (métodos) asociados, como el método saludar() en este caso.

# Puedes acceder a los atributos y métodos de una instancia utilizando la notación de punto:


# print(persona1.nombre)  # Juan
# print(persona2.edad)    # 25

# persona1.saludar()      # Imprime: Hola, mi nombre es Juan y tengo 30 años.
# persona2.saludar()      # Imprime: Hola, mi nombre es María y tengo 25 años.
# En resumen, una instancia de una clase es un objeto concreto creado a partir de la plantilla proporcionada por la clase, que tiene sus propios atributos y métodos.








class Persona:
    def __init__(self,nombre,edad=int):
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        print(f"{self.nombre} tiene {self.edad}")

pepe = Persona("pepe",13)
print(str(pepe))



# class Celular(): 
#     def __init__(self,marca,modelo,camara):
#         self.marca = marca
#         self.modelo = modelo
#         self.camara = camara
        
#     def llamar(self):
# print(f"Estas llamadondo desde un: {self.modelo}")
#     def cortar(self):
#         print(f"Cortaste la llamada desde tu : {self.modelo}")
#  # instanciar una clase es crear un objeto


# celular1 = Celular("samsung","s23","200mp")
# celular2 = Celular("apple","Iphone 15","100mp")

# print(celular1.llamar())
# print(celular1.cortar())