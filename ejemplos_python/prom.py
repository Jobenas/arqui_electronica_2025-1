    
def lee_num(msg: str) -> int | None:
    """
    Lee un numero desde el terminal.
    :returns: Un entero que representa el numero ingresado.
    """
    while True:
        try:
            num = input(msg)
            if num.lower() == 'q':
                return None
            num = int(num)
            break
        except ValueError:
            print("No ingreso un numero valido. Intente de nuevo.")
        except KeyboardInterrupt:
            print("\nEl usuario ha cerrado el programa")
            exit(0)

    return num


if __name__ == '__main__':
    nums = list()

    idx = 0
    while True:
        numero = lee_num(f"Ingrese un numero para la muestra {idx + 1} u oprima tecla 'q' para terminar: ")
        if numero is None:
            break
        nums.append(numero)
        idx += 1

    promedio = sum(nums) / len(nums)

    print(f"El promedio de {idx} muestras es: {promedio}")
