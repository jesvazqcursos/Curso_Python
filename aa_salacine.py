A continuación, se presenta un ejemplo de cómo podrías desarrollar una aplicación en Python para gestionar las reservas de asientos en una sala de cine, cumpliendo con los requisitos especificados:

```python
class Asiento:
    def __init__(self, numero, fila, precio_base):
        self._numero = numero
        self._fila = fila
        self._reservado = False
        self._precio_base = precio_base

    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def is_reservado(self):
        return self._reservado

    def get_precio(self, dia, edad):
        precio = self._precio_base
        if dia.lower() == "miercoles":
            precio *= 0.8
        if edad >= 65:
            precio *= 0.7
        return precio

    def reservar(self, dia, edad):
        if not self._reservado:
            self._reservado = True
            return self.get_precio(dia, edad)
        else:
            raise Exception(f"El asiento {self._numero} en la fila {self._fila} ya está reservado.")

    def cancelar_reserva(self):
        if self._reservado:
            self._reservado = False
        else:
            raise Exception(f"El asiento {self._numero} en la fila {self._fila} no está reservado.")

class SalaCine:
    def __init__(self):
        self._asientos = []

    def agregar_asiento(self, numero, fila, precio_base):
        if self.buscar_asiento(numero, fila) is None:
            self._asientos.append(Asiento(numero, fila, precio_base))
        else:
            raise Exception(f"El asiento {numero} en la fila {fila} ya está registrado.")

    def reservar_asiento(self, numero, fila, dia, edad):
        asiento = self.buscar_asiento(numero, fila)
        if asiento is not None:
            return asiento.reservar(dia, edad)
        else:
            raise Exception(f"El asiento {numero} en la fila {fila} no existe.")

    def cancelar_reserva_asiento(self, numero, fila):
        asiento = self.buscar_asiento(numero, fila)
        if asiento is not None:
            asiento.cancelar_reserva()
        else:
            raise Exception(f"El asiento {numero} en la fila {fila} no existe.")

    def mostrar_asientos(self, dia, edad):
        for asiento in self._asientos:
            estado = "Reservado" if asiento.is_reservado() else "Disponible"
            precio = asiento.get_precio(dia, edad)
            print(f"Asiento {asiento.get_numero()} en fila {asiento.get_fila()}: {estado}, Precio: {precio}")

    def buscar_asiento(self, numero, fila):
        for asiento in self._asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None

# Ejemplo de uso
sala = SalaCine()
sala.agregar_asiento(1, 'A', 10.0)
sala.agregar_asiento(2, 'A', 10.0)
sala.agregar_asiento(3, 'B', 12.0)

sala.mostrar_asientos('miercoles', 70)
precio_reserva = sala.reservar_asiento(1, 'A', 'miercoles', 70)
print(f"Precio de reserva: {precio_reserva}")
sala.mostrar_asientos('miercoles', 70)

sala.cancelar_reserva_asiento(1, 'A')
sala.mostrar_asientos('miercoles', 70)
```

Este código define las clases `Asiento` y `SalaCine` con los métodos necesarios para gestionar las reservas de asientos, aplicar descuentos y manejar las validaciones y excepciones. Puedes adaptar y expandir este código según las necesidades específicas de tu proyecto.
