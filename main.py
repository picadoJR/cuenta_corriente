from cuentacorriente import cuentacorriente

def main():
    print("=== PRUEBA DE EXCEPCIONES Y VALIDACIONES ===\n")

    try:
        print("Creando cuenta con nombre vacío...")
        cuenta_error = cuentacorriente("", 1000)
    except Exception as e:
        print("➡️ Error atrapado correctamente:", e)

    print("\nCreando cuentas válidas...")
    cuenta1 = cuentacorriente("Reinaldo Picado", 5000)
    cuenta2 = cuentacorriente("Adrian Berrio", 2000)
    print(cuenta1.get_datos_cuenta())
    print(cuenta2.get_datos_cuenta())

    print("\nIntentando ingreso inválido...")
    cuenta1.set_ingreso(-1000)
    cuenta1.set_ingreso("mil")

    print("\nRealizando ingreso válido...")
    cuenta1.set_ingreso(1500)

    print("\nIntentando retiro inválido...")
    cuenta1.set_retiro(0)
    cuenta1.set_retiro(10000)
    cuenta1.set_retiro("quinientos")

    print("\nRealizando retiro válido...")
    cuenta1.set_retiro(1000)

    print("\nIntentando transferencia con errores...")
    cuentacorriente.transferencia(cuenta1, cuenta2, "cien")
    cuentacorriente.transferencia(cuenta1, cuenta2, -200)
    cuentacorriente.transferencia(cuenta1, 123, 100)
    cuentacorriente.transferencia(cuenta1, cuenta2, 10000)

    print("\nTransferencia válida...")
    cuentacorriente.transferencia(cuenta1, cuenta2, 500)

    print("\n=== ESTADO FINAL DE LAS CUENTAS ===")
    print(cuenta1.get_datos_cuenta())
    print(cuenta2.get_datos_cuenta())


if __name__ == "__main__":
    main()
