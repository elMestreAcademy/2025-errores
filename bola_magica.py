import random

FICHERO = "frases.txt"


def respuestas_desde(FICHERO: str):
    respuestas = []
    with open(FICHERO, 'r', encoding='utf-8') as fichero:
        for linea in fichero:
            respuestas.append(linea.strip())

    return respuestas


# @TODO leamos respuetas desde "frases.txt"
def main(respuestas: list):
    print(random.choice(respuestas))

if __name__ == "__main__":
    main(respuestas_desde(FICHERO))
