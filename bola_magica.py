import random

FICHERO = "frases.txt"


def respuestas_desde(FICHERO: str):
    respuestas = []
    try:
        with open(FICHERO, 'r', encoding='utf-8') as fichero:
            for linea in fichero:
                respuestas.append(linea.strip())
    except FileNotFoundError:
        print(f"Error: el fichero «{FICHERO}» no existe.")
    except PermissionError:
        print(f"Error: permiso denegado al abrir «{FICHERO}».")
    except UnicodeDecodeError:
        print(f"Error: no se pudo decodificar «{FICHERO}» en UTF-8.")
    except IOError as e:
        print(f"Error de E/S al leer «{FICHERO}»: {e}")

    return respuestas


# @TODO leamos respuetas desde "frases.txt"
def main(respuestas: list):
    if not respuestas:
        print("No hay frases disponibles para elegir.")
        exit()
    print(random.choice(respuestas))

if __name__ == "__main__":
    main(respuestas_desde(FICHERO))
