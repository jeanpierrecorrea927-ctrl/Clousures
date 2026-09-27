"""
Ejercicio 20: Mini-Query Engine sobre Listas de Objetos
Nivel 4 - Patrones Avanzados de Arquitectura Funcional
"""


def crear_consultor(campo):
    """Retorna una HOF para generar filtros dinámicos sobre listas de
    diccionarios/objetos mediante expresiones lambda complejas."""
    def generar_filtro(condicion_lambda):
        def filtrar(lista_objetos):
            return [obj for obj in lista_objetos if condicion_lambda(obj.get(campo))]
        return filtrar
    return generar_filtro


if __name__ == "__main__":
    productos = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 60},
        {"nombre": "Monitor", "precio": 300},
    ]

    consultar_por_precio = crear_consultor("precio")
    filtro_caros = consultar_por_precio(lambda precio: precio > 100)
    filtro_baratos = consultar_por_precio(lambda precio: precio <= 100)

    print("--- Ejercicio 20: Mini-Query Engine ---")
    print(f"Productos caros (>100): {[p['nombre'] for p in filtro_caros(productos)]}")
    print(f"Productos baratos (<=100): {[p['nombre'] for p in filtro_baratos(productos)]}")
