import asyncio
from random import randint

SOCK_BUFFER = 1024

def busca_notas(codigo: str) -> list[int]:
    """
    Busca las notas correspondientes al codigo de alumno suministrado
    :param codigo: string que contiene el codigo del alumno
    :returns: lista de enteros con las notas correspondientes al codigo
    """
    with open("notas.csv", "r") as f:
        contenido = f.read()
    
    contenido = contenido.split("\n")

    notas = list()
    for fila in contenido:
        if codigo in fila:
            notas = [int(valor) for valor in fila.split(",")[1:]]
            break
    return notas


def calc_nota_final(notas: list[int]) -> float:
    """
    Calcula la nota final en base a una lista de notas especificas.
    :param notas: Lista de notas que el cliente envia.
    :returns: float con el valor de la nota final.
    """
    notas_labs = notas[0:12]
    e1 = notas[12]
    e2 = notas[13]

    lab = sum(notas_labs) / len(notas_labs)

    nota_final = ((5 * lab) + (2.5 * e1) + (2.5 * e2)) / 10

    return nota_final


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("cliente conectado")

    try:
        while True:
            data = await reader.read(SOCK_BUFFER)
            await asyncio.sleep(randint(3, 7))
            if data:
                codigo = data.decode("utf-8")
                valores = busca_notas(codigo)
                if len(valores) > 0:
                    nota_final = calc_nota_final(valores)
                else:
                    nota_final = -1

                writer.write(str(nota_final).encode("utf-8"))
                await writer.drain()
            else:
                print("No hay mas datos")
                break
    except ConnectionResetError:
        print("El cliente cerro la conexion de manera abrupta")
    finally:
        writer.close()
        await writer.wait_closed()
    
    print("conexion cerrada")


async def main():
    server_address = ("0.0.0.0", 5000)

    server = await asyncio.start_server(handle_client, server_address[0], server_address[1])

    async with server:
        print(f"Iniciando el servidor en {server_address[0]}:{server_address[1]}")
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
