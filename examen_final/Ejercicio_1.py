class Vehiculo:
    def __init__(self, marca, modelo, anio=2020):
        self.marca = marca
        self.modelo = modelo
        if anio > 0:
            self.anio = anio
        else:
            print("Error: El año debe ser mayor que cero. Se asignará 2020 por defecto.")
            self.anio = 2020

    def actualizar_marca(self, nueva_marca):
        self.marca = nueva_marca
        print("Marca actualizada correctamente.")

    def actualizar_anio(self, nuevo_anio):
        if nuevo_anio > 0:
            self.anio = nuevo_anio
            print("Año actualizado correctamente.")
        else:
            print("Error: El año debe ser mayor que cero.")

    def mostrar_datos(self):
        print("Marca: {}".format(self.marca))
        print("Modelo: {}".format(self.modelo))
        print("Año: {}".format(self.anio))


class VehiculoAlquiler(Vehiculo):

    def __init__(self, marca, modelo, codigo, tarifa_diaria, anio=2020):
        super().__init__(marca, modelo, anio)
        self.codigo = codigo
        if tarifa_diaria > 0:
            self.__tarifa_diaria = tarifa_diaria
        else:
            print("Error: La tarifa inicial debe ser mayor que cero. Se asignará S/ 50.00.")
            self.__tarifa_diaria = 50.0

    def obtener_tarifa(self):
        return self.__tarifa_diaria

    def actualizar_tarifa(self, nueva_tarifa):
        if nueva_tarifa > 0:
            self.__tarifa_diaria = nueva_tarifa
            print("Tarifa actualizada correctamente a S/ {:.2f}".format(self.__tarifa_diaria))
        else:
            print("Error: La tarifa debe ser mayor que cero. No se realizaron cambios.")

    def aumentar_tarifa(self, porcentaje=10):
        if porcentaje > 0:
            incremento = self.__tarifa_diaria * (porcentaje / 100)
            self.__tarifa_diaria += incremento
            print("Tarifa incrementada en {}%. Nueva tarifa: S/ {:.2f}".format(porcentaje, self.__tarifa_diaria))
        else:
            print("Error: El porcentaje de incremento debe ser mayor que cero.")

    def calcular_descuento(self, dias_alquiler):
        if dias_alquiler <= 0:
            print("Error: Los días de alquiler deben ser mayores que cero.")
            return

        importe_antes = self.__tarifa_diaria * dias_alquiler

        if dias_alquiler < 2:
            porcentaje_desc = 0.05
        elif dias_alquiler <= 5:
            porcentaje_desc = 0.10
        else:
            porcentaje_desc = 0.15

        descuento = importe_antes * porcentaje_desc
        total_final = importe_antes - descuento

        print("\n--- Resumen de Alquiler ({} días) ---".format(dias_alquiler))
        print("Código: {}".format(self.codigo))
        self.mostrar_datos()
        print("Tarifa diaria actual: S/ {:.2f}".format(self.__tarifa_diaria))
        print("Importe antes del descuento: S/ {:.2f}".format(importe_antes))
        print("Descuento aplicado ({:.0f}%): S/ {:.2f}".format(porcentaje_desc * 100, descuento))
        print("Total final a pagar: S/ {:.2f}".format(total_final))

# PRUEBAS OBLIGATORIAS
# Crear dos vehículos diferentes
vehiculo_1 = VehiculoAlquiler("Toyota", "Corolla", "ALQ-001", 100.0, 2022)
vehiculo_2 = VehiculoAlquiler("Hyundai", "Tucson", "ALQ-002", 150.0)

print("=== VEHÍCULO 1: Incrementos consecutivos y cálculo de descuentos ===")
vehiculo_1.aumentar_tarifa()       # Incremento por defecto (10%) -> 110.00
vehiculo_1.aumentar_tarifa(20)     # Segundo incremento (20%) -> 132.00

# Cálculo de descuentos con distintas cantidades de días
vehiculo_1.calcular_descuento(1)   # Menos de 2 días (5%)
vehiculo_1.calcular_descuento(4)   # De 2 a 5 días (10%)

print("=========================================================")
print("=== VEHÍCULO 2: Descuento > 5 días y validación de tarifa negativa ===")
vehiculo_2.calcular_descuento(7)   # Más de 5 días (15%)

# Intentar asignar una tarifa negativa y verificar que no se modifique
print("\nIntentando asignar tarifa negativa (-80.0) al Vehículo 2:")
vehiculo_2.actualizar_tarifa(-80.0)
print("Tarifa verificada tras intento inválido: S/ {:.2f}".format(vehiculo_2.obtener_tarifa()))