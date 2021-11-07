#Diccionarios
mi_diccionario = {
    "llave1": 1,
    "llave2": 2,
    "llave3": 3
}
# print(mi_diccionario)
# print(mi_diccionario["llave1"])
# print(mi_diccionario["llave2"])
# print(mi_diccionario["llave3"])

poblacion_paises = {
    "Argentina" : 44000000,
    "Brasil" : 210000000,
    "Colombia" : 50000000
}
# print(poblacion_paises["Argentina"])

#Recorrer el diccionarios
for pais in poblacion_paises.keys():
    print(pais)

for pais in poblacion_paises.values():
    print(pais)

for pais in poblacion_paises.items():
    print(pais)

for pais, poblacion in poblacion_paises.items():
    print(pais + " tiene " + str(poblacion) + " de habitantes.")