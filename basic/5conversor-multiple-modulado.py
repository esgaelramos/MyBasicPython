def conversor(tipo_pesos, valor_dolar):
    pesos = input("Ingrese cuántos pesos " + tipo_pesos + " tiene: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares.")

menu = """ 
😦 Bienvenido al conversor de monedas a dòlares 😦

1 - 🇨🇴 Pesos colombianos
2 - 🇦🇷 Pesos argentinos
3 - 🇲🇽 Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3875)
    #Convertir Pesos Colombianos a Dólares
elif opcion == 2:
    conversor("argentinos", 209)
    #Convertir Pesos Argentinos a Dólares
elif opcion == 3:
    conversor("mexicanos", 21)
    #Convertir Pesos Mexicanos a Dólares
else:
    print("Ingresa una opción válida, por favor.")
    