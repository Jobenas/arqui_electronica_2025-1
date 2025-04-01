    
def lee_num() -> int:
    """
    Lee un numero desde el terminal.
    :returns: Un entero que representa el numero ingresado.
    """
    while True:
        num = input("Ingrese un numero: ")
        try:
            num = int(num)
            break
        except ValueError:
            print("No ingreso un numero valido. Intente de nuevo.")

    return num


if __name__ == '__main__':
    nums = list()
    print(nums)
    for _ in range(4):
        nums.append(lee_num())

    acumulado = 0

    for i in range(4):
        acumulado += nums[i]

    acumulado /= 4

    print(acumulado)