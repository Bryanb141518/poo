# ejercicio #1 poo

# class usuario:
#     def __init__(self, nombre, edad,tipo):
#         self.nombre = nombre
#         self.edad = edad
#         self.tipo = tipo.lower()
#
#     def acceso_plataforma(self):
#         if self.tipo == "admin":
#             return "Acceso total a la plataforma"
#         elif self.edad >= 18 and self.tipo == "usuario":
#             return f"Acceso limitado concedido para el usuario {self.nombre}"
#         elif self.tipo == "usuario" and self.edad < 18:
#             return f"Acceso denegado para el usuario {self.nombre}, debido a que es menor de edad"
#         elif self.tipo == "moderador":
#             return f"nombre: {self.nombre}edad: {self.edad} tipo : {self.tipo}"
#         else:
#             return "tipo de usuario no reconocido"
#     def __str__(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo: {self.tipo}"
#
#
# usuario1 = usuario("bryan",21,"admin")
# print(usuario1)
# print(usuario1.acceso_plataforma())
#
#
# #ejercicio #2 -------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# class reservation:
#     def __init__(self,nombre_cliente,numero_de_noches,tipo_de_habitacion):
#         self.nombre_cliente = nombre_cliente
#         self.numero_de_noches = numero_de_noches
#         self.tipo_de_habitacion = tipo_de_habitacion.lower()
#
#     def calcular_precio(self):
#         if self.tipo_de_habitacion == "standard":
#             return self.numero_de_noches * 50
#         elif self.tipo_de_habitacion == "deluxe":
#             return self.numero_de_noches * 80
#         elif self.tipo_de_habitacion == "suite":
#             return self.numero_de_noches * 150
#         else:
#             return "Tipo de habitación no reconocida"
#
#     def modificar_reserva(self):
#         print("¿Desea modificar el nombre del cliente?")
#         respuesta = input().lower()
#         if respuesta == "sí":
#             print("Ingrese el nuevo nombre del cliente:")
#             self.nombre_cliente = input()
#         print("¿Desea modificar el número de noches?")
#         respuesta = input().lower()
#         if respuesta == "sí":
#             print("Ingrese el nuevo número de noches:")
#             self.numero_de_noches = int(input())
#         print("¿Desea modificar el tipo de habitación?")
#         respuesta = input().lower()
#         if respuesta == "sí":
#             print("Ingrese el nuevo tipo de habitación:")
#             self.tipo_de_habitacion = input()
#         else:
#             print("La reserva ha sido modificada.")
#     def __str__(self):
#         return f"Nombre del cliente: {self.nombre_cliente}, Número de noches: {self.numero_de_noches}, Tipo de habitación: {self.tipo_de_habitacion}"
# reserva1 = reservation("bryan",3,"suite")
# print(reserva1)
# print(reserva1.calcular_precio())
#
# reserva1.modificar_reserva()
# print(reserva1)
#
# #ejercicios #3----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# class membresia_gimnasio:
#     def __init__(self, nombre,edad,tipo_membresia):
#         self.nombre = nombre
#         self.edad = edad
#         self.tipo_membresia = tipo_membresia.lower()
#
#     def acceso_instalaciones(self):
#         if self.tipo_membresia == "basica":
#             return " solo Acceso a las maquinas de cardio"
#         elif self.tipo_membresia == "premium":
#             return "Acceso a carido y pesas"
#         elif self.tipo_membresia == "vip":
#             return "Acceso total incluye spa y clases grupales"
#         else:
#             return "Tipo de membresía no reconocida"
#     def cambiar_membresia(self,nueva_membresia):
#         self.topo_membresia =nueva_membresia.lower()
#         return f"Se ha cambiado la membresía de {self.tipo_membresia} a {self.tipo_membresia}"
#     def __str__(self):
#         return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo de membresía: {self.tipo_membresia}"
#
# cliente1 = membresia_gimnasio("bryan",24,"basica")
# print(cliente1)
# print(cliente1.acceso_instalaciones())
#
# cliente1.cambiar_membresia("vip")
# print(cliente1)
# print(cliente1.acceso_instalaciones())

#ejercicio # 3 -----------------------------------------------------------------------------------------------------------------------------------------------

