
def suma (a,b):
    
    resultado= a + b
    return resultado
        

a = float(input("ingrese el primer numero: "))
b = float(input("ingrese el segundo numero: "))

resultado = suma  (a, b)
print (f"el resultado de la suma de los dos numeros es: {resultado}")


numero1 = 5
numero2 = 7
resultado = numero1 + numero2

print(resultado)


a = str("hola como estas")
b = str("hola como estas")
c = str("hola como estas")

print(f"1 {a} 2 {b} 3 {c}")


nombre = "carlos"
edad = 23 
apellido = "gomez" 
list =[nombre, edad, apellido]

print(list)


hola = ("hola quiero ser programador")

print(len(hola))


numeros = [20,30,10,50]
sum4= sum(numeros) 
sum1 = len(numeros)
operacion = sum4 / sum1

print(operacion)

tuplass = (34,"hombre","ernan")
print(tuplass)

potencias =  int(input("ingrese el nuemro:" ))
exponente = int(input("ingrese el segundo numero: "))
resu = potencias ** exponente

print (f"el reslutado de {potencias}por{exponente}es = {resu}")

base = int(input("ingrese la base : "))
altura = int(input("ingrese la altura : "))
operacion =base * altura
print(f"el resultado de calcular al area de un rectangulo con los valores de {altura}por {base} es igual a{operacion } ")