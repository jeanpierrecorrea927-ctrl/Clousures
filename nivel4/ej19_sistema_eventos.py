"""
Ejercicio 19: Sistema Pub/Sub (Event Listener con HOFs y Closures)
Nivel 4 - Patrones Avanzados de Arquitectura Funcional
"""


def crear_sistema_eventos():
    """Retorna un closure gestor capaz de registrar suscriptores (lambdas)
    y emitir eventos notificando a cada uno."""
    suscriptores = {}

    def gestor(accion, *args):
        if accion == "suscribir":
            evento, callback = args
            suscriptores.setdefault(evento, []).append(callback)
        elif accion == "emitir":
            evento, payload = args
            for callback in suscriptores.get(evento, []):
                callback(payload)
        elif accion == "listar":
            return {k: len(v) for k, v in suscriptores.items()}
    return gestor


if __name__ == "__main__":
    eventos = crear_sistema_eventos()
    eventos("suscribir", "pedido_creado", lambda p: print(f"📧 Enviando email por pedido: {p}"))
    eventos("suscribir", "pedido_creado", lambda p: print(f"📦 Actualizando inventario por: {p}"))

    print("--- Ejercicio 19: Sistema Pub/Sub ---")
    eventos("emitir", "pedido_creado", "Pedido #1024")
    print(f"Suscriptores registrados: {eventos('listar')}")
