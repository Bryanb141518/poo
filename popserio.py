
#siempre se debe crear una clase asi
# class Producto:
#     def __init__(self,codigo,nombre,precio):
#         self.__codigo = codigo
#         self.__nombre = nombre
#         self.__precio = precio
# # se crea el property por que tiene dos barra baja lo que indica que es privado
#     @property
#     def codigo(self):
#         return self.__codigo
#     # siempre despues de que se llama al valor privado se coloca @codigo.stter van de la mano
#     @codigo.setter
#     def codigo(self,valor):
#         self.__codigo = valor
#
#     @property
#     def nombre(self):
#         return self.__nombre
#
#     @nombre.setter
#     def nombre(self,valor):
#         self.__nombre = valor
#
#     @property
#     def precio(self):
#         return self.__precio
#
#     @precio.setter
#     def precio(self,valor):
#         self.__precio = valor
# # crear una funcion para calcular el total de las unidades que le demos en el print
#     def calcular_total(self, unidades):
#         return self.precio * unidades
#
# #con el str en la clase se concatenan los atributos de la clase
#     def __str__(self):
#         return f"codigo: {self.__codigo},  nombre:  {self.__nombre}, precio: {self.__precio}"
#
# p1 = Producto(23,"producto",3304)
# p2 = Producto(23,"producto",3307)
#
# print(p1,p1.calcular_total(5))
# print(p2)
#
#
# #EJERCICIO #2 POO---------------------------------------------------------------------------------
#
#
# class persona:
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad
#
#     def __str__(self):
#         return f" hola mi nombre es {self.nombre}, y tengo {self.edad} anos"
#
# b1 = persona("juan",24)
# print(b1)
#
# #EJERCICIO # 3 POO----------------------------------------------------------------------------------
# import math
#
# class circulo:
#     def __init__(self,radio):
#         self.radio = radio
#
#     def area(self):
#         return   math.pi * (self.radio **2)
#
#     def perimetro (self):
#         return   math.pi * (self.radio **2)
#     def __str__(self):
#         return f"el radio {self.radio} el areal del circulo es {self.area():.2f} y el perimetro es {self.perimetro():.2f}"
# #se coloca entre parentesis en la concatencacion la variable cuando ya se declaro el valor
# c1 = circulo(5)
# print(c1)
#
# # EJERCICIO # 4 POO --------------------------------------------------------------------------------------------
#
# class Libro:
#     def __init__(self,titulo,autor,ano,disponible):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.disponible =disponible
#
#     def prestar(self):
#         if self.disponible:
#             self.disponible = False
#             print("has tomado el libro prestado")
#         else:
#             print("el libro no esta disponible")
#     def devolver(self):
#         if not self.disponible:
#             self.disponible = True
#             print("has devuelto el libro")
#         else:
#             print("el libro ya esta disponible")
#
#
# class Usuario:
#     def __init__(self,nombre,libros_prestados):
#         self.nombre = nombre
#         self.libros_prestados =libros_prestados
#     def tomar_prestado(self,libro):
#         if libro.disponible:
#             libro.prestar()
#             self.libros_prestados.append(libro)
#             print(f"{self.nombre} tomar prestado'{libro.titulo}'.")
#         else:
#             print("el libro no esta disponible")
#     def devolver_libro(self,devolver):
#         print("devolviste el libro prestado")
#
#
# class Biblioteca:
#     def __init__(self,nombre,coleccion):
#         self.nombre=nombre
#         self.coleccion = coleccion
#     def agregar_libro(self, libro):
#         self.coleccion.append(libro)
#         print(f"Libro '{libro.titulo}' agregado a la biblioteca.")
#
#     def mostrar_libros(self):
#         print(f"Libros en la biblioteca '{self.nombre}':")
#         for libro in self.coleccion:
#             estado = "Disponible" if libro.disponible else "No disponible"
#             print(f"- {libro.titulo} ({libro.autor}, {libro.ano}) - {estado}")
#
#
# # 🌟 PRUEBA DEL SISTEMA COMPLETO 🌟
# # Crear libros
# libro1 = Libro("1984", "George Orwell", 1949, True)
# libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, True)
# libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943, False)
#
# # Crear la biblioteca
# mi_biblioteca = Biblioteca("Biblioteca Central", [libro1, libro2, libro3])
#
# # Mostrar libros en la biblioteca
# mi_biblioteca.mostrar_libros()
#
# # Crear un usuario
# usuario1 = Usuario("Brayan", [])
#
# # El usuario toma prestado un libro
# usuario1.tomar_prestado(libro1)
#
# # El usuario intenta tomar un libro ya prestado
# usuario1.tomar_prestado(libro1)
#
# # El usuario devuelve el libro
# usuario1.devolver_libro(libro1)
#
# # El usuario intenta devolver un libro que no tiene
# usuario1.devolver_libro(libro2)
#
# # Mostrar libros actualizados
# mi_biblioteca.mostrar_libros()
#
# #EJERCICIO# 4 POO ---------------------------------------------------------------------------------------------------------
#
# class Mascota:
#     def __init__(self,nombre,especie,edad):
#         self.nombre = nombre
#         self.especie = especie
#         self.edad = edad
#
#     def mostrar_info(self):
#         print(f"el nombre d ela mascota es: {self.nombre} la especie del animal es: {self.especie} y su edad es{self.edad}")
#
# class Dueño:
#     def __init__(self,nombre,mascota):
#         self.nombre = nombre
#         self.mascota = mascota
#
#     def adoptar_mascota(self,mascota):
#         pass
#
# mascota1 = Mascota("rex","perro",3)
# mascota2 = Mascota("leo","gato",4)
#
# dueno = Dueño ("ana",[])
