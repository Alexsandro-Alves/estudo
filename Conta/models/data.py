class Data:
    def __init__(self, dia,  mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar_data(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')


data = Data(25, 10, 2022)
data.formatar_data()