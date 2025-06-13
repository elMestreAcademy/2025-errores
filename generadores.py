from random import randint, shuffle


def funcion():
    i = 0
    while True:
        i += 1
        return i


def generador():
    i = 0
    while True:
        i += 1
        yield i
        print("GENERADO CONTINUA")


def generadorDeAldeanos(nombres: list, apellidos: list) -> str:
    shuffle(nombres)
    shuffle(apellidos)
    while nombres and apellidos:
        yield f"{nombres.pop()} {apellidos.pop()}"

    yield "NO QUEDA NADIE EN LA ALDEA"


def demoBasica():
    gen = generador()

    for i in range(10):
        print(f"FUNCION:   {funcion()}")
        print(f"GENERADOR: {next(gen)}")


def demoAldea():
    contador = generador()
    aldea = generadorDeAldeanos(
        ["Paco", "Marta", "Lucia"],
        ["Ortíz", "Gonzalez", "Pescadero", "Pérez", "Castillos"]
    )

    while True:
        try:
            print(f"{next(contador)} - {next(aldea)}")
        except StopIteration:
            break


if __name__ == "__main__":
    demoBasica()
