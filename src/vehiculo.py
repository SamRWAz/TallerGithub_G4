class Vehiculo:
    """
    Representa un vehículo con sus características principales.

    Attributes:
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        año (int): Año de fabricación.
        kilometraje (int): Kilometraje actual.
        estado_actual (str): Estado actual del vehículo.
        tipo_combustible (str): Tipo de combustible utilizado.
    """

    COMBUSTIBLES_VALIDOS = {"Gasolina", "Diesel", "Eléctrico"}
    
    def __init__(self, marca, modelo, año, kilometraje, estado_actual, tipo_combustible, potencia, color):

        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
        self.estado_actual = estado_actual
        self.potencia = potencia
        # Validamos el tipo de combustible al inicializar
        if tipo_combustible not in self.COMBUSTIBLES_VALIDOS:
            raise ValueError(f"Tipo de combustible inválido: {tipo_combustible}. Debe ser uno de {self.COMBUSTIBLES_VALIDOS}")
        self.tipo_combustible = tipo_combustible
        self.año_actual = 2024
        self.color = color

    def __str__(self):
        return (f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, "
                f"Kilometraje: {self.kilometraje}, Estado: {self.estado}, "
                f"Combustible: {self.combustible}, Color: {self.color}, Potencia: {self.potencia} HP")

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_año(self):
        return self.año

    def get_kilometraje(self):
        return self.kilometraje

    def get_estado_actual(self):
        return self.estado_actual

    def get_tipo_combustible(self):
        return self.tipo_combustible
      
    def get_color(self):
        return self.color

    def get_potencia(self):
        return self.potencia

    def set_marca(self, nueva_marca):
        self.marca = nueva_marca

    def set_modelo(self, nuevo_modelo):
        self.modelo = nuevo_modelo

    def set_año(self, nuevo_año):
        self.año = nuevo_año

    def set_kilometraje(self, nuevo_kilometraje):
        self.kilometraje = nuevo_kilometraje

    def set_estado_actual(self, nuevo_estado):
        self.estado_actual = nuevo_estado

    def set_tipo_combustible(self, nuevo_combustible):
        # Validamos el tipo de combustible al modificarlo
        if nuevo_combustible not in self.COMBUSTIBLES_VALIDOS:
            raise ValueError(f"Tipo de combustible inválido: {nuevo_combustible}. Debe ser uno de {self.COMBUSTIBLES_VALIDOS}")
        self.tipo_combustible = nuevo_combustible
        
    def calcular_antiguedad(self):
        return self.año_actual - self.año
    
    def set_color(self, nuevo_color):
        self.color = nuevo_color
        
    def set_potencia(self, nueva_potencia):
        self.potencia = nueva_potencia


"""

mi_auto = Vehiculo("Toyota", "Corolla", 2020, 15000, "En movimiento", "Gasolina", 150)


print("Marca:", mi_auto.get_marca())                 # Toyota
print("Modelo:", mi_auto.get_modelo())               # Corolla
print("Año:", mi_auto.get_año())                     # 2020
print("Kilometraje:", mi_auto.get_kilometraje())     # 15000
print("Estado:", mi_auto.get_estado_actual())        # En movimiento
print("Tipo de Combustible:", mi_auto.get_tipo_combustible())  # Gasolina


# Cambiar el tipo de combustible
mi_auto.set_tipo_combustible("Diesel")
print("Nuevo Tipo de Combustible:", mi_auto.get_tipo_combustible())  # Diesel

# Intentar cambiar el tipo de combustible a uno inválido
try:
    mi_auto.set_tipo_combustible("Híbrido")  # Este lanzará un ValueError
except ValueError as e:
    print(e)  # Imprime el error: Tipo de combustible inválido: Híbrido. Debe ser uno de {'Gasolina', 'Diesel', 'Eléctrico'}

print("Potencia:", mi_auto.get_potencia())           # 150
    
"""