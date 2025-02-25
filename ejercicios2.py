usuario = input("ingrese su nombre: ")
print(f"nombre de usuario es {usuario} hola {usuario} como esta ")


numero = int(input("ingrese un numero: "))
if numero % 2 ==0:
    print("el numero es par")
else:
    print("el numero es impar")

print(f"el numero es {numero}")


num1 = int(input("ingrese el primer numero"))
num2 = int(input("ingrese el segundo numero"))
resultado = num1 + num2 
print(resultado)  


lista = {"lavar ropa": False, 
        "tender cama": False,
        "trabajo UNAD":False
}

while True:
    print("opcciones")
    print("1. mostrar tareas")
    print("2. marcar tarea como completada")
    print("3. agregar una nueva tarea ")
    print("4. salir")
    
    opcion = input("elije una opccion (1-4):")
    
    if opcion == "1":
        print("lista de tareas")
        for tarea, estado in lista.items(): 
            print(f"{tarea}: {"completada"if estado else "pendiente"}")
    elif opcion == "2":
        tarea = input("ingrese el nombre de la tarea a completar:")
        
        if tarea in lista:
            lista [tarea]= True #marca la terea como completada 
            print(f"tarea '{tarea}' marcada como completada ")
        else:
            print("tarea no encontrada") #si la tarea no existe 
            
    elif opcion == "3":
        tarea = input("ingrese la nueva tarea:")
        lista[tarea]=False
        print(f"tarea"'{tarea}'"agregada con estado pendiente")
    elif opcion =="4":
        print("saliendo del programa...")
        break
        
    else:
        print("opcion invalida. intentalo de nuevo")