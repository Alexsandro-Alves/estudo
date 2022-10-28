from HerancaPolimorfismo.models.Programas.Programa import Programa


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        self.__likes = 0

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min -  {self._likes} Likes'
