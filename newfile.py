import sys

# Lista para almacenar los vehículos registrados
vehiculos = []

# Marcas predefinidas
marcas_validas = ["toyota", "ford", "chevrolet"]

# Función para registrar un vehículo
def registrar_vehiculo():
    marca = input("Ingrese la marca del vehículo: ")
    if marca not in marcas_validas:
        print("Marca no válida. Las marcas válidas son: Toyota, Ford, Chevrolet")
        return

    ano_fabricacion = int(input("Ingrese el año de fabricación del vehículo: "))
    kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
    costo_reparacion = float(input("Ingrese el costo de reparación del vehículo (en pesos): "))
    impuesto_servicio = costo_reparacion * 0.08
    costo_total = costo_reparacion + impuesto_servicio
    
    vehiculo = {
        "Marca": marca,
        "Año de Fabricación": ano_fabricacion,
        "Kilometraje": kilometraje,
        "Costo de Reparación": costo_reparacion,
        "Impuesto de Servicio": impuesto_servicio,
        "Costo Total": costo_total
    }
    
    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.\n")
    
def mostrar_vehiculos():
    if not vehiculos:
        print("No hay vehículos registrados.\n")
        return

    for vehiculo in vehiculos:
        print(f"Marca: {vehiculo['Marca']}")
        print(f"Año de Fabricación: {vehiculo['Año de Fabricación']}")
        print(f"Kilometraje: {vehiculo['Kilometraje']}")
        print(f"Costo de Reparación: {vehiculo['Costo de Reparación']:.2f}")
        print(f"Impuesto de Servicio: {vehiculo['Impuesto de Servicio']:.2f}")
        print(f"Costo Total: {vehiculo['Costo Total']:.2f}")
        print("")

def generar_orden_reparacion():
    print("Marcas disponibles: Toyota, Ford, Chevrolet")
    marca_seleccionada = input("Ingrese la marca de los vehículos para generar la orden de reparación (o 'todos' para incluir todas las marcas): ")

    if marca_seleccionada != 'todos' and marca_seleccionada not in marcas_validas:
        print("Marca no válida. Las marcas válidas son: Toyota, Ford, Chevrolet")
        return

    with open('ordenes_de_reparacion.txt', 'w') as archivo:
        for vehiculo in vehiculos:
            if marca_seleccionada == 'todos' or vehiculo['Marca'] == marca_seleccionada:
                archivo.write(f"Marca: {vehiculo['Marca']}\n")
                archivo.write(f"Año de Fabricación: {vehiculo['Año de Fabricación']}\n")
                archivo.write(f"Kilometraje: {vehiculo['Kilometraje']}\n")
                archivo.write(f"Costo de Reparación: {vehiculo['Costo de Reparación']:.2f}\n")
                archivo.write(f"Impuesto de Servicio: {vehiculo['Impuesto de Servicio']:.2f}\n")
                archivo.write(f"Costo Total: {vehiculo['Costo Total']:.2f}\n")
                archivo.write("\n")

    print("Archivo 'ordenes_de_reparacion.txt' generado exitosamente.\n")


def main():
    while True:
        print("1. Registrar vehículo")
        print("2. Mostrar vehículos registrados")
        print("3. Generar orden de reparación")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_vehiculo()
        elif opcion == '2':
            mostrar_vehiculos()
        elif opcion == '3':
            generar_orden_reparacion()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()