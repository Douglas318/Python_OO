class Programa:
    def __init__(self, nome, ano,):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f' Nome: {self.nome}, Ano: {self.likes}'


class Filme (Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - Duração: {self.duracao} min - Likes: {self.likes} Likes'
class Serie (Programa):
     def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

     def __str__(self):
        return f'Nome: {self.nome} - Temporadas: {self.temporadas} Temp. - Likes: {self.likes} Likes'

class Playlist:
      def __init__(self, nome, programas):
          self.nome = nome
          self._programas = programas

      def __getitem__(self, item):
          return self._programas[item]

      def __len__(self):
          return len(self._programas)

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
demolidor = Serie("Demolidor", 2018, 2)
tdmp = Filme("todo mundo em pânico", 1998, 160)

vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tdmp.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

lista = vingadores, atlanta, demolidor, tdmp
minha_playlist = Playlist('fim de semana', lista)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho da minha Playlist: {len(minha_playlist)}')

pass




