from threading import Thread
import time

N = 100_000_000


def cuenta(n: int) -> None:
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    t1 = Thread(target=cuenta, args=(N // 2, ))
    t2 = Thread(target=cuenta, args=(N // 2, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):.6f} segundos")
