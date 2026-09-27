"""
Ejercicio 11: Pipeline de Mapeo y Filtrado Combinado
Nivel 3 - HOFs Complejas combinadas con Closures y Lambdas
"""


def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    """Combina internamente filter y map pasando expresiones lambda."""
    return list(map(fn_transformacion, filter(fn_predicado, lista)))


if __name__ == "__main__":
    numeros = list(range(1, 11))
    resultado = procesar_coleccion(numeros, lambda n: n % 2 == 0, lambda n: n ** 2)

    print("--- Ejercicio 11: Pipeline Mapeo + Filtrado ---")
    print(f"Pares al cuadrado de {numeros}: {resultado}")
