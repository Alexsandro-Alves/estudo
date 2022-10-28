from HerancaPolimorfismo.models.Funcionario.alura import Alura
from HerancaPolimorfismo.models.Funcionario.caelum import Caelum


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass


jose = Junior()
jose.busca_perguntas_sem_resposta()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()
