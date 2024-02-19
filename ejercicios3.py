# class Personaje():
#     def __init__(self,nombre,fuerza,velocidad):
#         self.nombre=nombre
#         self.fuerza=fuerza
#         self.velocidad=velocidad
#     def __repr__(self):
#         return f'{self.nombre} (Fuerza:{self.fuerza},Velocidad:{self.velocidad})'
    
#     def __add__(self,otro_pj):
#         nuevo_nombre = self.nombre + "-" + otro_pj.nombre
#         nueva_fuerza = ((self.fuerza+otro_pj.fuerza)/2)**1.5
#         nueva_velocidad = ((self.velocidad+otro_pj.velocidad)/2)**1.5
#         return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
    
# goku = Personaje("Goku",100,100)
# vegeta = Personaje("Vegeta",99,99)
# jiren = Personaje("Jiren",130,140)

# gogeta = goku + vegeta
# jireta = gogeta + jiren

# print(jireta)
# print(gogeta)
# print(goku)
# print(vegeta)






# Ejercicio 9: Cafetera robot
# Cómo diseñaríamos el comportamiento de una cafetera robot?
# desarrolla una clase Cafetera con atributos
# capacidadMaxima (la cantidad máxima de café que puede contener la
# cafetera)
# _cantidadActual (la cantidad actual de café que hay en la cafetera).
# Luego desarrollar los siguientes métodos:
# llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la
# capacidad.
# servirTaza(int): simula la acción de servir una taza con la capacidad indicada.
# Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que
# quede.
# vaciarCafetera(): pone la cantidad de café actual en cero.
# agregarCafe(int): añade a la cafetera la cantidad de café indicada.



# class Cafetera():
#         def __init__(self,capacidadMaxima=100,cantidadActual=0):
#                 self.capacidadMaxima= capacidadMaxima
#                 self.cantidadActual=cantidadActual
            
#         def llenarCafetera(self):
#                 if self.cantidadActual > self.capacidadMaxima:
#                         self.cantidadActual = self.capacidadMaxima
#                         print("Llenando la taza..")
#                 else:
#                         print("ya esta lleno!")
        
#         def servirTaza(self):
#                 valor = input("Cuanto desea agregar?:")
#                 self.cantidadActual += valor
#                 print(f"La taza tiene {self.cantidadActual}")
    
# cafe = Cafetera(100,10)

# cafe.servirTaza()
# # cafe.llenarCafetera()
















# Ejercicio 4
# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

# class Calculadora():
#     def __init__(self):
#         self.num1=int(input("ingrese el valor: "))
#         self.num2=int(input("Ingrese el valor: "))

#     def suma(self):
#         valor = self.num1 + self.num2
#         print(f"El resultado de la suma de {self.num1} + {self.num2} es igual a",valor)
    
#     def resta(self):
#         valor = self.num1 - self.num2
#         print(f"el resultado de la resta entre {self.num1} - {self.num2} es igual a {valor}")
    
#     def divisor(self):
#         valor = self.num1 // self.num2
#         print(f"la division entre {self.num1} / {self.num2} es igual a {valor}")
    
#     def multiplicacion(self):
#         valor = self.num1 * self.num2
#         print(f"la multiplicacion entre {self.num1} * {self.num2} es igual a {valor}")
    

    
# calc = Calculadora()

# # calc.suma()
# # calc.resta()
# calc.divisor()
# calc.multiplicacion()





# def comprobarContrasenia(password):
#     largo = False
#     numer = False
#     mayus = False
#     if len(password) > 8:
#         largo = True
#     for i in range(len(password)):
#        if password[i].isupper():
#           mayus = True
#        if password[i].isnumeric():
#            numer = True

#     if largo and numer and mayus:
#         return True
#     else:
#         return False

# password=input("Ingrese una clave: ")

# verificacion = comprobarContrasenia(password)
# if verificacion:
#     print("La clave es segura")
# else:
#     print("No es segura")









# class Agenda():
#    #iniciamos nuestra clase
#    def __init__(self):
#       # creamos una lista dodne guardamos los contactos
#       self.contactos = []
    
#    def menu(self):
#         menu=[
#             ['Agenda Personal'],
#             ['1.Añadir contacto',"añadir"],
#             ['2.Lista De Contactos'],
#             ['3.Buscar contacto'],
#             ['4.Editar contacto'],
#             ['5.Cerrar Agenda']
#         ]

#         for x in range(6):
#             print(menu[x][0])
        
#         opcion=int(input("Introduzca la opcion deseada: "))
#         if opcion==1:
#             self.añadir()
#         elif opcion==2:
#             self.lista()
#         elif opcion==3:
#             self.buscar()
#         elif opcion==4:
#             self.editar()
#         elif opcion==5:
#             print("Cerrando agenda")
#             exit()
        
#         self.menu()
    
#    def añadir(self):
#        print("Añadir nuevo contacto")
#        nombre = input("Introduzca el nombre: ")
#        telefono = int(input("Introduzca el telefono: "))
#        email = input("Introduzca el email: ")
#        self.contactos.append(f"nombre:{nombre}\nTelefono:{telefono}\nemail:{email}")
    
#    def lista(self):
#        print("--------")
#        print("Lista de contactos")
#        if len(self.contactos) == 0:
#             print("No hay contactos")
#        else:
#            for x in range(len(self.contactos)):
#             print(self.contactos[x])

# agenda1 = Agenda()
# agenda1.menu()





















# class Cuenta():
#     def __init__(self,titular,cantidad):
#         self.titular=titular
#         self.cantidad=cantidad
    
#     def imprimir(self):
#         print("El titular -",self.titular,"-")
#         print("Con una cantidad de $",self.cantidad)

# class CajaAhorro(Cuenta):
#     def __init__(self, titular, cantidad):
#         super().__init__(titular, cantidad)
    
#     def imprimir(self):
#         print("Cuenta de caja de ahorros")
#         return super().imprimir()

# class PlazoFijo(Cuenta):
#     def __init__(self, titular, cantidad,plazo,interes):
#         super().__init__(titular, cantidad)
#         self.plazo = plazo
#         self.interes=interes

#     def ganancia(self):
#         total = self.cantidad*self.interes/100
#         print("El importe del interes es",total)

#     def imprimir(self):
#         print("Cuenta a plazo fijo")
#         super().imprimir()
#         print("Plazo disponible en dias:",self.plazo)
#         print("Interes:",self.interes)
#         self.ganancia()
        

# caja1=CajaAhorro("Mamerto",5000)
# caja1.imprimir()

# caja2=PlazoFijo("Pepe",5000,365,1.1)
# caja2.imprimir()

# caja3 = Cuenta("pepe",13131)
# caja3.imprimir()



class Bebidas():
    def __init__(self,identificador,litros,precio,marca):
        self.identificador = identificador
        self.litros = litros
        self.precio = precio
        self.marca = marca


    def calcular_precio(self):
        return self.precio
            

class Agua(Bebidas):
    def __init__(self,identificador, litros, precio, marca,origen):
        super().__init__(identificador,litros, precio, marca)
        self.origen = origen

class Gaseosa(Bebidas):
    def __init__(self,identificador, litros, precio, marca,azucar,promocion):
        super().__init__(identificador,litros, precio, marca)
        self.azucar = azucar
        self.promocion = promocion


    def calcular_precio(self):
        if self.promocion:
            return self.precio * 0.9
        else:
            return self.precio



class DepositoBebidas:
    def __init__(self):
        self.bebidas = []

    def agregar_producto(self,bebida):
        for x in self.bebidas:
            if x.identificador == bebida.identificador:
                print("La bebida ya esta en el deposito")
            else:
                self.bebidas.append(bebida)
                print("Producto agregado con exito")
    

    def calcular_precio_total(self):
        precio_total= sum(bebida.calcular_precio() for bebida in self.bebidas)
        print(f"El precio total de las bebidas:{precio_total}")

deposito = DepositoBebidas()

agua_mineral = Agua('001',1.5,2.5,"Nestle","manantial")
gaseosa = Gaseosa("002",2,3,"Coca",10,promocion=True)

deposito.agregar_producto(agua_mineral)
deposito.agregar_producto(gaseosa)

deposito.calcular_precio_total()