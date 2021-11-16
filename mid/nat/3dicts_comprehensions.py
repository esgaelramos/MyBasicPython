def run():
    #Llaves = numeros naturales (100), y Values = elevados al cubo
    cubes = {}
    # for i in range(1, 101):
    #     cubes[i] = i**3
    # print(cubes)

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         cubes[i] = i**3
    # print(cubes)

    # cubes = {i: i**3 for i in range(1, 101)}
    # print(cubes)

    # cubes = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(cubes)

    # #Sin redondear
    # square_root = {i: i**(1/2) for i in range(1,101)}
    # print(square_root)

    #Redondeado a dos décimales
    square_root = {i: round(i**(1/2),2) for i in range(1,101)}
    print(square_root)

if __name__ == "__main__":
    run()