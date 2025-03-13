class Empleado:
    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def mostrar_informacion(self):
        print(f"el nombre del empleado es {self.nombre} su edad es {self.edad} su salario es {self.salario}")
        
class Gerente(Empleado):
    def __init__(self,nombre,edad,salario,departamento):
        super().__init__(nombre,edad,salario)
        self.departamento = departamento
    def mostrar_informacion(self):
        print(f"el nombre del empleado es {self.nombre} su edad es {self.edad} su salario es {self.salario} y su departamento es{self.departamento}")
    
empleado1 = Empleado("Carlos", 30, 3000)
gerente1 = Gerente("Ana", 40, 5000, "Ventas")

empleado1.mostrar_informacion()
gerente1.mostrar_informacion()

#ejercicio con poo #2 ---------------------------------------------------------------------------------------------------------------------------------------------


class Vehiculo:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f"la marca del vehiculo es: {self.marca} el modelo es: {self.modelo} el ano es: {self.ano}"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, ano,puertas,combustible ):
        super().__init__(marca, modelo, ano)
        self.puertas =puertas
        self.combustible = combustible
    
    def __str__(self):
         return f"la marca del vehiculo es: {self.marca} el modelo es: {self.modelo} el ano es: {self.ano} las puesrtas son: {self.puertas} y su combustible es {self.combustible}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano,cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada
    
    def __str__(self):
        return f"la marca del vehiculo es: {self.marca} el modelo es: {self.modelo} el ano es: {self.ano} la cilidrada de la mosto es {self.cilindrada}"
    
coche1 = Coche("Toyota", "Corolla", 2022, 4, "Gasolina")
moto1 = Motocicleta("Honda", "CBR", 2023, 650)

print(coche1)
print(moto1)

# ejercicio con poo # 3 ----------------------------------------------------------------------------------------------------------------------------------------------------

class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio 
        self.stock =stock
        
    def mostrar_infromacion(self):
        return f"nombre del cliente {self.nombre} el precio del producto es: {self.precio} el stock del profucto es: {self.stock}"
    def actualizar_stock(self,cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        else:
            print(f"no hay suficionete stockde {self.nombre}.")
            return False

class Carrito:
    def __init__(self,lista_de_productos_anadidos =None):
        self.lista_de_productos_anadidos = lista_de_productos_anadidos or []
    
    def agregar_producto_al_carrito(self ,producto,cantidad):
        print(f"agregaste un nuevo producto al carrito {self.agregar_producto_al_carrito}")
    
    def mostrar_productos(self):
        """Muestra los productos en el carrito."""
        if not self.lista_de_productos_anadidos:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto, cantidad in self.lista_de_productos_anadidos:
                print(f"{cantidad}x {producto.nombre} - ${producto.precio * cantidad}")

    def calcular_total(self):
        """Calcula el total a pagar de los productos en el carrito."""
        total = sum(producto.precio * cantidad for producto, cantidad in self.lista_de_productos_anadidos)
        print(f"Total a pagar: ${total}")
        
producto1 = Producto("Camiseta", 20, 5)
producto2 = Producto("Zapatos", 50, 2)
producto3 = Producto("Gorra", 15, 10)

carrito = Carrito()

carrito.agregar_producto(producto1, 2)
carrito.agregar_producto(producto2, 1)
carrito.agregar_producto(producto3, 3)

carrito.mostrar_carrito()