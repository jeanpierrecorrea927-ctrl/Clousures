# 🧪 Taller Práctico: Programación Funcional en Python

Diseño de Arquitecturas Funcionales: HOFs, Closures Avanzados y Composición con Lambdas.

## 📁 Estructura del repositorio

```
.
├── nivel1/
│   ├── ej1_formateador.py          # Generador de formateadores con transformación
│   ├── ej2_operador.py             # Multiplicador paramétrico con mapeo
│   ├── ej3_descuento.py            # Calculador de descuentos con regla dinámica
│   ├── ej4_sufijos.py              # Generador de seriales / nombres únicos
│   └── ej5_conversor.py            # Conversor de divisas con margen
├── nivel2/
│   ├── ej6_contador_paso.py        # Contador ponderado
│   ├── ej7_acumulador_validado.py  # Acumulador con filtro de aceptación
│   ├── ej8_promediador_filtrado.py # Promediador con eliminación de atípicos
│   ├── ej9_limitador_avanzado.py   # Rate limiter con reset
│   └── ej10_conmutador.py          # Interruptor múltiple / máquina de estados
├── nivel3/
│   ├── ej11_procesar_coleccion.py  # Pipeline de mapeo y filtrado combinado
│   ├── ej12_agrupar_por.py         # Reductor / agrupador personalizado
│   ├── ej13_ejecutar_rastrear.py   # Ejecutor repetitivo con historial
│   ├── ej14_componer_dos.py        # Compositor de cadenas f(g(x))
│   └── ej15_auditar_ejecucion.py   # HOF de profiling y auditoría
├── nivel4/
│   ├── ej16_validador_multiple.py  # Validador compuesto de reglas de negocio
│   ├── ej17_memoizar_avanzado.py   # Memoización con límite de capacidad
│   ├── ej18_pipeline.py            # Motor de pipeline secuencial
│   ├── ej19_sistema_eventos.py     # Sistema Pub/Sub
│   └── ej20_consultor.py           # Mini-Query Engine sobre listas de objetos
├── main.py                          # Ejecuta los 20 ejercicios en orden (opcional)
└── README.md
```

Cada archivo de ejercicio es **autocontenido**: define su(s) función(es) y, bajo
`if __name__ == "__main__":`, incluye las pruebas con `print()` que verifican su
comportamiento. Esto permite ejecutar y calificar cada ejercicio por separado.

## ▶️ Cómo ejecutar

Requiere Python 3.8+ (solo usa librerías estándar: `time`, `collections`, `runpy`).

```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre-del-repositorio>
```

**Ejecutar un ejercicio individual:**
```bash
python nivel1/ej1_formateador.py
python nivel4/ej17_memoizar_avanzado.py
```

**Ejecutar todo el taller de una vez** (los 20 ejercicios, en orden):
```bash
python main.py
```

## 📌 Índice de ejercicios por nivel

| Nivel | Tema | Archivos |
|-------|------|----------|
| 🟢 Nivel 1 | Closures con inyección de comportamiento | `nivel1/ej1_*.py` a `ej5_*.py` |
| 🟠 Nivel 2 | Estado encapsulado avanzado (`nonlocal`) | `nivel2/ej6_*.py` a `ej10_*.py` |
| 🔵 Nivel 3 | HOFs complejas combinadas | `nivel3/ej11_*.py` a `ej15_*.py` |
| 🟣 Nivel 4 | Patrones avanzados de arquitectura funcional | `nivel4/ej16_*.py` a `ej20_*.py` |

## 🧠 Conceptos aplicados

- **Higher-Order Functions (HOFs):** funciones que reciben y/o retornan otras funciones.
- **Closures:** funciones anidadas que capturan y encapsulan estado privado con `nonlocal`.
- **Lambdas:** comportamiento inyectado dinámicamente como parámetro (predicados,
  transformaciones, reglas de validación, callbacks de eventos, etc.).

## 👤 Autor

_Completa aquí tu nombre y curso._
