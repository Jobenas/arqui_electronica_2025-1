    
def lee_num(msg: str) -> int:
    """
    Lee un numero desde el terminal.
    :returns: Un entero que representa el numero ingresado.
    """
    while True:
        try:
            num = input(msg)
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

    num_len = lee_num("Ingrese la cantidad de muestras a tomar: ")
    for _ in range(num_len):
        nums.append(lee_num("Ingrese un numero: "))

    promedio = sum(nums) / len(nums)

    print(promedio)
