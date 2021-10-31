menu = """ 
😦 Bienvenido al conversor de monedas a dòlares 😦

1 - 🇨🇴 Pesos colombianos
2 - 🇦🇷 Pesos argentinos
3 - 🇲🇽 Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    #Convertir Pesos Colombianos a Dólares
    pesos = input("Ingrese cuántos pesos colombianos tiene: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")
elif opcion == 2:
    #Convertir Pesos Argentinos a Dólares
    pesos = input("Ingrese cuántos pesos argentinos tiene: ")
    pesos = float(pesos)
    valor_dolar = 209
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dólares americanos.")
elif opcion == 3:
    #Convertir Pesos Mexicanos a Dólares
    pesos = input("Ingrese cuántos pesos mexicanos tiene: ")
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dólares americanos.")
else:
    print("Ingresa una opción válida, por favor.")
    