class Asiento:
    def __init__(self, numero, fila, precio_base):
        if not isinstance(numero, int) or not isinstance(fila, str):
            raise ValueError(\"El número del asiento debe ser un entero y la fila una cadena.\")
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio_base = precio_base
        self.__precio = precio_base

    # Getters y Setters
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def set_reservado(self, estado):
        self.__reservado = estado

    def set_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError(\"El precio no puede ser negativo.\")
        self.__precio = nuevo_precio

    # Métodos para descuentos
    def calcular_precio(self, es_miercoles=False, es_mayor=False):
        descuento = 0
        if es_miercoles:
            descuento += 0.20
        if es_mayor:
            descuento += 0.30
        self.__precio = self.__precio_base * (1 - descuento)


class SalaCine:
    def __init__(self, precio_base):
        self.__asientos = []
        self.__precio_base = precio_base

    # Métodos para gestión de asientos
    def agregar_asiento(self, numero, fila):
        if self.buscar_asiento(numero, fila):
            raise ValueError(\"El asiento ya está registrado.\")
        nuevo_asiento = Asiento(numero, fila, self.__precio_base)
        self.__asientos.append(nuevo_asiento)

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None

    def reservar_asiento(self, numero, fila, es_miercoles=False, es_mayor=False):
        asiento = self.buscar_asiento(numero, fila)
        if not asiento:
            raise ValueError(\"Asiento no encontrado.\")
        if asiento.get_reservado():
            raise ValueError(\"El asiento ya está reservado.\")
        asiento.calcular_precio(es_miercoles, es_mayor)
        asiento.set_reservado(True)

    def cancelar_reserva(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        if not asiento:
            raise ValueError(\"Asiento no encontrado.\")
        if not asiento.get_reservado():
            raise ValueError(\"El asiento no está reservado.\")
        asiento.set_reservado(False)
        asiento.set_precio(self.__precio_base)

    def mostrar_asientos(self):
        if not self.__asientos:
            print(\"No hay asientos registrados.\")
            return
        for asiento in self.__asientos:
            estado = \"Reservado\" if asiento.get_reservado() else \"Disponible\"\n            print(f\"Asiento {asiento.get_numero()}-{asiento.get_fila()} | {estado} | Precio: {asiento.get_precio():.2f}\")


# Ejemplo de uso
if __name__ == \"__main__\":
    sala = SalaCine(precio_base=10.0)

    # Agregar asientos
    sala.agregar_asiento(1, \"A\")
    sala.agregar_asiento(2, \"A\")
    sala.agregar_asiento(1, \"B\")

    # Mostrar asientos
    print(\"Asientos disponibles:\")
    sala.mostrar_asientos()

    # Reservar asiento
    sala.reservar_asiento(1, \"A\", es_miercoles=True, es_mayor=False)
    print(\"\\nTras reservar asiento 1A:\")
    sala.mostrar_asientos()

    # Cancelar reserva
    sala.cancelar_reserva(1, \"A\")
    print(\"\\nTras cancelar la reserva del asiento 1A:\")
    sala.mostrar_asientos()
