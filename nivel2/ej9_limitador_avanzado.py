"""
Ejercicio 9: Limitador de Tasa Inteligente (Rate Limiter con Reset)
Nivel 2 - Estado Encapsulado Avanzado (nonlocal + Lambdas)
"""


def crear_limitador_avanzado(max_intentos, fn_alerta):
    """Cuenta ejecuciones privadas; ejecuta fn_alerta al superar el límite."""
    intentos = 0

    def ejecutar(accion):
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            return None
        return accion()

    def resetear():
        nonlocal intentos
        intentos = 0

    ejecutar.reset = resetear
    return ejecutar


if __name__ == "__main__":
    alerta = lambda n: print(f"⚠️  Límite excedido: intento número {n}")
    login_limitado = crear_limitador_avanzado(3, alerta)

    print("--- Ejercicio 9: Limitador de Tasa ---")
    for i in range(5):
        resultado = login_limitado(lambda: "login exitoso")
        print(f"Intento {i + 1}: {resultado}")
    login_limitado.reset()
    print("Después de reset:", login_limitado(lambda: "login exitoso"))
