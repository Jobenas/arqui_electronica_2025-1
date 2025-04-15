import socket

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola mundo!"
    msg_bytes = msg.encode("utf-8")

    sock.sendall(msg_bytes)
    bytes_recibidos = 0
    bytes_esperados = len(msg_bytes)

    full_msg = ""

    while bytes_recibidos < bytes_esperados:
        data = sock.recv(SOCK_BUFFER)
        print(f"Recibi parcial: {data}")
        bytes_recibidos += len(data)
        full_msg += data.decode("utf-8")

    sock.close()

    print(f"Recibi: {full_msg}")
