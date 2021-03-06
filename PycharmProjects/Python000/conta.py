class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo da sua conta é {}".format(self.__saldo))

    def deposita(self, valor):
        self.__saldo +=valor

    def __pode_sacar(self, valor_para_sacar):
        valor_disponivel = self.__saldo + self.limite
        return valor_para_sacar <= valor_disponivel


    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print("Valor de {} autorizado".format(valor))
        else:
            print('Saque de {} não autorizado'.format(valor))

    def transfere(self, valor, destino):
       self.saca(valor)
       destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
         self.__limite = limite

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Nubank": "241", "Caixa": "104"}

    pass
