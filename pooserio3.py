class gimnasio:
    def __init__(self,nombre, edad, membresia):
        self.nombre = nombre
        self.edad = edad
        self.membresia = membresia.lower()

    def membresia1(self):
        if self.membresia == "premium" and self.edad >= 18:
            print("puedes acceder a la sala vip")
        else:
            print(f"tu membreisa es {self.membresia} y tu edad es {self.edad}por consiguente no puedes pasar a la sala vip")

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - {self.membresia}"

persona1 = gimnasio("bryan",20,"premium")
print(persona1)
persona1.membresia1()

# ejercicio #2 poo----------------------------------------------------------------------------------------------------------------------
class empleado:
    def __init__(self, nombre, horas_trabajadas, salario_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.salario_por_hora = salario_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.salario_por_hora
    def __str__(self):
        return f"{self.nombre} - {self.horas_trabajadas} horas - {self.salario_por_hora} - {self.calcular_salario()}"
    def evaluar_desempeno(self):
        if self.horas_trabajadas >= 160:
            return "excelente"
        elif self.horas_trabajadas >=121:
            return "bueno"
        else:
            return "regular"

persona2 = empleado("bryan",140,112345)
print(persona2)
print(persona2.evaluar_desempeno())

# ejercicio #3 poo----------------------------------------------------------------------------------------------------------------------

class Libro:
    def __init__(self, titulo, autor, ano, disponible):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponible = disponible.lower() == "si"

    def prestar(self):
        if self.disponible:
            return "el libro se encuantra disponible "
        else:
            return "el libro no se encuentra disponible"

    def devolver(self):
        self.disponible = "libro devuelto con exito"
        return "disponible"
    def __str__(self):
        return f"{self.titulo} - {self.autor} - {self.ano} - {self.disponible}"

libro1 = Libro("100 anos de doledad","gabriel garcia marquez",1998,"no")
print(libro1)
print(libro1.prestar())




# ejercicio #4 poo----------------------------------------------------------------------------------------------------------------------
class invitado:
    def __init__(self, nombre, edad, vip):
        self.nombre = nombre
        self.edad = edad
        self.vip =  vip.lower() =="si"

    def __str__(self):
        return f"{self.nombre} - {self.edad} años - {"vip" if self.vip else "general"}"

    def verificar_acceso(self):
        if self.vip  and self.edad >= 18:
            return "acceso permitido a la zona vip"
        elif not self.vip == False and self.edad >= 18:
            return "acceso permitido a la zona general"
        else:
            return "no puedes ingresar al evento"

persona1 = invitado("bryan",21,"si")
print(persona1)
print(persona1.verificar_acceso())

# ejercicio #5 poo----------------------------------------------------------------------------------------------------------------------

class ReservaRestaurante:
    def __init__(self, nombre, personas, hora, confirmada):
        self.nombre = nombre
        self.personas = personas
        self.hora = hora
        self.confirmada = False

    def __str__(self):
        return f"{self.nombre} - {self.personas} personas - {self.hora} horas - {self.confirmada}"
    def verificar_disponibilidad(self):
        if self.personas < 6 and  12 <= self.hora <= 22 :
            return "reserva disponible"
        elif self.personas  >= 6 and 19 >= self.hora <= 21 :
            return "reserva disponible"
        else:
            return "no hay disponivilidad de reserva"

persona4 = ReservaRestaurante("bryan", 5,14,"si")
print(persona4)
print(persona4.verificar_disponibilidad())