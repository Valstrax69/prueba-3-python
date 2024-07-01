
import json
def limpiar_pantalla():
    import os
    os.system("cls")

print("bienvenido al servicio de reparacion")
main()

marcas = [Toyota, Ford, Chevrolet]
#lista almacenar vehiculos
vehiculos = []
#1 registrar_vehiculo   
#2 listar_vehiculos_registrados
#3 imprimir_orden_reparación
#4 salir del programa

def registrar_vehiculo():
    limpiar_pantalla()
    print("Bienvenido al registro de su vehiculo")
    while True:
        try:
            marca = input("Ingrese la marca del vehiculo: ")
            año_fabricacion = int(input("Ingrese el año de fabricación: "))
            kilometraje = int(input("Ingrese el kilometraje del vehiculo: "))
            costo_reparacion_estimado = int(input("Ingrese el costo de reparacion estimado: "))

            impuesto_servicio = costo_reparacion_estimado * 0.08
            costo_total = costo_reparacion_estimado + impuesto_servicio

            vehiculo = {
                "marca": marca,
                "año_fabricacion": año_fabricacion,
                "kilometraje": kilometraje,
                "costo_reparacion_estimado": costo_reparacion_estimado,
                "impuesto_servicio": impuesto_servicio,
                "costo_total": costo_total
            }

def imprimir_orden_reparacion():
    limpiar_pantalla()
    if vehiculos:
        print("Listado de Vehículos Registrados:")
            print(f"Vehículo {index}:")
            print(f"Marca: {vehiculo['marca']}")
            print(f"Año de fabricación: {vehiculo['año_fabricacion']}")
            print(f"Kilometraje: {vehiculo['kilometraje']}")
            print(f"Costo de reparación estimado: {vehiculo['costo_reparacion_estimado']}")
            print(f"Impuesto de servicio: {vehiculo['impuesto_servicio']}")
            print(f"Costo total: {vehiculo['costo_total']}")
            print("--------------------------")
    else:
        print("No hay vehículos registrados.")
def mostrar_menu():
    '''
           Menu de Opciones
     1- Registrar Vehiculo
     2- Listar Vehiculos Registrados
     3- Imprimir Orden de Reparación
     4- Salir del menu
    '''

def salir_del_programa():
    print(" Saliendo del programa")
    quit()

def main():
    mostrar_menu()
    opcion = input("Seleccione una opción")
    while True:
        if opcion == '1'
        registrar_vehiculo()
        if opcion == '2'
        listar_vehiculos_registrados()
        if opcion == '3'
        imprimir_orden_reparación()
        if opcion == '4'
        salir_del_programa()
        else:
            print("Opción no válida, intente nuevamente")


