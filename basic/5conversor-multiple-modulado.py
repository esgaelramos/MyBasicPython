def conversor(tipo_pesos, valor_dolar):
    pesos = input("Ingrese cu谩ntos pesos " + tipo_pesos + " tiene: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares.")

menu = """ 
馃槮 Bienvenido al conversor de monedas a d貌lares 馃槮

1 - 馃嚚馃嚧 Pesos colombianos
2 - 馃嚘馃嚪 Pesos argentinos
3 - 馃嚥馃嚱 Pesos mexicanos

Elige una opci贸n: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
    #Convertir Pesos Colombianos a D贸lares
elif opcion == 2:
    conversor("argentinos", 209)
    #Convertir Pesos Argentinos a D贸lares
elif opcion == 3:
    conversor("mexicanos", 21)
    #Convertir Pesos Mexicanos a D贸lares
else:
    print("Ingresa una opci贸n v谩lida, por favor.")
    