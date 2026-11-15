# Diccionario inicial con al menos cuatro productos
inventario = {
    "P001": {"nombre": "Laptop", "precio": 3200.00, "cantidad": 5},
    "P002": {"nombre": "Mouse", "precio": 45.50, "cantidad": 20},
    "P003": {"nombre": "Teclado", "precio": 120.00, "cantidad": 12},
    "P004": {"nombre": "Monitor", "precio": 850.00, "cantidad": 8}
}


def mostrar_inventario(inv):
    print("\n--- INVENTARIO DE PRODUCTOS ---")
    for codigo, datos in inv.items():
        print("Código: {} | Nombre: {} | Precio: S/ {:.2f} | Stock: {} unidades".format(
            codigo, datos["nombre"], datos["precio"], datos["cantidad"]
        ))


def registrar_compra(inv, codigo_producto, cantidad_solicitada):
    if codigo_producto not in inv:
        print("Error: El producto '{}' no existe en el inventario.".format(codigo_producto))
        return None

    if cantidad_solicitada <= 0:
        print("Error: La cantidad solicitada debe ser mayor que cero.")
        return None

    stock_disponible = inv[codigo_producto]["cantidad"]
    nombre_producto = inv[codigo_producto]["nombre"]

    if cantidad_solicitada > stock_disponible:
        print("Error: Stock insuficiente para '{}'. Disponible: {} unidades.".format(
            nombre_producto, stock_disponible
        ))
        return None

    precio_unitario = inv[codigo_producto]["precio"]
    importe = precio_unitario * cantidad_solicitada
    inv[codigo_producto]["cantidad"] -= cantidad_solicitada

    print("Compra exitosa: {} unidad(es) de '{}' | Importe total: S/ {:.2f}".format(
        cantidad_solicitada, nombre_producto, importe
    ))
    return importe


def calcular_valor_total(inv):
    valor_total = 0.0
    for datos in inv.values():
        valor_total += datos["precio"] * datos["cantidad"]
    return valor_total


# PRUEBAS OBLIGATORIAS
# Mostrar inventario inicial y su valor total
print("=== ESTADO INICIAL ===")
mostrar_inventario(inventario)
print("Valor monetario total inicial: S/ {:.2f}".format(calcular_valor_total(inventario)))

print("=========================================================")

print("=== REGISTRO DE COMPRAS ===")
registrar_compra(inventario, "P002", 4)    # Compra válida (4 Mouse)
registrar_compra(inventario, "P099", 2)    # Producto inexistente
registrar_compra(inventario, "P001", 10)   # Cantidad superior al stock (hay 5 Laptops)

print("=========================================================")

# Mostrar inventario actualizado y valor monetario total
print("=== ESTADO ACTUALIZADO ===")
mostrar_inventario(inventario)
print("Valor monetario total actualizado: S/ {:.2f}".format(calcular_valor_total(inventario)))