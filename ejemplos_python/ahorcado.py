from random import randint
from typing import Union

palabras = ["arquitectura", "computadoras", "electronica", "python", "ahorcado", "universidad"]
palabra = palabras[randint(0, len(palabras) - 1)]
palabra_lista = ["_"] * len(palabra)
intentos = 5


def actualiza_score(p_lista: list[str], intentos: int) -> str:
    score = f"{' '.join(p_lista)} - Intentos: {intentos}"
    return score


def lee_letra() -> str:
    letra = ""

    while len(letra) != 1:
        letra = input("Por favor ingrese una letra: ")
        if len(letra) != 1:
            print("Valor ingresado incorrecto, intente nuevamente.")
    
    return letra


def busca_letra(p: str, l: str, p_lista: list[str]) -> Union[list[str], bool]: 
    """
    Busca la letra especificada dentro de la palabra para poder reemplazar el '_' en la posicion que la letra ocuparia. 
    Si hay mas de una occurrencia de la letra, se reemplaza en todas las occurrencias.
    :param p: string que contiene la palabra a analizar.
    :param l: string que contiene la letra que se buscara dentro de la palabra.
    :param p_lista: lista de strings que inicialmente tienen '_' y que seran reemplazadas con las letras en donde occuran.
    :return: p_lista actualizada con los valores y una bandera booleana indicando si hubo una ocurrencia o no.
    """
    letra_encontrada = False

    for idx in range(len(p)):
        if l == p[idx]:
            p_lista[idx] = l
            letra_encontrada = True

    return p_lista, letra_encontrada


if __name__ == '__main__': 
    while True:
        print(actualiza_score(palabra_lista, intentos))
        letra_input = lee_letra()
        palabra_lista, encontrada = busca_letra(palabra, letra_input, palabra_lista)

        if not encontrada:
            print("Letra ingresada no es parte de la palabra =(")
            intentos -= 1
        
        if intentos == 0:
            print(f"Lo siento perdio el juego =(")
            exit(0)

        if not "_" in palabra_lista:
            print(f"Felicitaciones, la palabra encontrada fue {palabra} =)")
            exit(0)
