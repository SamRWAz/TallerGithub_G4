
class HistorialMantenimiento:
    def __init__(self, fecha, descripcion_servicio, kilometraje_en_servicio, costo, nombre_mecanico):
        """
        Inicializa los atributos del historial de mantenimiento.
        
        Args:
            fecha (str): Fecha del mantenimiento o reparación.
            descripcion_servicio (str): Descripción del servicio realizado.
            kilometraje_en_servicio (int): Kilometraje del vehículo al momento del servicio.
            costo (float): Costo del servicio.
            nombre_mecanico (str): Nombre del mecánico que realizó el servicio.
        """
        self._fecha = fecha
        self._descripcion_servicio = descripcion_servicio
        self._kilometraje_en_servicio = kilometraje_en_servicio
        self._costo = costo
        self._nombre_mecanico = nombre_mecanico

    # Getters
    def get_fecha(self):
        """
        Obtiene la fecha del servicio.
        Returns:
            str: Fecha del servicio.
        """
        return self._fecha

    def get_descripcion_servicio(self):
        """
        Obtiene la descripción del servicio realizado.
        Returns:
            str: Descripción del servicio.
        """
        return self._descripcion_servicio

    def get_kilometraje_en_servicio(self):
        """
        Obtiene el kilometraje del vehículo durante el servicio.
        Returns:
            int: Kilometraje del vehículo.
        """
        return self._kilometraje_en_servicio

    def get_costo(self):
        """
        Obtiene el costo del servicio.
        Returns:
            float: Costo del servicio.
        """
        return self._costo

    def get_nombre_mecanico(self):
        """
        Obtiene el nombre del mecánico que realizó el servicio.
        Returns:
            str: Nombre del mecánico.
        """
        return self._nombre_mecanico

    # Setters
    def set_fecha(self, fecha):
        """
        Establece la fecha del servicio.
        Args:
            fecha (str): Nueva fecha del servicio.
        """
        self._fecha = fecha

    def set_descripcion_servicio(self, descripcion_servicio):
        """
        Establece la descripción del servicio realizado.
        Args:
            descripcion_servicio (str): Nueva descripción del servicio.
        """
        self._descripcion_servicio = descripcion_servicio

    def set_kilometraje_en_servicio(self, kilometraje_en_servicio):
        """
        Establece el kilometraje del vehículo durante el servicio.
        Args:
            kilometraje_en_servicio (int): Nuevo kilometraje.
        """
        self._kilometraje_en_servicio = kilometraje_en_servicio

    def set_costo(self, costo):
        """
        Establece el costo del servicio.
        Args:
            costo (float): Nuevo costo del servicio.
        """
        self._costo = costo

    def set_nombre_mecanico(self, nombre_mecanico):
        """
        Establece el nombre del mecánico que realizó el servicio.
        Args:
            nombre_mecanico (str): Nuevo nombre del mecánico.
        """
        self._nombre_mecanico = nombre_mecanico
