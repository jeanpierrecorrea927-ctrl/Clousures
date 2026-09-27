"""
Ejercicio 15: Decorador / HOF de Profiling y Auditoría
Nivel 3 - HOFs Complejas combinadas con Closures y Lambdas
"""

import time


def auditar_ejecucion(fn_objetivo, fn_logger):
    """Mide el tiempo de ejecución y envía el informe al closure/lambda
    de logging pasado por parámetro."""
    def ejecutar(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        fn_logger({
            "funcion": fn_objetivo.__name__,
            "duracion_seg": round(duracion, 6),
            "resultado": resultado,
        })
        return resultado
    return ejecutar


def tarea_pesada(n):
    return sum(i * i for i in range(n))


if __name__ == "__main__":
    logger_consola = lambda info: print(f"📊 AUDITORÍA -> {info}")
    tarea_auditada = auditar_ejecucion(tarea_pesada, logger_consola)

    print("--- Ejercicio 15: Auditoría de Ejecución ---")
    tarea_auditada(100000)
