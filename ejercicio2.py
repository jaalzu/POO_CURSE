# class Personaje:
#     nombre = "Default"
#     fuerza = 0
#     inteligencia = 0
#     defensa = 0
#     vida = 0

#     def __init__(self,nombre,fuerza,inteligencia,defensa,vida):
#         self.nombre = nombre
#         self.fuerza = fuerza
#         self.inteligencia = inteligencia
#         self.defensa = defensa
#         self.vida = vida
    
#     def atributos(self):
#         print(self.nombre,":",sep="")
#         print("-Fuerza:",self.fuerza)
#         print("-Inteligencia:",self.inteligencia)
#         print("-Defensa:",self.defensa)
#         print("-Vida:",self.vida)

#     def subir_nivel(self,fuerza,inteligencia,defensa):
#         self.fuerza = self.fuerza + fuerza
#         self.inteligencia = self.inteligencia + inteligencia
#         self.defensa = self.defensa + defensa

#     def esta_vivo(self):
#         return self.vida > 0
    
#     def morir(self):
#         self.vida = 0 
#         print(self.nombre,"ha muerto")

#     def daño(self,enemigo):
#         return self.fuerza - enemigo.defensa
    
#     def atacar(self,enemigo):
#         daño = self.daño(enemigo)
#         enemigo.vida = enemigo.vida - daño
#         print(self.nombre,"ha realizado",daño,"puntos de daño a",enemigo.nombre)
#         if enemigo.esta_vivo():
#             print("La vida de",enemigo.nombre,"es",enemigo.vida)
#         else:
#             enemigo.morir()

# class Guerrero(Personaje):
#     def __init__(self, nombre, fuerza, inteligencia, defensa,vida,espada):
#         super().__init__(nombre, fuerza, inteligencia, defensa, vida)
#         self.espada = espada

#     def cambiar_arma(self):
#         opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8.(2) Matadragones , daño 10"))
#         if opcion == 1:
#             self.espada = 8
#         elif opcion == 2:
#             self.espada = 10
#         else:
#             print("Numero de arma incorrecto")


#     def atributos(self):
#             super().atributos()
#             print("-Espada:",self.espada)

#     def daño(self,enemigo):
#         return self.fuerza*self.espada - enemigo.defensa


# class Mago(Personaje):

#     def __init__(self, nombre, fuerza, inteligencia, defensa, vida,libro):
#         super().__init__(nombre, fuerza, inteligencia, defensa, vida)
#         self.libro = libro

#     def atributos(self):
#         super().atributos()
#         print("-Libro",self.libro)

#     def daño(self,enemigo):
#         return self.inteligencia*self.libro - enemigo.defensa


# personaje_1 = Personaje("Guts",20,10,4,100)
# personaje_2 = Mago("Vanessa",5,15,4,100,3)

# def combate(player1,player2):
#     turno = 0
#     while player1.esta_vivo() and player2.esta_vivo(): 
#         print("\nTurno",turno)
#         print(">>> Accion de",player1.nombre,":",sep="")  
#         player1.atacar(player2)
#         print(">>> Accion de",player2.nombre,":",sep="")  
#         player2.atacar(player1)
#         turno = turno + 1
#     if player1.esta_vivo():
#             print("\n ha ganado",player1.nombre)
#     elif player2.esta_vivo():
#             print("\n ha ganado",player2.nombre)
#     else:
#             print("\n Empate")

# combate(personaje_1,personaje_2)


# mi_personaje = Personaje("Kratos",20,15,10,250)
# guts = Guerrero("Guts",20,15,10,100,5)
# mago = Mago("Vanes",20,15,10,100,5)









# # class Cafe():
# #     def que_soy(self):
# #         print("soy cafe")
# # class te():
# #     def que_soy(self):
# #         print("Soy un te")

# # def definicion_bebida(bebida):
# #     bebida.que_soy()


#     # def get_fuerza(self):
#     #     return self.fuerza
    
#     # def set_fuerza(self,fuerza):
#     #     if fuerza < 0:
#     #         print("Error")
#     #     else:
#     #         self.fuerza = fuerza





# # /////////////////////////////////////////



# class Calculadora():
#      def __init__(self,num1,num2):
#           self._num1 = num1
#           self._num2 = num2

#      def suma(self):
#       resultado = self._num1 + self._num2 
#       print(f"el resultado de la suma es: {self._num1} + {self._num2} = {resultado}")

#      def resta(self):
#           resultado = self._num1 - self._num2 
#           print(f"el restulado de la resta es: {self._num1} - {self._num2} = {resultado}")

#      def division(self):
#           resultado = self._num1 // self._num2
#           print(f"el resultado de la division {self._num1} // {self._num2} = {resultado}")

#      def multiplicacion(self):
#           resultado = self._num1 * self._num2
#           print(f"el resultado de la multiplicaicon {self._num1} * {self._num2} = {resultado}")

# operacion = Calculadora(10,5)
# operacion.suma()

# operacion = Calculadora(20,5)
# operacion.resta()

# opera = Calculadora(10,5)
# opera.division()

# opera = Calculadora(10,5)
# opera.multiplicacion()







# # /////////////////////////////////////////


# class Persona():
#     def __init__(self,nombre,apellido):
#         self.nombre = nombre
#         self.apellido = apellido
    
#     def mostrar_nombre(self):
#         print(f"{self.nombre} {self.apellido}")

# class Estudiante(Persona):
#     def __init__(self, nombre, apellido,carrera):
#         super().__init__(nombre, apellido)
#         self.carrera = carrera
    
#     def mostrar_carrera(self):
#         print(f"La carrera que esta cursando es{self.carrera}")

# pepe = Persona("Pepe","Pepon")
# pepe.mostrar_nombre()
# pepe = Estudiante("Pepe","Apon","Ingeniero")
# pepe.mostrar_carrera()






# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
# Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

# class Fabrica:
#     def __init__(self,llantas,color,precio):
#         self.llantas = llantas
#         self.color = color
#         self.precio = precio

# class Moto(Fabrica):
#     def __init__(self, llantas, color, precio):
#         super().__init__(llantas, color, precio)
#         self.llantas = 2

#     def mostrar(self):
#         print(f"La moto cuenta con {self.llantas} llantas, de un color {self.color} y con un valor de ${self.precio}")

# class Carro(Fabrica):
#     def __init__(self, llantas, color, precio):
#         super().__init__(llantas, color, precio)
#         self.llantas = 4
#     def mostrar(self):
#         print(f"el auto cuenta con {self.llantas} llantas , tiene un color {self.color} y su precio es de ${self.precio}")

# moto = Moto("","Rojo","4000")
# moto.mostrar()

# auto = Carro("","Verde","6000")
# auto.mostrar()




# Ejercicio 6
# Crear una clase llamada Marino(), con un método que sea hablar, en donde muestre un mensaje que diga «Hola, soy un animal marino!». Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por «Hola soy un Pulpo!».
# Por último, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parámetro.



# class Marino:
#     def hablar(self):
#         print("Hola soy un animal marino!")

# class Pulpo(Marino):
#   def hablar(self):
#     print("«Hola soy un pulpo!»")

# class Foca():
#    def hablar(self,mensaje):
#       self.mensaje = mensaje
#       print(mensaje)

# marino=Marino()
# marino.hablar()

# pulpo=Pulpo()
# pulpo.hablar()

# foca=Foca()
# foca.hablar("PEPEPEPE")












# class Libro:
#     def __init__(self,titulo,autor,disponible):
#       self.titulo = titulo
#       self.autor = autor
#       self.disponible = True

#     def prestar(self):
#       if self.disponible:
#          self.disponible = False
#          print(f"el libro {self.titulo} ha sido prestado")
#       else:
#          print(f"el libro {self.titulo} no esta disponible")
#     def devolver(self):
#        if self.disponible:
#           self.disponible = True
#           print(f"El libro {self.titulo} ha sido devuelto")
#        else:
#           print(f"el libro {self.titulo} ya esta disponible")


# class Bibloteca:
#     def __init__(self):
#       self.libros = []

#     def agregar_libro(self,libro):
#          self.libros.append(libro)
#          print(f"El libro '{libro.titulo}' ha sido agregado a la bibloteca")


#     def mostrar_libros_disponibles(self):
#          print("Libros disponibles en la bibloteca:")
#          for libro in self.libros:
#             if libro.disponible:
#                print(f"-{libro.titulo} por {libro.autor}")



# libro1 = Libro("Adventures of Pepe","J,R,R.PEPE",True)
# libro2 = Libro("Adventurasdasdes of Pepe","J,R,R.PEPE",True)
# bibloteca = Bibloteca()
# bibloteca.agregar_libro(libro1)
# bibloteca.agregar_libro(libro2)
# bibloteca.mostrar_libros_disponibles()

# libro1.prestar()
# bibloteca.mostrar_libros_disponibles()














class Producto():
    def __init__(self,codigo,nombre,precio,stock):
        self.codigo =codigo
        self.nombre=nombre
        self.precio=precio
        self.stock = stock
    def mostrar_info(self):
        print(f"Codigo:{self.codigo}\nNombre:{self.nombre}\nPrecio:{self.precio}")
    def actualizar_precio(self,nuevo_precio):
        self.precio = nuevo_precio
        print("El precio del producto",self.nombre, "se actualizo a ",
              self.precio)
    def agregar_stock(self,cantidad):
        self.stock = cantidad
        print(f"Se agregaron {cantidad} unidades al stock del producto {self.nombre}")

    def vender_productos(self,cantidad):
        if self.stock >=cantidad:
            self.stock -=cantidad
            print(f"Se vendieron {cantidad} de unidades del producto {self.nombre}")
        else:
            print(f"No hay suficiente stock del producto {self.nombre}")
class Inventario:
    def __init__(self):
        self.productos = {}
    
    def agregar_productos(self,producto):
        self.productos[producto.codigo] = producto
        print(f"Producto '{producto.nombre} agregado al inventario")

    def mostrar_inventario(self):
        print("Inventario de la tienda:")
        for producto in self.productos.values():
            producto.mostrar_info()

inventario_tienda = Inventario()

producto1 = Producto("001","Remera",20.0,50)
producto2 = Producto("002","Pantalon",30,50)

inventario_tienda.agregar_productos(producto1)
inventario_tienda.agregar_productos(producto2)

inventario_tienda.mostrar_inventario()

producto1.actualizar_precio(25.0)
producto2.agregar_stock(20)

inventario_tienda.mostrar_inventario()