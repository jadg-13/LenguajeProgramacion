class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f'Se han depositado {cantidad} unidades.')
        else:
            print('La cantidad a depositar debe ser mayor que cero.')

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f'Se han retirado {cantidad} unidades.')
        else:
            print('Saldo insuficiente.')

    def consultar_saldo(self):
        print(f'Su saldo actual es: {self.__saldo}')


# Crear una cuenta bancaria
mi_cuenta = CuentaBancaria(1000)

# Intentar acceder directamente al saldo (esto causará un error)
# print(mi_cuenta.__saldo)  # Generará un AttributeError

# Acceder al saldo mediante un método público
mi_cuenta.consultar_saldo()

# # Intentar depositar una cantidad negativa
# mi_cuenta.depositar(-500)

# # Depositar una cantidad válida
# mi_cuenta.depositar(200)

# # Retirar una cantidad válida
# mi_cuenta.retirar(700)

# # Consultar el saldo actual
# mi_cuenta.consultar_saldo()
