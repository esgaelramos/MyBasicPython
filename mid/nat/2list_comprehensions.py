def run():
    # squares = []
    # #My answer, more complicated
    # for i in range(1, 101):
    #     number = i ** 2
    #     if number % 3 == 0:
    #         continue
    #     else:
    #         squares.append(number)
    # print("Solo imprimimos los resultados que al elevar no sean divisibles entre 3: ", squares)

    # #Answer teacher, better easy
    # #Every number to square, continues to be divisible at natural number
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    # print("Solo elevamos los numeros que no sean divisibles entre 3: ", squares)

    #En una linea súper fácil
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(squares)

    # #Crear una lista con todos los múltiplos de 4, que a su vez son múltiplos de 6 y de 9, hasta 5 dígitos:
    # list_multiple_four_six_nine = [i for i in range (1, 100000) if i % 36 == 0]
    # print(list_multiple_four_six_nine)

    #Crear una lista con todos los múltiplos de 5, que a su vez son múltiplos de 7 y de 8, hasta 4 dígitos:
    list_multiple_five_seven_eigth = [i for i in range (1, 10000) if i % 280 == 0]
    print(list_multiple_five_seven_eigth)

    # #Para descubrir los MCD o mcm //no sé cuáles:)
    # for i in range(1, 301):
    #     if i % 5 == 0 and i % 7 == 0 and i % 8 == 0:
    #         print(i)

if __name__ == "__main__":
    run()