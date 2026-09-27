"""
Ejercicio 2: Multiplicador Paramétrico con Mapeo
Nivel 1 - Closures con Inyección de Comportamiento
"""


def crear_operador(factor, operacion_lambda):
    """Retorna un closure capaz de aplicar operacion_lambda(valor, factor)."""
    def operar(valor):
        return operacion_lambda(valor, factor)
    return operar


if __name__ == "__main__":
    triplicar = crear_operador(3, lambda v, f: v * f)
    potenciar = crear_operador(2, lambda v, f: v ** f)

    print("--- Ejercicio 2: Multiplicador Paramétrico ---")
    print(f"triplicar(7) = {triplicar(7)}")
    print(f"potenciar(5) = {potenciar(5)}")
    print(f"map con triplicar: {list(map(triplicar, [1, 2, 3, 4]))}")
