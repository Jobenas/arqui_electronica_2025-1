import time
from concurrent.futures import ThreadPoolExecutor


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def actualiza(self, nombre: str) -> None:
        print(f"[Thread {nombre}] Empezando actualizacion")
        copia_local = self.value
        copia_local += 1
        time.sleep(0.1)
        self.value = copia_local
        print(f"[Thread {nombre}] Terminando actualizacion")


if __name__ == '__main__':
    db = FakeDatabase()

    print(f"[Main] Valor inicial de la base de datos: {db.value}")

    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(5):
            executor.submit(db.actualiza, f"t{i}")

    print(f"[Main] Valor final de la base de datos:{db.value}")
