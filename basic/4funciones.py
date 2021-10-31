#Ejemplo inicial
# def imprimir_mensaje():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()

# #Ejemplo pero repetitivo
# opcion = int(input("Elige una opción (1, 2, 3): "))
# if opcion == 1:
#     print("Hola")
#     print("Cómo estás")
#     print("Elegiste la opción 1")
#     print("Bye!!!")
# elif opcion == 2:
#     print("Hola")
#     print("Cómo estás")
#     print("Elegiste la opción 2")
#     print("Bye!!!")
# elif opcion == 3:
#     print("Hola")
#     print("Cómo estás")
#     print("Elegiste la opción 3")
#     print("Bye!!!")    
# else:
#     print("Elige una opción válida")

# #Ejemplo con función definida
# def conversacion(mensaje):
#     print("Hola")
#     print("Cómo estás")
#     print(mensaje)
#     print("Bye!!!")

# opcion = int(input("Elige una opción (1, 2, 3): "))
# if opcion == 1:
#     conversacion("Elegiste la opción 1")
# elif opcion == 2:
#     conversacion("Elegiste la opción 2")
# elif opcion == 3:
#     conversacion("Elegiste la opción 3") 
# else:
#     print("Elige una opción válida")

#Devolver función
# def suma(a, b):
#     print("Se suman dos numeros")
#     resultado = a + b
#     return resultado

# sumatoria = suma(1, 4)
# print(sumatoria)

#Devolver función y sumar lo devuelto
def suma(a, b):
    print("Se suman dos numeros")
    resultado = a + b
    return resultado

sumatoria1 = suma(1, 4)
sumatoria2 = suma(2, 4)
sumatoria = sumatoria1 + sumatoria2
print(sumatoria)