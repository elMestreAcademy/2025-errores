def patata(n):
    for i in range(n):
        print("patata")


def accion_complicada(callback):
    patata = 3
    print("hazCositas")
    print("Y al acabar:")
    print("-------------")
    callback(patata)
    print("#############")


accion_complicada(patata)
