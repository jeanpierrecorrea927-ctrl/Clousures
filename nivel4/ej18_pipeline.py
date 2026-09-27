"""
Ejercicio 18: Motor de Pipeline Secuencial (Currying / Middleware)
Nivel 4 - Patrones Avanzados de Arquitectura Funcional
"""


def crear_pipeline(*funciones_transformacion):
    """Permite pasar un dato inicial y hacerlo fluir en orden a través
    de todas las lambdas/funciones del pipeline."""
    def ejecutar_pipeline(dato_inicial):
        resultado = dato_inicial
        for fn in funciones_transformacion:
            resultado = fn(resultado)
        return resultado
    return ejecutar_pipeline


if __name__ == "__main__":
    pipeline_texto = crear_pipeline(
        lambda s: s.strip(),
        lambda s: s.lower(),
        lambda s: s.replace(" ", "_"),
    )

    print("--- Ejercicio 18: Pipeline Secuencial ---")
    print(pipeline_texto("   Programación FUNCIONAL en Python   "))
