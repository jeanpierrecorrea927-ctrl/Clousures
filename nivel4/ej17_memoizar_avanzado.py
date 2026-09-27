"""
Ejercicio 17: Caché con Expiración o Tamaño Máximo (Memoización Profesional)
Nivel 4 - Patrones Avanzados de Arquitectura Funcional
"""

from collections import OrderedDict


def memoizar_avanzado(fn_costosa, max_items):
    """Retorna un closure controlando el estado privado de una memoria
    caché con límite de capacidad (política FIFO/LRU simple)."""
    cache = OrderedDict()

    def envoltura(*args):
        if args in cache:
            cache.move_to_end(args)
            return cache[args]
        resultado = fn_costosa(*args)
        cache[args] = resultado
        if len(cache) > max_items:
            cache.popitem(last=False)
        return resultado

    envoltura.estado_cache = lambda: dict(cache)
    return envoltura


def calculo_costoso(n):
    print(f"   (calculando fibonacci({n})...)")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    fib_memo = memoizar_avanzado(calculo_costoso, max_items=2)

    print("--- Ejercicio 17: Memoización con Capacidad Máxima ---")
    print(fib_memo(10))
    print(fib_memo(20))
    print(fib_memo(10))  # desde caché
    print(fib_memo(30))  # provoca descarte del más antiguo (10)
    print(f"Estado de la caché: {fib_memo.estado_cache()}")
