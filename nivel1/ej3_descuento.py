"""
Ejercicio 3: Calculador de Descuentos con Regla Dinámica
Nivel 1 - Closures con Inyección de Comportamiento
"""


def crear_descuento_dinamico(regla_condicional_lambda, porcentaje_descuento=0.10):
    """Retorna un closure que aplica un descuento si la regla lambda se cumple."""
    def calcular(precio):
        if regla_condicional_lambda(precio):
            descuento = precio * porcentaje_descuento
            return round(precio - descuento, 2)
        return precio
    return calcular


if __name__ == "__main__":
    descuento_mayoristas = crear_descuento_dinamico(lambda p: p > 100, 0.15)
    descuento_liquidacion = crear_descuento_dinamico(lambda p: p <= 50, 0.05)

    print("--- Ejercicio 3: Calculador de Descuentos ---")
    print(f"Precio 150 (mayorista) -> {descuento_mayoristas(150)}")
    print(f"Precio 30 (liquidación) -> {descuento_liquidacion(30)}")
    print(f"Precio 30 (mayorista, no aplica) -> {descuento_mayoristas(30)}")
