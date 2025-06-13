from random import randint


def funcion():
    i = 0
    while(True):
        i += 1
        return i


def generador():
    i = 0
    while(True):
        i += 1
        yield i


gen = generador()

for i in range(10):
    print(f"FUNCION:   {funcion()}")
    print(f"GENERADOR: {next(gen)}")
