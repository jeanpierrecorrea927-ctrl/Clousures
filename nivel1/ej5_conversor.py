"""
Ejercicio 5: Conversor de Divisas con Margen
Nivel 1 - Closures con Inyección de Comportamiento
"""


def crear_conversor(tasa, margen_lambda):
    """Retorna una función para convertir montos calculando dinámicamente
    la comisión adicional mediante margen_lambda(monto_convertido)."""
    def convertir(monto):
        convertido = monto * tasa
        comision = margen_lambda(convertido)
        return round(convertido + comision, 2)
    return convertir


if __name__ == "__main__":
    usd_a_eur = crear_conversor(0.92, lambda monto: monto * 0.02)
    usd_a_gbp = crear_conversor(0.78, lambda monto: 3.5 if monto < 100 else monto * 0.01)

    print("--- Ejercicio 5: Conversor de Divisas ---")
    print(f"100 USD -> EUR: {usd_a_eur(100)}")
    print(f"50 USD -> GBP: {usd_a_gbp(50)}")
    print(f"500 USD -> GBP: {usd_a_gbp(500)}")
