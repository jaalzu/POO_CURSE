# class Estudiante():
#     def __init__(self,nombre,edad,grado):
#         self.nombre = nombre
#         self.edad = edad
#         self.grado = grado
#     def estudiar(self):
#         print("Estudiando...")

# nombre = input("Digame su nombre: ")
# edad = input("Que edad tienes: ")
# grado = input("Cual es tu grado: ")        
# estudiante1 = Estudiante(nombre,edad,grado)
# print(f"El estudiante se llama : {estudiante1.nombre}\nTiene : {estudiante1.edad}\ny va al grado: {estudiante1.grado}\n")

# while True:
#     estudiar = input()
#     if (estudiar.lower() == "estudiar"):
#         estudiante1.estudiar()
#         break





# class Coche:
#     def __init__(self,marca,modelo,año):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año
#     def arrancar(self):
#         print("el coche arranco")
#     def acelerar(self):
#         print("el coche esta acelerando")
#     def frenar(self):
#         print("el coche esta frenando")
#     def cambiar_marca(self,nueva_marca):
#         self.marca = nueva_marca
#         print("La marca del coche ha sido cambiada a",nueva_marca)
# audi = Coche("Audi","A4",2020)

# print(f"mi auto {audi.marca} es un {audi.modelo} del año {audi.año}")
# audi.cambiar_marca("BMW")
# print(f"mi auto {audi.marca} es un {audi.modelo} del año {audi.año}")


# flota = [Coche("Audi","A4",2020),Coche("BMW","Serie 3",2021),Coche("Porsche","911",2022)]

# for coche in flota:
#     print("Marca:",coche.marca)
#     print("Modelo:",coche.modelo)
#     print("Año: ",coche.año)
#     coche.arrancar()
#     coche.acelerar()
#     coche.frenar()
#     coche.cambiar_marca("Volkswagen")
#     print("---------------")
  









# class Rectangulo:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.width + self.height)

# rect = Rectangulo(5,19)

# print("Area del rectangulo",rect.area())
# print("Perimetro del rectangulo",rect.perimeter())





# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
#     def display_employee(self):
#         print("Name:",self.name, ",Salary:",self.salary)
    
#     def calculate_bonus(self,bonus_percentage):
#         bonus = (self.salary * bonus_percentage) / 100
#         print(f"{self.name} get a bonus of ${bonus}")

# emp1 = Employee("Pepe",35000)
# emp2 = Employee("Juan",15000)

# emp1.display_employee()
# emp2.display_employee()

# emp1.calculate_bonus(10)
# emp2.calculate_bonus(5)








# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_numbre = account_number
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Deposio {amount}. Nuevo balance: {self.balance}")

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Retiro {amount}. Nuevo Balance: {self.balance}")
#         else:
#             print("Fondos insufi")

# account1 = BankAccount("1234",5000)
# print(account1.balance)
# account1.deposit(100)
# account1.withdraw(5300)








# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.grades = []

#     def add_grade(self,grade):
#         self.grades.append(grade)
#     def get_average_grade(self):
#         if self.grades:
#             return sum(self.grades) / len(self.grades)
#         else:
#             return 0
# student1 = Student("Alice",20)

# student1.add_grade(56)
# student1.add_grade(96)
# student1.add_grade(66)

# average_grade = student1.get_average_grade()
# print(f"{student1.name} have a average grade: {average_grade}")










# class Persona:
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad
    
#     def mostrar_datos(self):
#         print(f"Nombre: ",self.nombre,"\nEdad: ",self.edad)

# class Estudiante(Persona):
#     def __init__(self, nombre, edad,grado):
#         super().__init__(nombre, edad)
#         self.grado = grado
    
#     def mostrar_grado(self):
#         print(f"Grado: {self.grado}")

# estudiante1 = Estudiante("Pepe","23","10mo")
# estudiante1.mostrar_datos()
# estudiante1.mostrar_grado()



class Animal:
    def comer(self):
        print("El animal ta comiendo")
class Ave(Animal):
    def volar(self):
        print("El Animal ta volando ")
class Mamifero(Animal):
    def matar(self):
        print("El animal esta matando")

class Murcielago(Mamifero,Ave):
    pass
ave = Ave()

ave.comer()
ave.volar()
print(Murcielago.mro())


