# class Persona:
#     def __init__(self,nombre,edad):
#         self.__nombre = nombre
#         self._edad = edad
#     @property
#     def nombre(self):
#         return self.__nombre
#     @nombre.setter
#     def nombre(self,new_nombre):
#         self.__nombre = new_nombre

#     @nombre.deleter
#     def nombre(self):
#         del self.__nombre

# dalto = Persona("pespe",21)

# nombre = dalto.nombre
# print(nombre)





import time
def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()-t1
        print(f'{func.__name__} ran in {t2} seconds')
    return wrapper

@tictoc
def do_this():
    ##
    time.sleep(1.3)
@tictoc
def do_that():
    #
    time.sleep(.4)

do_this()
do_that()
print('Done')