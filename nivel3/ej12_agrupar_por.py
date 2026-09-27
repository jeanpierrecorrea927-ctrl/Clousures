"""
Ejercicio 12: Reductor / Agrupador Personalizado
Nivel 3 - HOFs Complejas combinadas con Closures y Lambdas
"""


def agrupar_por(lista, fn_clave):
    """Agrupa una lista de diccionarios en un dict clave-valor
    basándose en el resultado de la lambda fn_clave."""
    grupos = {}
    for item in lista:
        clave = fn_clave(item)
        grupos.setdefault(clave, []).append(item)
    return grupos


if __name__ == "__main__":
    empleados = [
        {"nombre": "Ana", "depto": "Ventas"},
        {"nombre": "Luis", "depto": "TI"},
        {"nombre": "Carla", "depto": "Ventas"},
        {"nombre": "Beto", "depto": "TI"},
    ]
    resultado = agrupar_por(empleados, lambda e: e["depto"])

    print("--- Ejercicio 12: Agrupador Personalizado ---")
    for depto, personas in resultado.items():
        print(f"{depto}: {[p['nombre'] for p in personas]}")
