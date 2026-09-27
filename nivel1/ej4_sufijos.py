"""
Ejercicio 4: Generador de Seriales / Nombres Únicos
Nivel 1 - Closures con Inyección de Comportamiento
"""


def crear_generador_sufijos(patron_lambda):
    """Retorna un closure que renombra archivos usando un contador privado
    y una lambda de formato patron_lambda(nombre, contador)."""
    contador = 0

    def generar(nombre_archivo):
        nonlocal contador
        contador += 1
        return patron_lambda(nombre_archivo, contador)
    return generar


if __name__ == "__main__":
    renombrar_backup = crear_generador_sufijos(lambda n, c: f"{n}_backup_{c:03d}")

    print("--- Ejercicio 4: Generador de Seriales ---")
    print(renombrar_backup("reporte.docx"))
    print(renombrar_backup("reporte.docx"))
    print(renombrar_backup("reporte.docx"))
