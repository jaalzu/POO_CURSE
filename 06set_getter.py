# class Persona:
#     def __init__(self,nombre,edad):
#         self._nombre = nombre
#         self._edad = edad
    
#     def get_nombre(self):
#         return self._nombre
#     def get_edad(self):
#         return self._edad
    
#     def set_nombre(self,new_name):
#         self._nombre = new_name

# dalto = Persona("pepe",21)

# nombre = dalto.get_nombre()
# dalto.set_nombre("PEp")
# nombre = dalto.get_nombre()

# print(nombre)









class Producto:
    def __init__(self,costo):
        self._costo=costo

        self._precioventa=self._calculaPVenta()
    
    def _calculaPVenta(self):
        return self._costo*1.30
    

    def getPrecioVenta(self):
        return self._precioventa
    

    def setCosto(self,valor):

        if valor>0:
            self._costo=valor
            self._precioventa=self._calculaPVenta()
        else:
            print('valor invalido')
            self._costo=0
    
    def getCosto(self):
        return self._costo
    
    def __repr__(self):
        return f'costo=${self._costo},Precio Venta =${self._precioventa}'
    
manzana = Producto(12.5)
print(manzana)

pv= manzana.getPrecioVenta()
print('el impuesto es $',pv*0.16)

manzana.setCosto(11.10)

print(manzana.getCosto())

print(manzana)





# label.py

class Label:
    def __init__(self, text, font):
        self._text = text
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value

label = Label("Fruits", "JetBrains Mono NL")
label.get_text()
'Fruits'

label.set_text("Vegetables")

label.get_text()
'Vegetables'

label.get_font()
'JetBrains Mono NL'





