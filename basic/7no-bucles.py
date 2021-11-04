# #RECURSIVDAD PARA POTENCIAS DE 2
# def run(num, rept):
#     if num <= rept:
#         print(str(2 ** num))
#         run(num + 1, rept)
#     else:
#         print("¡Fin!")

# if __name__ == "__main__":
#     repeticiones = int(input("Cuantas potencias de 2 quieres: "))
#     run(0, repeticiones)

#RECURSIVDAD PARA POTENCIAS DE CUALQUIER NUMERO
def run(base, num, rept):
    if num <= rept:
        print(str(base ** num))
        run(base, num + 1, rept)
    else:
        print("¡Fin!")

if __name__ == "__main__":
    base = int(input("Cuál base quieres:"))
    repeticiones = int(input("Cuantas potencias de " + str(base) + " quieres:"))
    run(base, 0, repeticiones)    