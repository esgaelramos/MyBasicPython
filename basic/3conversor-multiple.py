menu = """ 
馃槮 Bienvenido al conversor de monedas a d貌lares 馃槮

1 - 馃嚚馃嚧 Pesos colombianos
2 - 馃嚘馃嚪 Pesos argentinos
3 - 馃嚥馃嚱 Pesos mexicanos

Elige una opci贸n: """

opcion = int(input(menu))

if opcion == 1:
    #Convertir Pesos Colombianos a D贸lares
    pesos = input("Ingrese cu谩ntos pesos colombianos tiene: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares.")
elif opcion == 2:
    #Convertir Pesos Argentinos a D贸lares
    pesos = input("Ingrese cu谩ntos pesos argentinos tiene: ")
    pesos = float(pesos)
    valor_dolar = 209
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " d贸lares americanos.")
elif opcion == 3:
    #Convertir Pesos Mexicanos a D贸lares
    pesos = input("Ingrese cu谩ntos pesos mexicanos tiene: ")
    pesos = float(pesos)
    valor_dolar = 21
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " d贸lares americanos.")
else:
    print("Ingresa una opci贸n v谩lida, por favor.")
    