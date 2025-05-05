# class gimnasio:
#     def __init__(self,nombre, edad, membresia):
#         self.nombre = nombre
#         self.edad = edad
#         self.membresia = membresia.lower()
#
#     def membresia1(self):
#         if self.membresia == "premium" and self.edad >= 18:
#             print("puedes acceder a la sala vip")
#         else:
#             print(f"tu membreisa es {self.membresia} y tu edad es {self.edad}por consiguente no puedes pasar a la sala vip")
#
#     def __str__(self):
#         return f"{self.nombre} ({self.edad} años) - {self.membresia}"
#
# persona1 = gimnasio("bryan",20,"premium")
# print(persona1)
# persona1.membresia1()
#
# # ejercicio #2 poo----------------------------------------------------------------------------------------------------------------------
# class empleado:
#     def __init__(self, nombre, horas_trabajadas, salario_por_hora):
#         self.nombre = nombre
#         self.horas_trabajadas = horas_trabajadas
#         self.salario_por_hora = salario_por_hora
#
#     def calcular_salario(self):
#         return self.horas_trabajadas * self.salario_por_hora
#     def __str__(self):
#         return f"{self.nombre} - {self.horas_trabajadas} horas - {self.salario_por_hora} - {self.calcular_salario()}"
#     def evaluar_desempeno(self):
#         if self.horas_trabajadas >= 160:
#             return "excelente"
#         elif self.horas_trabajadas >=121:
#             return "bueno"
#         else:
#             return "regular"
#
# persona2 = empleado("bryan",140,112345)
# print(persona2)
# print(persona2.evaluar_desempeno())
#
# # ejercicio #3 poo----------------------------------------------------------------------------------------------------------------------
#
# class Libro:
#     def __init__(self, titulo, autor, ano, disponible):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano
#         self.disponible = disponible.lower() == "si"
#
#     def prestar(self):
#         if self.disponible:
#             return "el libro se encuantra disponible "
#         else:
#             return "el libro no se encuentra disponible"
#
#     def devolver(self):
#         self.disponible = "libro devuelto con exito"
#         return "disponible"
#     def __str__(self):
#         return f"{self.titulo} - {self.autor} - {self.ano} - {self.disponible}"
#
# libro1 = Libro("100 anos de doledad","gabriel garcia marquez",1998,"no")
# print(libro1)
# print(libro1.prestar())
#
#
#
#
# # ejercicio #4 poo----------------------------------------------------------------------------------------------------------------------
# class invitado:
#     def __init__(self, nombre, edad, vip):
#         self.nombre = nombre
#         self.edad = edad
#         self.vip =  vip.lower() =="si"
#
#     def __str__(self):
#         return f"{self.nombre} - {self.edad} años - {"vip" if self.vip else "general"}"
#
#     def verificar_acceso(self):
#         if self.vip  and self.edad >= 18:
#             return "acceso permitido a la zona vip"
#         elif not self.vip == False and self.edad >= 18:
#             return "acceso permitido a la zona general"
#         else:
#             return "no puedes ingresar al evento"
#
# persona1 = invitado("bryan",21,"si")
# print(persona1)
# print(persona1.verificar_acceso())
#
# # ejercicio #5 poo----------------------------------------------------------------------------------------------------------------------
#
# class ReservaRestaurante:
#     def __init__(self, nombre, personas, hora, confirmada):
#         self.nombre = nombre
#         self.personas = personas
#         self.hora = hora
#         self.confirmada = False
#
#     def __str__(self):
#         return f"{self.nombre} - {self.personas} personas - {self.hora} horas - {self.confirmada}"
#     def verificar_disponibilidad(self):
#         if self.personas < 6 and  12 <= self.hora <= 22 :
#             return "reserva disponible"
#         elif self.personas  >= 6 and 19 >= self.hora <= 21 :
#             return "reserva disponible"
#         else:
#             return "no hay disponivilidad de reserva"
#
# persona4 = ReservaRestaurante("bryan", 5,14,"si")
# print(persona4)
# print(persona4.verificar_disponibilidad())
# from poo3 import cliente1


# # ejercicio #6-------------------------------------------------------------------------------------------------------------------
# class estudiante:
#     def __init__(self, nombre, edad,notas):
#         self.nombre = nombre
#         self.edad = edad
#         self.notas = notas if isinstance(notas,list)else[notas]
#     def agregar_nota(self,):
#         self.notas.append(float(input("Ingrese una nota: ")))
#         print("Nota agregada con éxito")
#     def calcular_promedio(self):
#         if len(self.notas) == 0:
#             return 0
#         return sum(self.notas)/ len(self.notas)
#     def __str__(self):
#         return f"{self.nombre} - {self.edad} años - Promedio: {self.calcular_promedio()}"
#
#     def mostrar_info(self):
#         print(f"Nombre: {self.nombre}, Edad: {self.edad}, Promedio: {self.calcular_promedio():.2f}")
#
# uno = estudiante("brayan",24,10)
# uno.mostrar_info()
#
# # print(uno.mostrar_info())
# # print(uno)
#
# # ejercicio #7 ----------------------------------------------------------------------------------------------------
#
# # class empleado:
# #     def __init__(self, nombre, cargo, salario):
# #         self.nombre = nombre
# #         self.cargo = cargo
# #         self.salario = salario
# #     def salario1(self):
# #         if self.salario <= 3000:
# #             return self.salario * 1.10
# #         else:
# #             return "no tienes un aumento de sueldo disponible"
# #     def mostrar_info(self):
# #         return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Salario: {self.salario:.2f}"
# #     def __str__(self):
# #         return self.mostrar_info()
# # empleado1 = empleado("bryan","promgramador",2500)
# #
# # print(empleado1.mostrar_info())
# # print("Nuevo salario", empleado1.salario1())
#
#
# # ejercicio # 8-------------------------------------------------------------------------------------------
#
# class libro:
#     def __init__(self, titulo, autor,cantidad_disponible):
#         self.titulo = titulo
#         self.autor = autor
#         self.cantidad_disponible = cantidad_disponible
#
#     def info_libro(self):
#         return f"Título: {self.titulo}, Autor: {self.autor}, Cantidad disponible: {self.cantidad_disponible}"
#
# class usuario:
#     def __init__(self, nombre, id_usuario):
#         self.nombre = nombre
#         self.id_usuario = id_usuario
#
#     def info_usuario(self):
#         return f"Nombre: {self.nombre}, ID Usuario: {self.id_usuario}"
#
# class prestamo:
#     def __init__(self, usuario,):
#         self.usuario = usuario
#         self.lista_prestados = []
#
#     def prestamo(self,libro):
#             if self.lista_prestados:
#                 libro_prestado = self.lista_prestados.pop(0)
#                 libro_prestado.cantidad_disponible -= 1
#                 print(f"El usuario {self.usuario.nombre} ha prestado el libro {libro_prestado.titulo}")
#             else:
#                 print(f"El usuario {self.usuario.nombre} no tiene libros disponibles")
#
#     def devolver_libro(self,libro):
#         if libro.cantidad_disponible > 0:
#             libro.cantidad_disponible -= 1
#             self.lista_prestados.append(libro)
#             print(f"El usuario {self.usuario.nombre} ha prestado el libro {libro.titulo}")
#         else:
#             print(f"No hay copias disponibles de {libro.titulo}")
#
#     def info_prestados(self):
#         if self.lista_prestados:
#             return f"El usuario {self.usuario.nombre} tiene prestados los siguientes libros: {', '.join([libro.titulo for libro in self.lista_prestados])}"
#         else:
#             return f"El usuario {self.usuario.nombre} no tiene libros prestados"
#
#
#
# libro1 = libro("Python desde cero", "Guido van Rossum", 3)
# libro2 = libro("Estructuras de datos", "John Smith", 2)
#
# # Crear usuario
# usuario1 = usuario("Brayan", 101)
#
# # Crear préstamo
# prestamo1 = prestamo(usuario1)
#
# # Prestar un libro
# prestamo1.prestamo(libro1)
#
# # Mostrar libros prestados
# print(prestamo1.info_prestados())
#
# # Devolver un libro
# prestamo1.devolver_libro(libro1)
#
# # Mostrar estado final
# print(prestamo1.info_prestados())
#
#
#
