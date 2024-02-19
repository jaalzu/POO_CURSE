# class Persona:
#     def __init__(self,nombre,edad,nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionalidad = nacionalidad
#     def hablar(self):
#         print("Hi , im talking a little")    


# class Empleado(Persona):
#    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
#        super().__init__(nombre,edad,nacionalidad)
#        self.trabajo = trabajo
#        self.salario = salario

# class Estudiante(Persona):
#       def __init__(self,nombre,edad,nacionalidad,notas,universidad):
#        super().__init__(nombre,edad,nacionalidad)
#        self.notas = notas
#        self.universidad = universidad


# roberto = Empleado("Roberto",53,"Argentino","Programador",10000)
# roberto.hablar()








# class Persona:
#     def __init__(self,nombre,edad,nacionalidad):
#         self.nombre = nombre
#         self.edad = edad
#         self.nacionalidad = nacionalidad
#     def hablar(self):
#         print("Hi , im talking a little")    

# class Artista:
#     def __init__(self,habilidad):
#         self.habilidad = habilidad
    
#     def mostrar_habilidad(self):
#         print(f"Mi habilidad es : {self.habilidad}")

# class Empleado(Persona):
#    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
#        super().__init__(nombre,edad,nacionalidad)
#        self.trabajo = trabajo
#        self.salario = salario

# class EmpleadoArtista(Persona,Artista):
#     def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
#         Persona.__init__(nombre, edad, nacionalidad)
#         Artista.__init__(self,habilidad)
#         self.salario = salario
#         self.empresa = empresa

#     def presentarse(self):
#         print(f'{self.mostrar_habilidad()}')

# roberto = EmpleadoArtista("Roberto",43,"argentino","Cantar","programador",1000)
# roberto.presentarse()










# class Vehiculos():
#     def __init__(self,marca,modelo):
#         self.marca=marca
#         self.modelo=modelo
#         self.enmarcha=False
#         self.acelera=False
#         self.frena=False
#     def arrancar(self):
#         self.enmarcha=True
#     def acelerar(self):
#         self.acelera=True
#     def frenar(self):
#         self.frena=True
#     def estado(self):
#         print("Marca:",self.marca, "\nModelo:",self.modelo, "\nEn marcha",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:" , self.frena)



# class Furgoneta(Vehiculos):
#     def carga(self,carga):
#         self.cargado = carga
#         if(self.cargado):
#             return "La furgoneta esta cargada"
#         else:
#             return "La furgoneta no esta cargada"

# class Moto(Vehiculos):
#     hcaballito =""
#     def caballito(self):
#         self.hcaballito = "Voy haciendo el caballito"

#     def estado(self):
#         print("Marca:",self.marca, "\nModelo:",self.modelo, "\nEn marcha",self.enmarcha,"\nAcelerando:",self.acelera,"\nFrenando:" , self.frena,"\n",self.hcaballito)

# class VElectricos():
#     def __init__(self):
#         self.autonomia = 100

#     def cargarEnergia(self):
#         self.cargando = True

# class BiciElectrica(VElectricos,Vehiculos):
#     pass


# miBici=BiciElectrica()



# miFurgoneta = Furgoneta("Mercedes","Sprinter")
# miFurgoneta.estado()
# print(miFurgoneta.carga(True))


# # miMoto = Moto("Honda","CBR")
# # miMoto.caballito()
# # miMoto.estado()










class Persona:
    def __init__(self,nombre,edad,lugar):
        self.nombre = nombre
        self.edad = edad
        self.lugar = lugar
    def descripcion(self):
        print("Nombre:",self.nombre,"\nEdad: ",self.edad , "\nLugar: " , self.lugar)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("salario:",self.salario,"Antiguedad:",self.antiguedad)

pepe = Empleado(1500,15,"pepe",55,"colombia")
pepe.descripcion()