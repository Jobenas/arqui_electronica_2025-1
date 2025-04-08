import time


if __name__ == "__main__":
    inicio = time.perf_counter()
    notas_nombres = [f"lab {idx + 1}" for idx in range(12)]
    notas_nombres.append("examen 1")
    notas_nombres.append("examen 2")
    notas = list()

    for nombre in notas_nombres:
        nota = input(f"Por favor ingrese la nota de {nombre}: ")
        nota = int(nota)
        notas.append(nota)

    print(f"Notas: {notas}")

    inicio_cpu = time.perf_counter()
    notas_labs = notas[:12]
    e1 = notas[12]
    e2 = notas[13]

    lab = sum(notas_labs) / len(notas_labs)

    nota_final = ((5 * lab) + (2.5 * e1) + (2.5 * e2)) / 10
    fin = time.perf_counter()

    print(f"Nota final: {nota_final}")

    t_ejecucion = fin - inicio
    t_cpu = fin - inicio_cpu
    print(f"Tiempo de ejecucion de cpu: {t_cpu:.5f} segundos - Tiempo de ejecucion total: {t_ejecucion:.5f} segundos")