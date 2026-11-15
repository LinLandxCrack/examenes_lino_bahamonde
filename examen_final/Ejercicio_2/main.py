import Operaciones

print("=== EJECUCIÓN 1 (n = 10) ===")
try:
    lista_1 = Operaciones.generar_lista(10)
    sin_dup_1 = Operaciones.eliminar_duplicados(lista_1)
    asc_1, desc_1 = Operaciones.ordenar_listas(sin_dup_1)
    par_1 = Operaciones.mayor_par(sin_dup_1)

    print("Lista original: {}".format(lista_1))
    print("Lista sin duplicados: {}".format(sin_dup_1))
    print("Orden ascendente: {}".format(asc_1))
    print("Orden descendente: {}".format(desc_1))
    if par_1 is not None:
        print("Mayor número par: {}".format(par_1))
except ValueError as error:
    print("Error de validación: {}".format(error))

print("=========================================================")

print("=== EJECUCIÓN 2 (n = 6) ===")
try:
    lista_2 = Operaciones.generar_lista(6)
    sin_dup_2 = Operaciones.eliminar_duplicados(lista_2)
    asc_2, desc_2 = Operaciones.ordenar_listas(sin_dup_2)
    par_2 = Operaciones.mayor_par(sin_dup_2)

    print("Lista original: {}".format(lista_2))
    print("Lista sin duplicados: {}".format(sin_dup_2))
    print("Orden ascendente: {}".format(asc_2))
    print("Orden descendente: {}".format(desc_2))
    if par_2 is not None:
        print("Mayor número par: {}".format(par_2))

    print("\nConsultando posición válida (índice 2):")
    elem_valido = Operaciones.obtener_elemento(lista_2, 2)
    print("Elemento en posición 2: {}".format(elem_valido))

    print("\nConsultando posición fuera de rango (índice 25):")
    Operaciones.obtener_elemento(lista_2, 25)

except ValueError as error:
    print("Error de validación: {}".format(error))

print("=========================================================")

print("=== EJECUCIÓN 3 (Cantidad n inválida) ===")
try:
    Operaciones.generar_lista(-4)
except ValueError as error:
    print("Error capturado correctamente: {}".format(error))