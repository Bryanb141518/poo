# # control temperatrura
# from poo3 import usuario
#
# temperatura = int( input ("coloca la temperatura"))
#
# if temperatura <= 0 :
#     print("hace frio")
# elif 0 < temperatura <= 30 :
#     print("temperatura agradable")
# elif temperatura >= 31:
#     print("hace calor")
# else:
#     print("ingresaste un valor diferente")
#
# print("temperatura")
# #ejercicio #2 -------------------------------------------------------------------------------------------------------------------------------------------
#
# numero = int( input ("ingrese un numero"))
# if numero > 0 and numero % 2 == 0 :
#     print("el numero es positivo y es par")
# elif numero >0 and numero % 2 != 0 :
#      print("el numero es positivo y es impar")
# elif numero < 0 :
#     print("el numero es negativo")
# elif numero == 0:
#     print("el numero es cero")
# else:
#     print("ingrese un numero valido")
# print(numero)

#ejercicio #3-----------------------------------------------------------------------------------------------------------------------------------------------------

# try:
#         numero = int(input("ingrese un numero"))
#
#         if numero > 0:
#             if numero % 2 == 0:
#                 print("el numero es positivo y es par")
#             else:
#                 print("el numero es positivo y es impar")
#         elif numero < 0 :
#             print("el numero es negativo")
#         else:
#             print("el numero es cero")
# except ValueError:
#         print("Debes ingresar un número")
#
#
# print(numero)

#ejercicio #4----------------------------------------------------------------------------------------------------------------------------------------------------
# try:
#     peso = int(input("ingrere su peso"))
#
#     if peso < 29.9:
#         if peso >=25 and peso <= 29.9:
#             print("sobrepeso")
#         elif peso >=18.5 and peso <=24.9:
#             print("peso normal")
#         elif peso < 18:
#             print("bajo peso")
#     else:
#             print("obesidad")
# except ValueError:
#             print("Debes ingresar un numero y que sea positivo")
#
# print (peso)


#ejercicio #5 -----------------------------------------------------------------------------------------------------------------------------------------------------
# try:
#     precio = int(input("precio de la membresia es "))
#     edad = int(input("ingrese su edad "))
#     descuento = 0
#     if edad > 0:
#         if edad >= 60:
#             descuento = 0.6
#             print("obtiene un descuento del 60%")
#         elif edad >= 18 :
#             print("no obtiene descuento")
#         elif edad  < 18 :
#             descuento = 0.3
#             print("obtiene un descuento del 30%")
#
#         precio_final = precio * (1 - descuento)
#         print(f"el precio con descuento es: {precio_final:.2f}")
#
#     else:
#         print("Debes ingresar una edad valida")
# except ValueError:
#     print("Debes ingresar un numero y que sea positivo")
# print(precio,edad)

# ejercicio # 6 -------------------------------------------------------------------------------------------------------------------------

# numero = int(input("ingrese un numero: "))
#
# if numero == 0:
#     print("el numero es cero")
# elif numero < 0:
#     print("el numero es negativo")
# else:
#     print("el numero es positivo")
#
# print(numero)

# contrasena  = input("ingrese una contrasena: ")
# if contrasena == "phthon123*":
#     print("Contrasena correcta")
# else:
#     print("Contrasena incorrecta")
# print(contrasena)
# try:
#     numero = int(input("ingrese un numero entre el 1 y el 10: "))
#     if numero >=1 and numero <= 10:
#         print("El numero debe estar entre el 1 y el 10")
#     elif numero == 7:
#         print("felicidades adivinastel el numero")
#     else:
#         print("Intente de nuevo")
# except ValueError:
#     print("Debes ingresar un numero")
# print(numero)


# #ejercicio # 7 -------------------------------------------------------------------------------------------------------------------------
#
# print("1. suma")
# print("2. resta")
# print("3. multiplicacion")
# print("4. division")
#
# operacion = int(input("ingrese la operacion a realizar: "))
#
# numero1 = int(input("ingrese el primer numero"))
# numero2 = int(input("ingrese el segundo numero"))
#
# if operacion == 1:
#     resultado = numero1 + numero2
#     print(f"El resultado de la suma es: {resultado}")
# elif operacion == 2:
#     resultado = numero1 - numero2
#     print(f"El resultado de la resta es: {resultado}")
# elif operacion == 3:
#     resultado = numero1 * numero2
#     print(f"El resultado de la multiplicacion es: {resultado}")
# elif operacion == 4:
#     if numero2 == 0:
#         print("Error, no se puede dividir por cero")
#     else:  # division normal
#         resultado = numero1 / numero2
#         print(f"El resultado de la division es: {resultado:.2f}")
# else:
#     print("ingrese una operacion valida")
# print(numero1,numero2)


# #ejercicio # 8 -------------------------------------------------------------------------------------------------------------------------
# numero1 = int(input("ingrese la primera longitud"))
# numero2 = int(input("ingrese la segunda longitud"))
# numero3 = int(input("ingrese la tercera longitud"))
# if numero1 + numero2 > numero3 and numero1 + numero3 > numero2 and numero3 + numero2 > numero1:
#     if numero1 == numero2 == numero3:
#         print("es un triangulo equilatero")
#     elif numero1 ==2 != numero3 or  numero2 == numero3 != numero1:
#         print("es un triangulo isosceles")
#     elif numero1 != numero3 != numero2:
#         print("es un triangulo escaleno")
# print(numero1,numero2,numero3)


# #ejercicio # 9 -------------------------------------------------------------------------------------------------------------------------
# ano = int(input("ingrese un ano:"))
# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano % 400 == 0:
#             print(f"{ano} es un ano bisiesto")
#         else:
#             print(f"{ano} no es un ano bisiesto")
#     else:
#         print(f"{ano} es un ano bisiesto")
# else:
#     print(f"{ano} no es un ano bisiesto")
# print(ano)


# #ejercicio # 10 -------------------------------------------------------------------------------------------------------------------------

# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# num3 = int(input("ingrese el tercer numero: "))
#
# if num1 == num2 and  num2 == num3:
#     print("los numeros son iguales")
# else:
#     print(f"el numero menor es : {min(num1, num2 ,num3)}")
#     print(f"el numero mayor es : {max(num1, num2 ,num3)}")
# print(num1, num2, num3)


# #ejercicio # 11 -------------------------------------------------------------------------------------------------------------------------

# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))
# num3 = int(input("ingrese el tercer numero: "))
# num4 = int(input("ingrese el cuarto numero: "))
#
# if num1 != num2 and num1 != num3 and num1 != num4:
#     print("los numeros son diferentes")
# else:
#     print("algunos numeros son iguales")
# print(num1, num2, num3, num4)
#
# print (f"el numero mayor es: {max(num1, num2, num3,num4)}")
# print (f"el numero menor es: {min (num1,num2,num3,num4)}")


# #ejercicio # 12 -------------------------------------------------------------------------------------------------------------------------

# num1 = input("ingrese una hora en formato de 24 horas: ")
# try:
#     horas ,minutos = map(int, num1.split(":"))
#     if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
#         print("La hora ingresada no es valida")
#     else:
#         if horas >= 6 and horas < 12:
#             print("Es de manana")
#         elif horas >= 12 and horas <18:
#             print("Es de tarde")
#         elif horas >= 18 and horas <= 23:
#             print("Es de noche")
#         else:
#             print("Es de madrugada")
#
# except ValueError:
#     print("Debe ingresar una hora en formato de 24 horas, ejemplo: 12,00")
# print(num1)


# #ejercicio # 13 -------------------------------------------------------------------------------------------------------------------------
# num1 = int(input("ingrese el primer angulo "))
# num2 = int(input("ingrese el segundo angulo"))
# num3 = int(input("ingrese el tercer angulo"))
#
# if num1 + num2 + num3 == 180:
#
#     if num1 == 90 or num2 == 90 or num3 == 90:
#         print("es un triangulo rectangulo")
#     elif num1 > 90 or num2 > 90 or num3> 90:
#         print("es un triangulo obtusangulo")
#     elif num1 < 90 and num2 < 90 and num3 < 90:
#         print("es un triangulo acutangulo")
# else:
#     print("los angulos no suman 180 grados")
#
#
# print(num1,num2,num3)


# #ejercicio # 14 -------------------------------------------------------------------------------------------------------------------------
# peso = int(input("ingrese su peso"))
# altura = int(input("ingrese su estatura en centimetros"))
# altura = altura / 100
# imc  =  peso / (altura ** 2)
# print(f"Tu IMC es:{imc:.2f}")
# if imc < 18.5:
#     print("Peso bajo")
# elif imc < 25:
#     print("Peso normal")
# elif  imc < 30:
#     print("Sobrepeso")
# elif  imc < 35:
#     print("Obesidad grado I")
# elif  imc < 40:
#     print("Obesidad grado II (severa)")
# else:
#     print("Obesidad grado III (muerte)")
# print(peso,altura)



# #ejercicio # 15 -------------------------------------------------------------------------------------------------------------------------

# num1 = int(input("ingrese la cantidad de kilometros: "))
# num2 = (input("ingrese la hora del viaje (formato 24h)"))
#
# horas , minutos = map(int, num2.split(":"))
# tarifa_base = 4000 +(num1 * 100)
#
#
# if horas >= 22 or horas < 6:
#     tarifa_base *=1.2
#     print("el precio se incrementa un 20%por la hora del viaje")
#
#
# print(num1,num2)


# #ejercicio # 16 -------------------------------------------------------------------------------------------------------------------------

# nota = float(input("ingrese su nota: "))
# if  0.0 <=  nota <= 5.0:
#     if   nota >= 4.5:
#         print("el estudiente tiene un desempeno exelente")
#     elif  3.5 <= nota < 4.5:
#         print("el estudiente aprueba")
#     elif  3.0 <= nota < 3.5:
#         print("el estudiante esta en riesgo")
#     else:
#         print("ele studiante reprueba ")
# else:
#     print("la nota ingresada no es valida")

#ejercicio # 17 ------------------------------------------------------------------------------------------------------------------------
#
# metro = float(input("ingrse su altura"))
# if  metro >= 1.40:
#     print("puede subir sin restricciones")
# elif  1.20 <= metro < 1.40 :
#     print("puede subir solo con un adulto")
# else:
#     print("puede no  subir por que mide menos de 1.20")




#ejercicio # 18 -------------------------------------------------------------------------------------------------------------------------

# edad = int(input("ingrese su edad"))
# entrada =15000
#
# if edad <5:
#     precio_final = 0
#     print("ingresas gratis")
# elif edad > 60:
#     descuento = 0.50
#     precio_final =entrada * (1 - descuento)
#     print("obtiene un descuento del 50%")
# elif edad >17 and edad <=59:
#     print("no obtiene s decuento")
# elif edad >=13 and edad <= 17:
#     descuento = 0.20
#     precio_final =entrada * (1 - descuento)
#     print("obtuiste un descuento del 20%")
# elif edad >= 5 and  edad<= 12 :
#     descuento = 0.40
#     precio_final =entrada * (1 - descuento)
#     print("obitneie un descuento del 40%")
# else:
#     print("ingrese una edad valida")