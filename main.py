"""
main.py
Ejecuta, en orden, los 20 ejercicios del taller (cada uno vive en su propio
archivo dentro de nivel1/ .. nivel4/). Útil para generar de un solo vistazo
toda la evidencia de ejecución con print().

Uso:
    python main.py
"""

import runpy
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EJERCICIOS = [
    ("NIVEL 1: Closures con Inyección de Comportamiento", [
        "nivel1/ej1_formateador.py",
        "nivel1/ej2_operador.py",
        "nivel1/ej3_descuento.py",
        "nivel1/ej4_sufijos.py",
        "nivel1/ej5_conversor.py",
    ]),
    ("NIVEL 2: Estado Encapsulado Avanzado", [
        "nivel2/ej6_contador_paso.py",
        "nivel2/ej7_acumulador_validado.py",
        "nivel2/ej8_promediador_filtrado.py",
        "nivel2/ej9_limitador_avanzado.py",
        "nivel2/ej10_conmutador.py",
    ]),
    ("NIVEL 3: HOFs Complejas Combinadas", [
        "nivel3/ej11_procesar_coleccion.py",
        "nivel3/ej12_agrupar_por.py",
        "nivel3/ej13_ejecutar_rastrear.py",
        "nivel3/ej14_componer_dos.py",
        "nivel3/ej15_auditar_ejecucion.py",
    ]),
    ("NIVEL 4: Patrones Avanzados de Arquitectura Funcional", [
        "nivel4/ej16_validador_multiple.py",
        "nivel4/ej17_memoizar_avanzado.py",
        "nivel4/ej18_pipeline.py",
        "nivel4/ej19_sistema_eventos.py",
        "nivel4/ej20_consultor.py",
    ]),
]

if __name__ == "__main__":
    for titulo_nivel, archivos in EJERCICIOS:
        print("\n" + "=" * 70)
        print(titulo_nivel)
        print("=" * 70)
        for ruta_relativa in archivos:
            runpy.run_path(os.path.join(BASE_DIR, ruta_relativa), run_name="__main__")
            print()

    print("=" * 70)
    print("FIN DEL TALLER - Todos los ejercicios ejecutados correctamente ✅")
    print("=" * 70)
