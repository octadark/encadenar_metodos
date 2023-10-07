class usuario:
    #constructor
    def __init__(self, name):
        #atributos a instancias
        self.name = name
        self.amount = 0
    def hacer_deposito(self, amount):
        self.amount += amount
        return self
    def hacer_retiro(self, amount):
        self.amount -= amount
        return self
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name}, Balance: {self.amount}")
        return self
    def transferir_dinero(self,amount,usuario):
        self.amount -= amount
        usuario.amount += amount
        self.mostrar_balance_usuario()
        usuario.mostrar_balance_usuario()
        return self


adrien = usuario("Adrien")
nibbles = usuario("Mr Nibbles")
benny_bob = usuario("Benny Bob")

adrien.hacer_deposito(100).hacer_deposito(200).hacer_deposito(50).hacer_retiro(45).mostrar_balance_usuario()
nibbles.hacer_deposito(500).hacer_deposito(500).hacer_deposito(300).hacer_retiro(100).mostrar_balance_usuario()
benny_bob.hacer_deposito(1500).hacer_retiro(1000).hacer_retiro(5000).hacer_retiro(3000).mostrar_balance_usuario()

nibbles.transferir_dinero(400, adrien)
