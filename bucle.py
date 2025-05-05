numero = int(input("Ingresa un numero: "))
contador = 1
while contador <= numero:
    print(contador)
    contador += 1

num = int(input("Ingresa un numero: "))
while num :
    if num % 2 == 1:
        print("El numero es impar")
        break
    else:
        print("El numero es par")
        break

num1 = int(input("adivina un numero entre 1 y 100: "))
num2 = 32

while num1 != num2:
    print("El numero es incorrecto")
    num1 = int(input("adivina un numero entre 1 y 100: "))
print("El numero es correcto")
