# limpiador-de-ventas-python
Script en Python que limpia archivos CSV con datos sucios, filtra registros inválidos y genera métricas clave de ventas.
# Limpiador y Analizador de Datos de Ventas en Python

Script en Python diseñado para procesar archivos CSV con datos desordenados o corruptos, normalizar su formato, descartar registros inválidos y generar un reporte limpio junto con un resumen ejecutivo en consola.

## Características principales

* **Limpieza y normalización:** Elimina filas completamente vacías, recorta espacios en blanco innecesarios y unifica el texto de los productos a formato título (`Title Case`).
* **Sanitización de valores numéricos:** Limpia símbolos de moneda (`$`) y comas en los precios para convertirlos en valores decimales (`float`), descartando de forma segura registros con datos corruptos sin detener la ejecución del programa.
* **Cálculo automático de métricas:** Genera la columna `Subtotal` por cada venta válida y calcula el ingreso total, el ticket promedio y el producto más vendido.
* **Cero dependencias externas:** Desarrollado íntegramente con la librería estándar de Python (`csv` y `collections`).

## Transformación de datos (Antes vs. Después)

| Estado | Fecha | Producto | Cantidad | Precio Unitario | Subtotal |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Entrada (`ventas_sucias.csv`)** | `2026-10-01` | `  laptop lenovo ` | `1` | `$12500.50` | *No existe* |
| **Salida (`ventas_limpias.csv`)** | `2026-10-01` | `Laptop Lenovo` | `1` | `12500.5` | `12500.5` |

## Requisitos

* Python 3.6 o superior.

## Instalación y uso

1. Clona este repositorio en tu computadora:
   ```bash
   git clone [https://github.com/](https://github.com/)Taurox29/limpiador-datos-ventas-python.git
   cd limpiador-datos-ventas-python

Asegúrate de tener el archivo de entrada ventas_sucias.csv en la misma carpeta que el script y ejecuta:

Bash
python limpiador_ventas.py

Ejemplo de salida en consola
Plaintext
Aviso: Fila 8 descartada por precio o cantidad inválida ('error_precio').

=============================================
RESUMEN EJECUTIVO DE VENTAS
=============================================
Registros válidos procesados : 8
Filas vacías/inválidas omitidas: 3
Ingreso Total Calculado      : $36,151.00
Ticket Promedio por Venta    : $4,518.88
Producto Más Vendido         : Mouse Inalambrico (5 unidades)
=============================================

Desarrollado por Alberto López Fuentes
