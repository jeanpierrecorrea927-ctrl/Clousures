"""
Ejercicio 14: Compositor de Cadenas de Operaciones
Nivel 3 - HOFs Complejas combinadas con Closures y Lambdas
"""


def componer_dos(f, g):
    """Retorna un closure que aplica f(g(x))."""
    def compuesta(x):
        return f(g(x))
    return compuesta


if __name__ == "__main__":
    doble_mas_uno = componer_dos(lambda x: x + 1, lambda x: x * 2)
    mayus_recortado = componer_dos(lambda s: s.upper(), lambda s: s.strip())

    print("--- Ejercicio 14: Compositor de Cadenas ---")
    print(f"doble_mas_uno(5) = {doble_mas_uno(5)}")
    print(f"mayus_recortado('  hola  ') = '{mayus_recortado('  hola  ')}'")
