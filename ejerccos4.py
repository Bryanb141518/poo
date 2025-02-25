texto = (input("ingrese el texto"))

if len(texto ) >=10:
    print("es igual o mayor a dies")
else:
    print("es menor a dies ") 
    
print(texto)

num = int(input("ingrse el numero: "))
if 1 <= num <= 100 :
    print("el numero es menor a 100")
else:
    print("el numero es mayor a 100")
    
print(num)

letra = "aeiou"
vocal = input("ingrese la letra")
if letra == vocal :
    print("es una vocal")    
else:
    print("no es una vocal")
    
number1 = int(input('ingrese el primer numero'))
number2 = int(input('ingrese el segundo numero'))
number3 = int(input('ingrese el tercer numero'))

maximo = max(number1, number2, number3)

print(f"el numero mayor es el {maximo}")

nums =int(input("ingrese el primer numero: "))

if nums % 5 == 0:
    print("el numero es divisible por 5")
elif nums % 7 ==0:
    print("el numero es divisible por 7")
else:
    print("el numero no es divisible ni por 7 ni por 5")
print(nums)

letra = "python"
palabra = input("ingrese su texto: ")

if palabra == letra:
    print("la palabra es python")
else:
    print("no es la palabra python")
    
print(letra)