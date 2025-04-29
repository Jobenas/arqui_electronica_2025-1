import asyncio

SOCK_BUFFER = 1024


async def nota_client(codigo: str) -> float:
    """
    Envia una solicitud de codigo de alumno al servidor de manera asincrona y recibe una respuesta de la nota final.
    :param codigo: str representando el codigo de alumno
    :returns: Nota final representada como float
    """
    reader, writer = await asyncio.open_connection('127.0.0.1', 5000)

    print(f'Send: {codigo!r}')
    writer.write(codigo.encode("utf-8"))
    await writer.drain()

    data = await reader.read(SOCK_BUFFER)
    print(f'Received: {data.decode("utf-8")!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

    return float(data.decode("utf-8"))


if __name__ == '__main__':
    nota = asyncio.run(nota_client('20250002'))

    print(nota)