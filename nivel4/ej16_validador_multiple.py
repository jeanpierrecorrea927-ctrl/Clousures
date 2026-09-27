"""
Ejercicio 16: Validador Compuesto de Reglas de Negocio
Nivel 4 - Patrones Avanzados de Arquitectura Funcional
"""


def crear_validador_multiple(*lambdas_criterios):
    """Retorna un closure que evalúa si un objeto cumple todas
    las reglas pasadas como argumento."""
    def validar(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validar


if __name__ == "__main__":
    validar_usuario = crear_validador_multiple(
        lambda u: len(u.get("password", "")) >= 8,
        lambda u: "@" in u.get("email", ""),
        lambda u: u.get("edad", 0) >= 18,
    )

    usuario_ok = {"password": "seguro123", "email": "a@b.com", "edad": 25}
    usuario_mal = {"password": "123", "email": "invalido", "edad": 16}

    print("--- Ejercicio 16: Validador Compuesto ---")
    print(f"usuario_ok válido: {validar_usuario(usuario_ok)}")
    print(f"usuario_mal válido: {validar_usuario(usuario_mal)}")
