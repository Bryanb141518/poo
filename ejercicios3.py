lista1 = {24,45,8,"hola"}
lista2 = {43,86,7,"hola"}
resultado =  lista1 | lista2

print (resultado)


tupla1 =("hola", 33,"si")

print(tupla1[1])

tupla3 = ("hola", 34,"edad",21)
conjunto = {32,54,76,"hola"}

union = zip(tupla3,conjunto)
print( list(union ))


numero = int(input("ingresa un numero"))

if numero > 0:
    print("your number is positive")
elif numero < 0:
    print("your number is negative")
elif numero == 0:
    print("your number is cero")
    
print(numero)


numero1 = int(input("ingresa un numero"))

if numero1 % 2 == 0:
    print("el numero es par ")
else:
    print("el numero es impar")
print(numero1)


ingreseano = int(input("ingrese el ano: "))

if ingreseano  % 400 ==0:
    print("el ano es bicesto")
elif ingreseano %100 ==0:
    print("el ano es bciesto")
elif ingreseano %4 ==0:
    print("el ano es biciesto")
else:
    print("el ano no es bicesto")
    
print(ingreseano)