# a = range(1000)
# print(a)

# a = list(range(1000))
# print(a)

# for contador in range(1, 1001):
#     print(contador)

# for i in range(10):
#     print(11 * i)

#Tablas de multiplicar

def tabla(base):
    for i in range(11):
        print(str(base) + " por " + str(i) + " es igual a: " + str(base * i))

def tablas():
    for i in range(1,11):
        print("La tabla del " + str(i) + " es: ")
        tabla(i)

if __name__ == "__main__":
    tablas()