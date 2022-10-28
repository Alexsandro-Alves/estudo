from typing import Dict


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self) -> None:
        print(f'Saldo da conta {self.__saldo}')

    def deposita(self, valor) -> None:
        self.__saldo += valor

    # Métodos que não devem ou não serão usados fora da própria classe devem ser privados
    # basta colocar __ antes do nome
    def __pode_sacar(self, valor_a_sacar) -> bool:
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor) -> None:
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'Saldo insuficiente!')

    def transfere(self, valor, destino) -> None:
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def titular(self) -> str:
        return self.__titular

    # Retornar de forma correta o valor de um atributo da classe
    @property
    def limite(self) -> float:
        return self.__limite

    # Atribuir de forma correta o valor a um atributo da classe
    @limite.setter
    def limite(self, limite) -> None:
        self.__limite = limite

    # Métodos estáticos retornam algo sem que precise criar uma instancia da classe
    # Para chamar ele basta chamar a classe Conta.codigo_banco() e obterá seu valor de retorno
    @staticmethod
    def codigo_banco() -> str:
        return '001'

    @staticmethod
    def codigos_bancos() -> Dict[str, str]:
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}




