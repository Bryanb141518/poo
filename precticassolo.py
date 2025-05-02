
# estaciones = {
#     "enero" : "invierno",
#     "febrero" : "invierno",
#     "marzo": "primavera",
#     "abril" : "primavera",
#     "mayo" : "primavera",
#     "junio" : "verano",
#     "julio" : "verano",
#     "agosto" : "verano",
#     "septiempre" : "otono",
#     "octubre" : "otono",
#     "noviembre" : "otono",
#     "diciembre" : "invierno"
# }
# frutas= {
#     "pera" : "enero",
#     "manzana" : "febrero",
#     "banano" : "marzo",
#     "tomate de arbol" : "abril",
#     "fresa" : "mayo",
#     "mamonsillo" : "junio",
#     "uva" : "julio",
#     "mora" : "agosto",
#     "papaya" : "septiempre",
#     "mango" : "octubre",
#     "pina" : "noviembre",
#     "melon" : "diciembre"
#
# }
# mes = input("ingrese el nombre de una fruta").lower()
#
# if mes in frutas:
#         mes = frutas[mes]
#         estacion = estaciones[mes]
#         print(f"La fruta {mes} se cosecha en {mes}, que pertenece a la estación {estacion}.")
# else:
#     print("dato no es valido")
try:
    calificacion =  int(input("ingrese su calificacion entre 0 y 100: "))

    if calificacion >= 90:
        print("A exelente")
    elif calificacion >= 80 and calificacion < 90:
        print("B muy bien")
    elif calificacion >= 70 and calificacion < 80:
        print("C  bien")
    elif calificacion >= 60 and calificacion < 70:
        print("D  sificiente")
    elif calificacion < 60:
        print("F  insuficiente")
except ValueError:
    print("ingrese una notta valida")
