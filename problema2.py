# ============================================================
# Universidad Nacional Abierta y a Distancia - UNAD
# Fundamentos de Programacion 
# Grupo: 213022_34
# Fase 5 - Evaluacion Final POA
# Problema2 : Gestión de precios con promociones en un menú
# Estudiante: Josias Madera Martinez
# Fecha: Mayo de 2026
# ============================================================
#  PROBLEMA 2: Gestión de precios con promociones en un menú
# ============================================================

# --- MATRIZ DEL MENÚ ---
# Estructura: [Nombre, Categoría, Precio Base]
menu = [
    ["Bandeja Paisa",   "Plato Fuerte",  35000],
    ["Ajiaco",          "Plato Fuerte",  28000],
    ["Limonada Natural","Bebida",        8000 ],
    ["Jugo de Mango",   "Bebida",        12000],
    ["Brownie",         "Postre",        15000],
    ["Cheesecake",      "Postre",        22000],
]

# --- PARÁMETROS DE LA PROMOCIÓN ---
CATEGORIA_OBJETIVO = "Plato Fuerte"
UMBRAL_PRECIO      = 20000   # Solo aplica si el precio base supera este valor
DESCUENTO          = 0.15    # 15%


# --- MÓDULO (FUNCIÓN) ---
def calcular_precio_final(nombre, categoria, precio_base):
    """
    Retorna el precio final del producto.
    Aplica 15% de descuento si:
      - La categoría coincide con CATEGORIA_OBJETIVO, Y
      - El precio base es mayor al UMBRAL_PRECIO.
    De lo contrario, mantiene el precio base.
    """
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        precio_final = precio_base * (1 - DESCUENTO)
        aplico = "✔ Descuento aplicado"
    else:
        
        precio_final = precio_base
        aplico = "  Sin descuento    "

    return precio_final, aplico


# --- SALIDA ---
print("=" * 60)
print(f"  MENÚ DEL RESTAURANTE  |  Promoción: {int(DESCUENTO*100)}% en {CATEGORIA_OBJETIVO}")
print(f"  (Precio base > ${UMBRAL_PRECIO:,})")
print("=" * 60)
print(f"{'Producto':<18} {'Categoría':<14} {'Base':>9} {'Final':>9}  Estado")
print("-" * 60)

for producto in menu:
    nombre, categoria, precio_base = producto          # Desempaquetar fila
    precio_final, estado = calcular_precio_final(nombre, categoria, precio_base)

    print(f"{nombre:<18} {categoria:<14} ${precio_base:>8,} ${precio_final:>8,.0f}  {estado}")

print("=" * 60)
