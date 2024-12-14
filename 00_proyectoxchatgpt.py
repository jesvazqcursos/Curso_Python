# Clase Asiento: Representa cada asiento en la sala.
class Asiento:
    def __init__(self, numero, fila, precio):
        # Atributo privado para el número del asiento
        self.__numero = numero
        # Atributo privado para la fila del asiento
        self.__fila = fila
        # Atributo privado para el estado de reserva (True si reservado, False si no)
        self.__reservado = False
        # Atributo privado para el precio del asiento
        self.__precio = precio

    # Getter para obtener el número del asiento
    def get_numero(self):
        return self.__numero

    # Getter para obtener la fila del asiento
    def get_fila(self):
        return self.__fila

    # Getter para verificar si el asiento está reservado
    def esta_reservado(self):
        return self.__reservado

    # Método para reservar el asiento
    def reservar(self, precio):
        if self.__reservado:
            # Si el asiento ya está reservado, lanza una excepción
            raise Exception("El asiento ya está reservado.")
        # Cambia el estado a reservado
        self.__reservado = True
        # Asigna el precio correspondiente al asiento
        self.__precio = precio

    # Método para cancelar la reserva del asiento
    def cancelar_reserva(self):
        if not self.__reservado:
            # Si el asiento no está reservado, lanza una excepción
            raise Exception("El asiento no está reservado.")
        # Cambia el estado a no reservado
        self.__reservado = False

    # Método para obtener el precio del asiento
    def get_precio(self):
        return self.__precio

    # Método para mostrar información del asiento
    def mostrar_informacion(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Asiento {self.__fila}-{self.__numero}: {estado}, Precio: {self.__precio}"

# Clase SalaCine: Administra todos los asientos de la sala.
class SalaCine:
    def __init__(self):
        # Lista privada para almacenar los asientos
        self.__asientos = []

    # Método para agregar un asiento
    def agregar_asiento(self, numero, fila, precio_base):
        # Busca si ya existe un asiento con el mismo número y fila
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                raise Exception("El asiento ya está registrado.")
        # Si no existe, crea un nuevo asiento y lo agrega a la lista
        self.__asientos.append(Asiento(numero, fila, precio_base))

    # Método para reservar un asiento
    def reservar_asiento(self, numero, fila, edad, dia):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                # Calcula el precio final con descuentos
                precio = self.__calcular_precio(asiento.get_precio(), edad, dia)
                # Reserva el asiento con el precio final
                asiento.reservar(precio)
                return
        # Si no encuentra el asiento, lanza una excepción
        raise Exception("Asiento no encontrado.")

    # Método para cancelar la reserva de un asiento
    def cancelar_reserva(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                # Cancela la reserva del asiento
                asiento.cancelar_reserva()
                return
        # Si no encuentra el asiento, lanza una excepción
        raise Exception("Asiento no encontrado.")

    # Método para mostrar todos los asientos
    def mostrar_asientos(self):
        for asiento in self.__asientos:
            # Imprime la información de cada asiento
            print(asiento.mostrar_informacion())

    # Método para buscar un asiento por número y fila
    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                # Retorna la información del asiento encontrado
                return asiento.mostrar_informacion()
        # Si no encuentra el asiento, lanza una excepción
        raise Exception("Asiento no encontrado.")

    # Método privado para calcular el precio final del asiento con descuentos
    def __calcular_precio(self, precio_base, edad, dia):
        # Aplica un descuento del 20% si es miércoles
        if dia.lower() == "miércoles":
            precio_base *= 0.8
        # Aplica un descuento del 30% si el espectador es mayor de 65 años
        if edad >= 65:
            precio_base *= 0.7
        # Retorna el precio calculado
        return precio_base

# Ejemplo de uso de las clases
def main():
    # Crear una sala de cine
    sala = SalaCine()

    # Agregar asientos a la sala
    sala.agregar_asiento(1, "A", 10.0)
    sala.agregar_asiento(2, "A", 10.0)

    # Reservar un asiento
    try:
        sala.reservar_asiento(1, "A", 70, "miércoles")
    except Exception as e:
        print(e)

    # Mostrar información de los asientos
    sala.mostrar_asientos()

    # Cancelar la reserva de un asiento
    try:
        sala.cancelar_reserva(1, "A")
    except Exception as e:
        print(e)

    # Buscar un asiento
    try:
        print(sala.buscar_asiento(2, "A"))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
