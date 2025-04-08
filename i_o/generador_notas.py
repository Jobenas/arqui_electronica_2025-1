from random import randint
import time


if __name__ == "__main__":
    inicio = time.perf_counter()
    contenido = ""

    encabezado = f"codigo,{','.join([f"lab_{idx + 1}" for idx in range(12)])},examen1,examen2\n"
    contenido += encabezado

    codigo_inicial = 20250001

    # for i in range(200):
    #     linea = f"{codigo_inicial + i},{','.join([str(randint(0,20)) for _ in range(14)])}\n"
    #     contenido += linea

    lineas = f"{'\n'.join(
        [f"{codigo_inicial + i},{','.join([str(randint(0,20)) for _ in range(14)])}" for i in range(200)]
    )}"
    contenido += lineas

    inicio_archivo = time.perf_counter()
    with open("notas.csv", "w+") as f:
        f.write(contenido)

    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    t_archivo = fin - inicio_archivo

    print(f"Tiempo de escribir en archivo: {t_archivo:.5f} segundos - Tiempode total de ejecucion: {t_ejecucion:.5f} segundos.")
