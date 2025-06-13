monstruos = 3
exp = 0


def experiencia(accion):
    def aaa():
        global exp
        resultado = accion()
        exp += 1

        return resultado
    return aaa


@experiencia
def matar():
    global monstruos
    monstruos -= 1


@experiencia
def curar():
    print("Has curado la party")


print(f"quedan {monstruos} monstruos")
matar()
matar()
curar()
print(f"quedan {monstruos} monstruos")
print(f"EXPERICIA: {exp}")
