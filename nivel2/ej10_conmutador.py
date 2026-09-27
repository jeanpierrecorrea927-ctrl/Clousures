"""
Ejercicio 10: Interruptor Múltiple (Máquina de Estados Ligera)
Nivel 2 - Estado Encapsulado Avanzado (nonlocal + Lambdas)
"""


def crear_conmutador(lista_estados):
    """Alterna cíclicamente entre estados internos privados en cada llamada."""
    indice = -1

    def siguiente_estado():
        nonlocal indice
        indice = (indice + 1) % len(lista_estados)
        return lista_estados[indice]
    return siguiente_estado


if __name__ == "__main__":
    semaforo = crear_conmutador(["ROJO", "AMARILLO", "VERDE"])

    print("--- Ejercicio 10: Interruptor Múltiple ---")
    print([semaforo() for _ in range(6)])
