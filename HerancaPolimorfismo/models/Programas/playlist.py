class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # Forma de deixar a classe como iteravel sem precisar herdar de list e comprometer a usabilidade da classe
    # Nesse caso a classe deixa de ser um list e passa a ter uma lista
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    # Se quiser retornar o tamanho de algum objeto da classe de uma forma mais elegante e organizada
    def __len__(self):
        return len(self._programas)