import random
import sys

FICHERO = "frases.txt"


def respuestas_desde(ruta: str) -> list:
    respuestas = []
    try:
        with open(ruta, 'r', encoding='utf-8') as fichero:
            for linea in fichero:
                respuestas.append(linea.strip())
    except FileNotFoundError:
        print(f"Error: el fichero «{ruta}» no existe.", file=sys.stderr)
    except PermissionError:
        print(f"Error: permiso denegado al abrir «{ruta}».", file=sys.stderr)
    except UnicodeDecodeError:
        print(f"Error: no se pudo decodificar «{ruta}» en UTF-8.", file=sys.stderr)
    except IOError as e:
        print(f"Error de E/S al leer «{ruta}»: {e}", file=sys.stderr)

    return respuestas


# @TODO leamos respuetas desde "frases.txt"
def main(respuestas: list):
    if not respuestas:
        print("No hay frases disponibles para elegir.", file=sys.stderr)
        sys.exit(1)
    print(random.choice(respuestas))

if __name__ == "__main__":
    main(respuestas_desde(FICHERO))
