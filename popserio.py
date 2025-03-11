
#siempre se debe crear una clase asi
class Producto:
    def __init__(self,codigo,nombre,precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio 
# se crea el property por que tiene dos barra baja lo que indica que es privado
    @property
    def codigo(self):
        return self.__codigo
    # siempre despues de que se llama al valor privado se coloca @codigo.stter van de la mano 
    @codigo.setter
    def codigo(self,valor):
        self.__codigo = valor
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor
        
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,valor):
        self.__precio = valor
# crear una funcion para calcular el total de las unidades que le demos en el print
    def calcular_total(self, unidades):
        return self.precio * unidades
    
#con el str en la clase se concatenan los atributos de la clase
    def __str__(self):
        return f"codigo: {self.__codigo},  nombre:  {self.__nombre}, precio: {self.__precio}"

p1 = Producto(23,"producto",3304)
p2 = Producto(23,"producto",3307)

print(p1,p1.calcular_total(5))
print(p2)


#EJERCICIO #2 POO---------------------------------------------------------------------------------


class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f" hola mi nombre es {self.nombre}, y tengo {self.edad} anos"
    
b1 = persona("juan",24)
print(b1)

#EJERCICIO # 3 POO----------------------------------------------------------------------------------
import math

class circulo:
    def __init__(self,radio):
        self.radio = radio
    
    def area(self):
        return   math.pi * (self.radio **2)
    
    def perimetro (self):
        return   math.pi * (self.radio **2)
    def __str__(self):
        return f"el radio {self.radio} el areal del circulo es {self.area():.2f} y el perimetro es {self.perimetro():.2f}"
    
c1 = circulo(5)
print(c1)    