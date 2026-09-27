"""
Ejercicio 8: Promediador con Eliminación de Valores Extremos
Nivel 2 - Estado Encapsulado Avanzado (nonlocal + Lambdas)
"""


def crear_promediador_filtrado(filtro_ruido_lambda):
    """Acumula datos privadamente descartando valores atípicos
    (filtro_ruido_lambda(valor, datos_actuales) -> True si es válido)."""
    datos = []

    def procesar(valor):
        if filtro_ruido_lambda(valor, datos):
            datos.append(valor)
        return round(sum(datos) / len(datos), 2) if datos else 0
    return procesar


if __name__ == "__main__":
    # Descarta valores que se alejen más del 50% del promedio actual
    promedio_robusto = crear_promediador_filtrado(
        lambda v, datos: True if not datos
        else abs(v - sum(datos) / len(datos)) <= 0.5 * (sum(datos) / len(datos))
    )

    print("--- Ejercicio 8: Promediador con Filtro de Atípicos ---")
    for lectura in [10, 11, 9, 100, 10]:  # 100 es un outlier
        print(f"Lectura {lectura} -> promedio actual = {promedio_robusto(lectura)}")
