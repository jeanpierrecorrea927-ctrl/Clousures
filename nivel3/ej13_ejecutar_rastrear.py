"""
Ejercicio 13: Ejecutor Repetitivo con Estado Accesible
Nivel 3 - HOFs Complejas combinadas con Closures y Lambdas
"""


def ejecutar_y_rastrear(fn_tarea, n):
    """Ejecuta fn_tarea N veces y retorna un closure con el historial
    de resultados obtenidos."""
    historial = []
    for i in range(n):
        historial.append(fn_tarea(i))

    def acceder_historial():
        return list(historial)
    return acceder_historial


if __name__ == "__main__":
    obtener_historial = ejecutar_y_rastrear(lambda i: i ** 2, 5)

    print("--- Ejercicio 13: Ejecutor Repetitivo con Historial ---")
    print(f"Historial de ejecuciones: {obtener_historial()}")
