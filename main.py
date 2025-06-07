# main.py
import ventas
import clientes
import destinos

def menu_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        subop = input("Seleccione una opción: ")

        if subop == "1":
            clientes.mostrar_clientes()
        elif subop == "2":
            clientes.agregar_cliente()
        elif subop == "3":
            clientes.modificar_cliente()
        elif subop == "4":
            clientes.eliminar_cliente()
        elif subop == "5":
            break
        else:
            print("Opción inválida.")

def menu_destinos():
    while True:
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menú Principal")
        subop = input("Seleccione una opción: ")

        if subop == "1":
            destinos.mostrar_destinos()
        elif subop == "2":
            destinos.agregar_destino()
        elif subop == "3":
            destinos.modificar_destino()
        elif subop == "4":
            destinos.eliminar_destino()
        elif subop == "5":
            break
        else:
            print("Opción inválida.")

def menu_ventas():
    while True:
        print("\n-- GESTIONAR VENTAS --")
        print("1. Registrar Venta")
        print("2. Ver Ventas")
        print("3. Botón de Arrepentimiento")
        print("4. Volver al Menú Principal")
        subop = input("Seleccione una opción: ")

        if subop == "1":
            ventas.registrar_venta()
        elif subop == "2":
            ventas.ver_ventas()
        elif subop == "3":
            ventas.boton_arrepentimiento()
        elif subop == "4":
            break
        else:
            print("Opción inválida.")

def menu_reportes():
    while True:
        print("\n-- REPORTES --")
        print("1. Ventas por Destino")
        print("2. Total Recaudado")
        print("3. Volver al Menú Principal")
        subop = input("Seleccione una opción: ")

        if subop == "1":
            ventas.reporte_ventas_por_destino()
        elif subop == "2":
            ventas.reporte_total_recaudado()
        elif subop == "3":
            break
        else:
            print("Opción inválida.")
# Menú principal
while True:
    print("\nBienvenido a SkyRoute")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Reportes")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menu_clientes()
    elif opcion == "2":
        menu_destinos()
    elif opcion == "3":
        menu_ventas()
    elif opcion == "4":
        menu_reportes()
    elif opcion == "5":
        print("Gracias por usar SkyRoute.")
        break
    else:
        print("Opción inválida.")