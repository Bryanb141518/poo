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

class persona :
    def __init__(self, nombre, edad, membresia):
        self.nombre = nombre
        self.edad = edad
        self.membresia = True
    def __str__(self):
        return f"El nombre es: {self.nombre}, la edad es: {self.edad}, la membresia es: {self.membresia}"
    def pueden_entrar(self):
        if self.edad >= 18 and self.membresia == True:
            print(f"{self.nombre} puede entrar al parque")
        else:
            print(f"{self.nombre} no puede entrar al parque")

persona1= persona("bryan",21,"si")
print(persona1)