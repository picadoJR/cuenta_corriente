import random

class cuentacorriente:
    def __init__(self, nombre_titular: str, saldo: float):
        try:
            if not isinstance(nombre_titular, str) or not nombre_titular.strip():
                raise ValueError("El nombre del titular debe ser una cadena no vacía.")
            if not isinstance(saldo, (int, float)) or saldo < 0:
                raise ValueError("El saldo inicial debe ser un número >= 0.")

            self.nombre_titular = nombre_titular.strip()
            self.saldo = float(saldo)
            self.numero_cuenta = abs(random.randint(0, 10**9))
        except Exception as e:
            print(f"Error al crear la cuenta: {e}")
            raise

    def set_ingreso(self, ingreso: float):
        try:
            if not isinstance(ingreso, (int, float)):
                raise TypeError("El ingreso debe ser un número.")
            if ingreso <= 0:
                raise ValueError("No se permiten ingresos negativos o cero.")
            self.saldo += ingreso
            print(f"Ingreso exitoso de {ingreso}. Nuevo saldo: {self.saldo}")
        except Exception as e:
            print(f"Error al realizar el ingreso: {e}")

    def set_retiro(self, retiro: float):
        try:
            if not isinstance(retiro, (int, float)):
                raise TypeError("El retiro debe ser un número.")
            if retiro <= 0:
                raise ValueError("El retiro debe ser un número positivo.")
            if retiro > self.saldo:
                raise ValueError("Fondos insuficientes para el retiro.")
            self.saldo -= retiro
            print(f"Retiro exitoso de {retiro}. Nuevo saldo: {self.saldo}")
        except Exception as e:
            print(f"Error al realizar el retiro: {e}")

    def get_saldo(self) -> str:
        try:
            return f"El saldo de la cuenta es: {self.saldo}"
        except Exception as e:
            return f"Error al obtener el saldo: {e}"

    @staticmethod
    def transferencia(titular1, titular2, cantidad: float):
        try:
            if not isinstance(titular1, cuentacorriente) or not isinstance(titular2, cuentacorriente):
                raise TypeError("titular1 y titular2 deben ser objetos 'cuentacorriente'.")
            if not isinstance(cantidad, (int, float)):
                raise TypeError("La cantidad debe ser un número.")
            if cantidad <= 0:
                raise ValueError("La cantidad a transferir debe ser positiva.")
            if cantidad > titular1.saldo:
                raise ValueError("Fondos insuficientes para realizar la transferencia.")

            titular1.saldo -= cantidad
            titular2.saldo += cantidad
            print(f"Transferencia exitosa de {cantidad} de {titular1.nombre_titular} a {titular2.nombre_titular}.")
        except Exception as e:
            print(f"Error en la transferencia: {e}")

    def get_datos_cuenta(self) -> str:
        try:
            return f"Cuenta corriente de {self.nombre_titular}, número: {self.numero_cuenta}, saldo: {self.saldo}"
        except Exception as e:
            return f"Error al obtener los datos de la cuenta: {e}"
