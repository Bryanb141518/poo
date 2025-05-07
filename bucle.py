contador = 0
contado =0
while True:
    numero = int(input("Ingresa un numero: "))
    if numero == 0:
        print("El numero es 0 el programa a terminado")
        break
    if numero < 0:
        contador += 1
    elif numero > 0:
        contado += 1
print(f"el total de los numeros negativos ingresados fue de   {contador}")
print (f"el total de numeros positivos  ingresados fue de  {contado}")

