
# En el contexto de la programación orientada a objetos (POO), un decorador es un patrón de diseño que permite agregar funcionalidades adicionales a un objeto existente dinámicamente. Este patrón es muy útil cuando se necesita extender el comportamiento de un objeto sin modificar su código.

# En términos generales, un decorador consiste en crear una clase que envuelve a otra clase (o a un objeto de esa clase) y proporciona funcionalidades adicionales sin alterar la interfaz original de la clase envuelta.

# Algunos puntos clave sobre los decoradores en POO:

# Extensibilidad: Los decoradores permiten extender la funcionalidad de un objeto sin modificar su código.

# Composición: Se utiliza la composición para agregar funcionalidades adicionales al objeto envuelto.

# Transparencia: Desde el punto de vista del cliente que utiliza el objeto, el decorador y el objeto original se comportan de la misma manera, ya que siguen la misma interfaz.

# Un ejemplo común de decorador es la funcionalidad de "logging" (registro de eventos) que se agrega a un objeto existente. En lugar de modificar la clase original para agregar el registro de eventos, se puede crear un decorador de registro que envuelva al objeto original y registre las acciones realizadas en él.

# En resumen, los decoradores son una herramienta poderosa para extender la funcionalidad de los objetos en tiempo de ejecución, lo que promueve un diseño flexible y modular en la programación orientada a objetos.






# def funcion_decorador(funcion): # Funcion B
#     def funcion_interna(): # Funcion A recibe como parametro a B para retornar C
#         print("Hola")
#     return funcion_interna() # Funcion C 

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args,**kwargs):
        #Acciones adicionales que decoran

        print("Vamos a realizar una operacion: ")

        funcion_parametro(*args,**kwargs)

        #Acciones adicionales que decoran

        print("Hemos terminado la operacion")
    return funcion_interior

@funcion_decoradora
def suma(num1,num2):

    print(num1+num2)

@funcion_decoradora

def resta(num1,num2,num3):

    print(num1-num2-num3)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base,exponente))

suma(7,5)

resta(10,12,2)
potencia(5,3)



















# def decorador(funcion):
#     def funcion_modificada():
#         print("Antse de llamar la funciom")
#         funcion()
#         print("Despues de llaamr a la funcion")
#     return funcion_modificada

# # def saludo():
# #     print("Hola Dalto")

# # saludo_modificado = decorador(saludo)
# # saludo_modificado()

# @decorador
# def saludo():
#     print("Hola dalto comn dnas")

# saludo()



# def abrir_base(datos):
#     def ejecutando_base():
#         print("Ejecutando el codigo a la base de datos")

#         datos()

#         print("Cerrando la base de datos")

#     return ejecutando_base()

# @abrir_base
# def abe():
#     print("LA BASE")

# abe()






import time







