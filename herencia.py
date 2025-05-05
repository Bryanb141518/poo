# class Vehiculo:
#     def __init__(self, placa, modelo: int ,):
#         self.placa = placa
#         self.modelo = modelo
#
#     def mostrar_info(self):
#         return f"placa: {self.placa} modelo: {self.modelo}"
#
# class Automovil(Vehiculo):
#     def __init__(self, placa, modelo,cantidad_puertas):
#         super().__init__(placa, modelo)
#         self.cantidad_puertas = cantidad_puertas
#
#     def mostrar_info(self):
#         return f"Placa: {self.placa} Modelo: {self.modelo}  Cantidad de puertas: {self.cantidad_puertas}"
#
# class Motocicleta(Vehiculo,):
#     def __init__(self, placa, modelo, tipo_manillar: int):
#         super().__init__(placa, modelo)
#         self.tipo_manillar = tipo_manillar
#
#     def mostrar_info(self):
#         return f"Placa: {self.placa} Modelo: {self.modelo}  tipo de manillar: {self.tipo_manillar}"
#
#
# Vehiculo1 = Vehiculo("234fde",4)
# Motocicleta1 = Motocicleta ("234fd",2017,32)
#
#
#
# print (Vehiculo1.mostrar_info())
# print (Motocicleta1.mostrar_info())


#ejercicio #2---------------------------------------------------------------------------------------------------------------

# class Producto:
#     def __init__(self, nombre: str, precio: float, ):
#         self.nombre = nombre
#         self.precio = precio
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Precio: {self.precio}"
#
# class Computadora (Producto):
#     def __init__(self, nombre: str, precio: float, ram: int):
#         super().__init__(nombre, precio)
#         self.ram = ram
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Precio: {self.precio} RAM: {self.ram}"
#
# class Telefono(Producto):
#     def __init__(self, nombre: str, precio: float, camara: int):
#         super().__init__(nombre, precio)
#         self.camara = camara
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Precio: {self.precio} Cámara: {self.camara}"
#
# producto = Producto("Cargador", 15.99)
# computadora = Computadora("Laptop HP", 899.99, 16)
# telefono = Telefono("Samsung Galaxy", 799.99, 48)
#
# # Imprimir la información
# print(producto.mostrar_info())
# print(computadora.mostrar_info())
# print(telefono.mostrar_info())


#ejercicio #3---------------------------------------------------------------------------------------------------------------

# class Empleado:
#     def __init__(self, nombre: str,  salario: float):
#         self.nombre = nombre
#         self.__salario = salario
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Salario: {self.__salario}"
#
#     def aumentar_salario(self, porcentaje: float):
#         self.__salario += self.__salario * (porcentaje / 100)
#
#     def obtener_salario(self):
#         return self.__salario
#
# class Gerente (Empleado):
#     def __init__(self, nombre: str, salario: float, departamento: str):
#         super().__init__(nombre, salario)
#         self.departamento = departamento
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Salario: {self.obtener_salario()} Departamento: {self.departamento}"
#
# class Desarrollador(Empleado):
#     def __init__(self, nombre: str, salario: float, lenguaje: str):
#         super().__init__(nombre, salario)
#         self.lenguaje = lenguaje
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Salario: {self.obtener_salario()} Lenguaje: {self.lenguaje}"
#
#
# empleado1 = Empleado("Juan Pérez", 3000.00)
# gerente1 = Gerente("Ana Gómez", 5000.00, "Ventas")
# desarrollador1 = Desarrollador("Carlos Ruiz", 4000.00, "Python")
#
# # Mostrando información antes de aumento de salario
# print(empleado1.mostrar_info())
# print(gerente1.mostrar_info())
# print(desarrollador1.mostrar_info())
#
# # Aumentando salario
# empleado1.aumentar_salario(10)
# gerente1.aumentar_salario(15)
# desarrollador1.aumentar_salario(12)
#
# print("\nDespués del aumento de salario:")
# print(empleado1.mostrar_info())
# print(gerente1.mostrar_info())
# print(desarrollador1.mostrar_info())


#ejercicio #4---------------------------------------------------------------------------------------------------------------

class Vehiculo:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.ano}"
class Camion(Vehiculo):
    def __init__(self, marca: str, modelo: str, ano: int, capacidad_carga: int):
        super().__init__(marca, modelo, ano)
        self.capacidad_carga = capacidad_carga
    def mostrar_info(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.ano} Capacidad de carga: {self.capacidad_carga} toneladas"

    def aumentar_capacidad(self, porcentaje: float):
        self.capacidad_carga += self.capacidad_carga * (porcentaje / 100)

# class Autobus(Vehiculo):
#     def __init__(self, marca: str, modelo: str, ano: int, cantidad_pasajeros: int):
#         super().__init__(marca, modelo, ano)
#         self.cantidad_pasajeros = cantidad_pasajeros
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.ano} Cantidad de pasajeros: {self.cantidad_pasajeros}"
#
#     def aumentar_pasajeros(self,porcentaje: float):
#         self.cantidad_pasajeros += int(self.cantidad_pasajeros * (porcentaje /100))
#
#
# # Crear un objeto de la clase Vehiculo (solo para probar si es necesario)
# vehiculo1 = Vehiculo("Toyota", "Hilux", 2020)
#
# # Crear un objeto de la clase Camion
# camion1 = Camion("Volvo", "FH16", 2019, 20000)
#
# # Crear un objeto de la clase Autobus
# autobus1 = Autobus("Mercedes-Benz", "Sprinter", 2021, 50)
#
# # Imprimir la información antes del aumento
# print(vehiculo1.mostrar_info())
# print(camion1.mostrar_info())
# print(autobus1.mostrar_info())
#
# # Aumentar la capacidad o la cantidad de pasajeros
# camion1.aumentar_capacidad(10)  # Aumentar capacidad de carga en un 10%
# autobus1.aumentar_pasajeros(5)  # Aumentar cantidad de pasajeros en un 5%
#
# # Imprimir la información después del aumento
# print("\nDespués del aumento:")
# print(camion1.mostrar_info())
# print(autobus1.mostrar_info())


#ejercicio #5---------------------------------------------------------------------------------------------------------------

# class Dispositivo:
#     def __init__(self, marca: str, modelo: str,precio: float) :
#         self.precio = precio
#         self.marca = marca
#         self.modelo = modelo
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Precio: ${self.precio}"
#
# class Laptop(Dispositivo):
#     def __init__(self, marca: str, modelo: str, precio: float,  memoria_ram: int, ):
#         super().__init__(marca, modelo, precio)
#         self.memoria_ram = memoria_ram
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Precio: ${self.precio} Memoria RAM: {self.memoria_ram} GB"
#
# class Smartphone(Dispositivo):
#     def __init__(self, marca: str, modelo: str, precio: float, megapixeles_camara: int, ):
#         super().__init__(marca, modelo, precio)
#         self.megapixeles_camara =  megapixeles_camara
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Precio: ${self.precio} Megapixeles de cámara: {self.megapixeles_camara}"
#
#
# laptop1 = Laptop("Dell", "XPS 15", 1500.99, 16)
# smartphone1 = Smartphone("Apple", "iPhone 13", 999.99, 12)
#
# print(laptop1.mostrar_info())
# print(smartphone1.mostrar_info())


#ejercicio #6---------------------------------------------------------------------------------------------------------------

# class Animal:
#     def __init__(self, nombre: str, edad: int):
#         self.nombre = nombre
#         self.edad = edad
#
#     def hacer_sonido(self):
#         return
#
# class Perro(Animal):
#     def __init__(self, nombre: str, edad: int, raza: str):
#         super().__init__(nombre, edad, )
#         self.raza = raza
#
#     def hacer_sonido(self):
#         return "Guau!"
#
# class Gato(Animal):
#     def __init__(self, nombre: str, edad: int,color: str):
#         super().__init__(nombre, edad,)
#         self.color = color
#     def hacer_sonido(self):
#         return "Miau!"
#
# perro1 = Perro("juan",2,"pincher")
# gato1 =  Gato("juan",2,"azul")
#
# print(perro1.hacer_sonido())
# print(gato1.hacer_sonido())


#ejercicio #7---------------------------------------------------------------------------------------------------------------

# class Cuentas_bancarias:
#     def __init__(self,  nombre_titular: str, saldo: float):
#         self.nombre_titular = nombre_titular
#         self.saldo = saldo
#
#     def depositar(self, cantidad: float):
#         self.saldo += cantidad
#     def retirar(self, cantidad: float):
#         if cantidad <= self.saldo:
#             self.saldo -= self.cantidad
#         else:
#             print("No se puede retirar, saldo insuficiente.")
#     def mostrar_info(self):
#         return f"Titular: {self.nombre_titular} Saldo: ${self.saldo}"

# class Cuenta_ahorros(Cuentas_bancarias):
#     def __init__(self, nombre_titular: str, saldo: int, tasa_interes: float):
#         super().__init__(nombre_titular, saldo)
#         self.tasa_interes =tasa_interes
#
#     def mostrar_info(self):
#         return f"Titular: {self.nombre_titular} Saldo: ${self.saldo} Tasa de interés: {self.tasa_interes}%"
#
# class Cuenta_corriente(Cuentas_bancarias):
#     def __init__(self, nombre_titular: str, saldo: float, sobrejiro_permitido: int):
#         super().__init__(nombre_titular, saldo)
#         self.sobrejiro_permitido = sobrejiro_permitido
#
#     def retirar(self, cantidad: float):
#         if cantidad <= self.saldo + self.sobrejiro_permitido:
#             self.saldo -= cantidad
#         else:
#             print("No se puede retirar, supera el sobregiro permitido.")
#     def mostrar_info(self):
#         return f"Titular: {self.nombre_titular} Saldo: ${self.saldo} Sobrejiro permitido: ${self.sobrejiro_permitido}"
#
#
# cuenta_ahorros1 = Cuenta_ahorros("Juan Pérez", 5000, 0.03)  # 3% de interés
# cuenta_corriente1 = Cuenta_corriente("Ana Gómez", 2000, 1000)  # Sobregiro permitido de 1000
#
# print(cuenta_ahorros1.mostrar_info())
# print(cuenta_corriente1.mostrar_info())
#
# cuenta_ahorros1.depositar(1000)
# cuenta_corriente1.retirar(2500)  # Debe permitir sobregiro hasta 1000
#
# print("\nDespués de las operaciones:")
# print(cuenta_ahorros1.mostrar_info())
# print(cuenta_corriente1.mostrar_info())


#ejercicio #8---------------------------------------------------------------------------------------------------------------

# class Vehiculo:
#     def __init__(self, marca: str, modelo: str, precio: float):
#         self.marca = marca
#         self.modelo = modelo
#         self.precio = precio
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Precio: ${self.precio}"
#
# class Auto(Vehiculo):
#     def __init__(self, marca: str, modelo: str, precio: float, color: str, cantidad_puertas: int):
#         super().__init__(marca, modelo, precio)
#         self.color = color
#         self.cantidad_puertas = cantidad_puertas
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Precio: ${self.precio} Color: {self.color} Cantidad de puertas: {self.cantidad_puertas}"
#
# class Motocicleta(Vehiculo):
#     def __init__(self, marca: str, modelo: str, precio: float, cilindrada: int, tipo_motor: str):
#         super().__init__(marca, modelo, precio)
#         self.cilindrada = cilindrada
#         self.tipo_motor = tipo_motor
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Precio: ${self.precio} Cilindrada: {self.cilindrada} CC {self.tipo_motor}"
#
#
# auto1 = Auto("Toyota", "Corolla", 25000, "azul",4)
# moto1 = Motocicleta("Yamaha", "MT-07", 7500, 2514 ,"gfgds")
#
# print(auto1.mostrar_info())
# print(moto1.mostrar_info())


#ejercicio #9---------------------------------------------------------------------------------------------------------------

# class Empleado:
#     def __init__(self, nombre: str, edad: str, salario: float):
#         self.nombre = nombre
#         self.edad = edad
#         self.salario = salario
#
# class Gerente(Empleado):
#     def __init__(self, nombre: str, edad: str, salario: float, puesto: str,departamento: str):
#         super().__init__(nombre, edad, salario)
#         self.puesto = puesto
#         self.departamento = departamento
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Edad: {self.edad} Salario: ${self.salario} Puesto: {self.puesto} Departamento: {self.departamento}"
#     def nuevo_departamento(self):
#         self.departamento = input("Ingrese el nuevo departamento: ")
#
# class Desarrollador(Empleado):
#     def __init__(self, nombre: str, edad: str, salario: float, lenguajes_programacion: list):
#         super().__init__(nombre, edad, salario)
#         self.lenguajes_programacion = lenguajes_programacion
#
#     def mostrar_info(self):
#         return f"Nombre: {self.nombre} Edad: {self.edad} Salario: ${self.salario} Lenguajes de programación: {', '.join(self.lenguajes_programacion)}"
#     def agregar_lenguaje(self):
#         nuevo_lenguaje = input("Ingrese un nuevo lenguaje de programación: ")
#         self.lenguajes_programacion.append(nuevo_lenguaje)
#
# gerente1 = Gerente("Carlos López", 45, 5000, "Ventas","cuarto")
# desarrollador1 = Desarrollador("Ana Pérez", 30, 4000, ["python"])
#
# print(gerente1.mostrar_info())
# print(desarrollador1.mostrar_info())


#ejercicio #10---------------------------------------------------------------------------------------------------------------

# class Dispositivo_electronico:
#     def __init__(self, marca: str, modelo: str, ):
#         self.marca = marca
#         self.modelo = modelo
#
# class Telefono(Dispositivo_electronico):
#     def __init__(self, marca: str, modelo: str, color: str, memoria_interna: int, numero_telefono: int):
#         super().__init__(marca, modelo)
#         self.color = color
#         self.memoria_interna = memoria_interna
#         self.numero_telefono = numero_telefono
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Color: {self.color} Memoria interna: {self.memoria_interna}GB Numero de teléfono: {self.numero_telefono}"
#
#     def realizar_llamada(self,numero_telefono):
#         if  numero_telefono == input("ingrese el numero de teléfono"):
#             return f"Llamando a {numero_telefono}"
#         else:
#             return "El número de teléfono ingresado es incorrecto"
#
# class Computadora(Dispositivo_electronico):
#     def __init__(self, marca: str, modelo: str, procesador: str, memoria_ram: int, sistema_operativo: str):
#         super().__init__(marca, modelo)
#         self.procesador = procesador
#         self.memoria_ram = memoria_ram
#         self.sistema_operativo = sistema_operativo
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Procesador: {self.procesador} Memoria RAM: {self.memoria_ram}GB Sistema operativo: {self.sistema_operativo}"
#
# telefono1 = Telefono("Samsung", "Galaxy S21", "azul",128,3204324243)
# computadora1 = Computadora("Dell", "XPS 15", "intel",8,"linux")
#
# print(telefono1.mostrar_info())
# print(computadora1.mostrar_info())


#ejercicio #11---------------------------------------------------------------------------------------------------------------

# class Cuenta_bancaria:
#     def __init__(self, titular: str, saldo: float , moneda: str):
#         self.titular = titular
#         self.saldo = saldo
#         self.moneda = moneda
#
#     def depositar(self,monto: float):
#         self.saldo += monto
#     def retirar(self,monto: float):
#         if monto > self.saldo:
#             print("No hay suficiente saldo.")
#         else:
#             self.saldo -= monto
# class Cuenta_ahorros(Cuenta_bancaria):
#     def __init__(self, titular: str, saldo: float, tasa_interes: float, moneda: str):
#         super().__init__(titular, saldo, moneda)
#         self.tasa_interes = tasa_interes
#     def aplicar_interes(self):
#         interes = self.saldo * self.tasa_interes
#         self.saldo += interes
#
#     def mostrar_info(self):
#         return f"Titular: {self.titular} Saldo: {self.saldo} {self.tasa_interes} Tasa de interés: {self.moneda}"
#
# class Cuenta_corriente(Cuenta_bancaria):
#     def __init__(self, titular: str, saldo: float, moneda: str, sobregiro_maximo: float):
#         super().__init__(titular, saldo, moneda)
#         self.sobregiro_maximo =sobregiro_maximo
#
#     def retirar(self,monto: float):
#         if monto > self.saldo + self.sobregiro_maximo:
#             print("No se puede retirar más de lo que tiene en sobregiro.")
#         else:
#             self.saldo -= monto
#     def mostrar_info(self):
#         return f"Titular: {self.titular} Saldo: {self.saldo} {self.moneda} Sobregiro máximo: {self.sobregiro_maximo}"
#
# cuenta1 = Cuenta_ahorros("Carlos Pérez", 1000, 0.02, "USD")
# cuenta2 = Cuenta_corriente("Ana Gómez", 500, "COP", 200)
#
# cuenta1.depositar(500)
# cuenta1.aplicar_interes()
# print(cuenta1.mostrar_info())  # Muestra el saldo actualizado con intereses
#
# cuenta2.retirar(600)  # Permite retirar hasta el sobregiro máximo
# print(cuenta2.mostrar_info())


#ejercicio #12---------------------------------------------------------------------------------------------------------------
# class Material_bibliografico:
#     def __init__(self, titulo: str, autor: str, editorial: str, ano_publicacion: int):
#         self.titulo = titulo
#         self.autor = autor
#         self.editorial = editorial
#         self.ano_publicacion = ano_publicacion
#
#     def mostrar_info(self):
#         return f"Título: {self.titulo} Autor: {self.autor} Editorial: {self.editorial} Año de publicación: {self.ano_publicacion}"
#
# class Libro(Material_bibliografico):
#     def __init__(self, titulo: str, autor: str, editorial: str, ano_publicacion: int, genero: str,num_paginas: int):
#         super().__init__(titulo, autor, editorial, ano_publicacion)
#         self.genero = genero
#         self.num_paginas = num_paginas
#
#
#     def mostrar_info(self):
#         return super().mostrar_info() + f" Género: {self.genero} Número de páginas: {self.num_paginas}"
#
# class Revista(Material_bibliografico):
#     def __init__(self, titulo: str, autor: str, editorial: str, ano_publicacion: int, edicion:str, mes_publicacion):
#         super().__init__(titulo, autor, editorial, ano_publicacion)
#         self.edicion = edicion
#         self.mes_publicacion = mes_publicacion
#     def mostrar_info(self):
#         return super().mostrar_info() + f" Edición: {self.edicion} Mes de publicación: {self.mes_publicacion}"
#
#
# libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "panamericana", 1998,"realismo magico",456)
# revista1 = Revista("National Geographic", "Varios", "panamericana", 1898, "vol #2","Diciembre")
#
# print(libro1.mostrar_info())
# print(revista1.mostrar_info())



#ejercicio #13---------------------------------------------------------------------------------------------------------------
#
# class Vehiculo:
#     def __init__(self, marca: str, modelo: str, ano: int,kilometraje: int):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.kilometraje = kilometraje
#
# class Auto(Vehiculo):
#     def __init__(self, marca: str, modelo: str, ano: int, kilometraje: int, tipo_combustible:str):
#         super().__init__(marca, modelo, ano, kilometraje)
#         self.tipo_combustible = tipo_combustible
#
#     def calcular_autonomia(self):
#         if self.tipo_combustible == "gasolina":
#             autonomia = 12 * (100 - self.kilometraje)
#         elif self.tipo_combustible == "diesel":
#             autonomia = 8 * (100 - self.kilometraje)
#         else:
#             autonomia = 0
#         return autonomia
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.ano} Kilometraje: {self.kilometraje} Kilometraje autónomo: {self.calcular_autonomia()}"
#
# class Moto(Vehiculo):
#     def __init__(self, marca: str, modelo: str, ano: int, kilometraje: int, cilindrada: int):
#         super().__init__(marca, modelo, ano, kilometraje)
#         self.cilindrada = cilindrada
#
#     def es_de_alta_cilindrada(self):
#         if self.cilindrada >= 500:
#             return True
#         else:
#             return False
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.ano} Kilometraje: {self.kilometraje} Cilindrada: {self.cilindrada} Es de alta cilindrada: {self.es_de_alta_cilindrada()}"
#
# class Camion(Vehiculo):
#     def __init__(self, marca: str, modelo: str, ano: int, kilometraje: int, capacidad_carga: int):
#         super().__init__(marca, modelo, ano, kilometraje)
#         self.capacidad_carga = capacidad_carga
#
#     def puede_transportar(self,):
#         if self.capacidad_carga > 10000:
#             return True
#         else:
#             return False
#
#     def mostrar_info(self):
#         return f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.ano} Kilometraje: {self.kilometraje} Capacidad de carga: {self.capacidad_carga} Puede transportar: {self.puede_transportar()}"
#
# auto1 = Auto("Toyota", "Corolla", 2020, 30000, "Gasolina")
# print(auto1.mostrar_info())  # Información completa del auto
# print(auto1.calcular_autonomia())  # Calcula la autonomía
#
# moto1 = Moto("Yamaha", "R1", 2022, 5000, 1000)
# print(moto1.mostrar_info())
# print(moto1.es_de_alta_cilindrada())  # True
#
# camion1 = Camion("Volvo", "FH16", 2018, 120000, 30000)
# print(camion1.mostrar_info())
# print(camion1.puede_transportar())  # True
# print(camion1.puede_transportar())  # False
