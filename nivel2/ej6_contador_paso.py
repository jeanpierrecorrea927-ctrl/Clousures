"""
Ejercicio 6: Contador Ponderado
Nivel 2 - Estado Encapsulado Avanzado (nonlocal + Lambdas)
"""


def crear_contador_paso(fn_paso):
    """Incrementa el estado interno usando fn_paso(cuenta_actual)."""
    cuenta = 0

    def siguiente():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return siguiente


if __name__ == "__main__":
    contador_par = crear_contador_paso(lambda c: c + 2)
    contador_exponencial = crear_contador_paso(lambda c: (c or 1) * 2)

    print("--- Ejercicio 6: Contador Ponderado ---")
    print([contador_par() for _ in range(5)])
    print([contador_exponencial() for _ in range(5)])
