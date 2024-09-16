class Main:
    def __init__(self):
        self.vehiculos = []

    def añadir_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"Vehículo añadido: {vehiculo}")

    def buscar_por_año(self, año):
        resultado = [vehiculo for vehiculo in self.vehiculos if vehiculo.año == año]
        if resultado:
            print(f"Vehículos encontrados para el año {año}:")
            for vehiculo in resultado:
                print(vehiculo)
        else:
            print(f"No se encontraron vehículos del año {año}")

    def imprimir_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.")
        else:
            print("Vehículos registrados:")
            for vehiculo in self.vehiculos:
                print(vehiculo)


if __name__ == "__main__":

    main = Main()


    vehiculo1 = Vehiculo("Toyota", "Corolla", 50000, 2020, "Usado", "Gasolina", "Rojo", 132)
    vehiculo2 = Vehiculo("Ford", "Focus", 30000, 2019, "Usado", "Diésel", "Azul", 150)
    vehiculo3 = Vehiculo("Honda", "Civic", 10000, 2020, "Nuevo", "Híbrido", "Negro", 158)

    main.añadir_vehiculo(vehiculo1)
    main.añadir_vehiculo(vehiculo2)
    main.añadir_vehiculo(vehiculo3)

  
    main.imprimir_vehiculos()
    main.buscar_por_año(2020)
    main.buscar_por_año(2018)