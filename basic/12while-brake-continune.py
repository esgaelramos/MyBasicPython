def run():
    contador = 0
    while contador < 24:
        contador += 1
        print("El contador sube a: " + str(contador) + " cuidado al hacerlo.")
        if contador == 21:
            break

if __name__== "__main__":
    run()