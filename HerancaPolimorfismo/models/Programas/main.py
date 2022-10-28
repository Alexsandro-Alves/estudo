from HerancaPolimorfismo.models.Programas.filme import Filme
from HerancaPolimorfismo.models.Programas.playlist import Playlist
from HerancaPolimorfismo.models.Programas.serie import Serie

if __name__ == '__main__':

    vikings = Serie('Vikings', 2013, 6)
    zumbilandia = Filme('Zumbilandia', '2010', 120)
    tmep = Filme('Todo mundo em pânico', 1999, 100)
    demolidor = Serie('Demolidor', 2016, 2)

    vikings.dar_like()
    zumbilandia.dar_like()
    zumbilandia.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    tmep.dar_like()
    demolidor.dar_like()
    demolidor.dar_like()
    vikings.dar_like()
    vikings.dar_like()
    vikings.dar_like()

    lista_de_programas = [vikings, zumbilandia, tmep, demolidor]
    playlist = Playlist('Filmes e Séries', lista_de_programas)
    print(f'Tamanho da playlist -  {len(playlist)}')

    for programa in playlist:
        print(programa)
