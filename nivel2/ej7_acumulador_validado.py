"""
Ejercicio 7: Acumulador con Filtro de Aceptación
Nivel 2 - Estado Encapsulado Avanzado (nonlocal + Lambdas)
"""


def crear_acumulador_validado(criterio_lambda):
    """Mantiene un total privado, solo suma valores que pasen criterio_lambda."""
    total = 0
    rechazados = []

    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        else:
            rechazados.append(valor)
        return total
    acumular.rechazados = lambda: rechazados
    return acumular


if __name__ == "__main__":
    acumular_positivos = crear_acumulador_validado(lambda v: v > 0)

    print("--- Ejercicio 7: Acumulador con Filtro ---")
    for v in [10, -5, 20, -1, 7]:
        print(f"Ingresando {v} -> total = {acumular_positivos(v)}")
    print(f"Valores rechazados: {acumular_positivos.rechazados()}")
