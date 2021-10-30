#Convertir Pesos Colombianos a Dólares | Ejercicio Guiado
pesos = input("Ingrese cuántos pesos colombianos tiene: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dólares.")


#Convertir Pesos Mexicanos a Dólares | Ejercicio
pesos = input("Ingrese cuántos pesos mexicanos tiene: ")
pesos = float(pesos)
valor_dolar = 21
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Usted tiene $" + dolares + " dólares americanos.")


#Convertir Dólares a Pesos Mexicanos| Ejercicio 
dolares = input("Ingrese cuántos dólares americanos tiene: ")
dolares = float(dolares)
valor_peso_mex = 21
pesos = dolares * valor_peso_mex
pesos = round(pesos, 2)
pesos = str(pesos)
print("Usted tiene $" + pesos + " pesos mexicanos, ¡millonario!")