import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Ingresa un numero del 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Ingrese un número más grande!")
        else:
            print("Ingrese un número más chico!")
        numero_elegido = int(input("Elige otro número: "))
    print("¡Ganaste! El número era: " + str(numero_elegido))

if __name__ == "__main__":
    run()