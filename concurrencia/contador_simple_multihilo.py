from threading import Thread
import time


def cuenta():
    print("Uno")
    time.sleep(1)
    print("Dos")


def main():
    t1 = Thread(target=cuenta)
    t2 = Thread(target=cuenta)
    t3 = Thread(target=cuenta)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion multi hilo: {t_ejecucion:.6f} segundos")
