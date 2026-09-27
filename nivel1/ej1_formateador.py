"""
Ejercicio 1: Generador de Formateadores con Transformación
Nivel 1 - Closures con Inyección de Comportamiento
"""


def crear_formateador(prefijo, fn_transformacion):
    """Retorna un closure que transforma un texto y le antepone un prefijo."""
    def formatear(texto):
        texto_transformado = fn_transformacion(texto)
        return f"{prefijo}{texto_transformado}"
    return formatear


if __name__ == "__main__":
    fmt_mayus = crear_formateador("[LOG] ", lambda t: t.upper())
    fmt_invertido = crear_formateador(">> ", lambda t: t[::-1])

    print("--- Ejercicio 1: Generador de Formateadores ---")
    print(fmt_mayus("sistema iniciado correctamente"))
    print(fmt_invertido("closures"))
