

if __name__ == '__main__':
    with open("notas.csv", "r") as f:
        contenido = f.read()

    datos = contenido.split("\n")[1:]

    notas_finales = list()
    for dato in datos:
        valores = [int(val) for val in dato.split(",")]
        notas_labs = valores[1:13]
        e1 = valores[13]
        e2 = valores[14]

        lab = sum(notas_labs) / len(notas_labs)

        nota_final = ((5 * lab) + (2.5 * e1) + (2.5 * e2)) / 10
        notas_finales.append(nota_final)

    print(notas_finales)

