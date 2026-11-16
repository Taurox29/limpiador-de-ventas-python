import csv
from collections import defaultdict

ARCHIVO_ENTRADA = "ventas_sucias.csv"
ARCHIVO_SALIDA = "ventas_limpias.csv"

def limpiar_precio(valor_sucio):
    """Elimina símbolos de moneda/espacios y convierte a float. Devuelve None si es inválido."""
    texto = valor_sucio.replace("$", "").replace(",", "").strip()
    try:
        return float(texto)
    except ValueError:
        return None

def procesar_ventas(ruta_entrada, ruta_salida):
    """Lee el CSV sucio, limpia cada registro, calcula totales y guarda el archivo limpio."""
    registros_limpios = []
    filas_descartadas = 0
    
    # Diccionario para acumular unidades vendidas por producto
    unidades_por_producto = defaultdict(int)
    ingreso_total = 0.0

    with open(ruta_entrada, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for numero_fila, fila in enumerate(lector, start=2):
            # 1. Validar que la fila no esté vacía
            if not fila["Fecha"] or not fila["Producto"]:
                filas_descartadas += 1
                continue

            # 2. Normalizar textos (quitar espacios extra y unificar a Formato Título)
            fecha = fila["Fecha"].strip()
            producto = " ".join(fila["Producto"].split()).title()

            # 3. Validar y convertir números (Cantidad y Precio)
            try:
                cantidad = int(fila["Cantidad"].strip())
            except (ValueError, AttributeError):
                filas_descartadas += 1
                continue

            precio = limpiar_precio(fila["Precio_Unitario"])
            if precio is None or cantidad <= 0:
                print(f"Aviso: Fila {numero_fila} descartada por precio o cantidad inválida ('{fila['Precio_Unitario']}').")
                filas_descartadas += 1
                continue

            # 4. Calcular el subtotal de la venta
            subtotal = round(cantidad * precio, 2)

            # Guardar registro limpio
            registros_limpios.append({
                "Fecha": fecha,
                "Producto": producto,
                "Cantidad": cantidad,
                "Precio_Unitario": precio,
                "Subtotal": subtotal
            })

            # Acumular métricas para el resumen ejecutivo
            ingreso_total += subtotal
            unidades_por_producto[producto] += cantidad

    # 5. Exportar los datos limpios a un nuevo CSV
    if registros_limpios:
        columnas = ["Fecha", "Producto", "Cantidad", "Precio_Unitario", "Subtotal"]
        with open(ruta_salida, mode="w", newline="", encoding="utf-8-sig") as salida:
            escritor = csv.DictWriter(salida, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(registros_limpios)

    # 6. Mostrar resumen ejecutivo en consola
    imprimir_resumen(registros_limpios, filas_descartadas, ingreso_total, unidades_por_producto)

def imprimir_resumen(registros, descartadas, total, productos):
    """Imprime las métricas clave del análisis de ventas."""
    print("\n" + "=" * 45)
    print("RESUMEN EJECUTIVO DE VENTAS")
    print("=" * 45)
    print(f"Registros válidos procesados : {len(registros)}")
    print(f"Filas vacías/inválidas omitidas: {descartadas}")
    print(f"Ingreso Total Calculado      : ${total:,.2f}")

    if registros:
        ticket_promedio = total / len(registros)
        producto_estrella = max(productos, key=productos.get)
        print(f"Ticket Promedio por Venta    : ${ticket_promedio:,.2f}")
        print(f"Producto Más Vendido         : {producto_estrella} ({productos[producto_estrella]} unidades)")
    print("=" * 45 + "\n")

if __name__ == "__main__":
    procesar_ventas(ARCHIVO_ENTRADA, ARCHIVO_SALIDA)