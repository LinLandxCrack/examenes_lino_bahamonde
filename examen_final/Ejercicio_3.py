import datetime

def registrar_pedido(funcion):
    def wrapper(*args, **kwargs):
        ahora = datetime.datetime.now()
        print("Fecha y hora de ejecución: {}".format(ahora.strftime("%Y-%m-%d %H:%M:%S")))
        resultado = funcion(*args, **kwargs)
        if resultado is not None:
            print("Operación finalizada correctamente.")
        return resultado
    return wrapper

@registrar_pedido
def calcular_total(*args):
    total = 0.0
    for precio in args:
        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio <= 0:
            print("Error: El precio '{}' no es válido. Debe ser numérico y mayor que cero.".format(precio))
            return None
        total += precio
    return total

@registrar_pedido
def procesar_pedido(cliente, **kwargs):
    print("Cliente: {}".format(cliente))
    total = 0.0
    for producto, precio in kwargs.items():
        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio <= 0:
            print("Error: El producto '{}' tiene un precio inválido ({}). Operación cancelada.".format(producto, precio))
            return None
        print(" - {}: S/ {:.2f}".format(producto, precio))
        total += precio
    return total


# PRUEBAS OBLIGATORIAS
print("=== PRUEBA 1: calcular_total con 3 precios ===")
total_1 = calcular_total(15.50, 22.00, 8.50)
if total_1 is not None:
    print("Importe total (3 precios): S/ {:.2f}".format(total_1))

print("=========================================================")

print("=== PRUEBA 2: calcular_total con 6 precios ===")
total_2 = calcular_total(10.0, 12.5, 8.0, 25.0, 14.5, 6.0)
if total_2 is not None:
    print("Importe total (6 precios): S/ {:.2f}".format(total_2))

print("=========================================================")

print("=== PRUEBA 3: procesar_pedido con 4 productos válidos ===")
pedido_1 = procesar_pedido(
    "George Cerdito",
    Hamburguesa=24.50,
    Papas_Fritas=9.00,
    Gaseosa=6.50,
    Helado=8.00
)
if pedido_1 is not None:
    print("Importe total del pedido: S/ {:.2f}".format(pedido_1))

print("=========================================================")

print("=== PRUEBA 4: procesar_pedido con precio negativo ===")
pedido_2 = procesar_pedido(
    "Peppa Cerdita",
    Pizza=38.00,
    Alitas=-15.00,
    Limonada=7.50
)
if pedido_2 is not None:
    print("Importe total del pedido: S/ {:.2f}".format(pedido_2))