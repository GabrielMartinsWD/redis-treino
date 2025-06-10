
class Ranking:
    def __init__(self, redis_conn, key='ranking_jogadores'):
        self.redis = redis_conn
        self.key = key

    def adicionar_ou_atualizar_jogador(self, nome: str, pontuacao: float):
        self.redis.zadd(self.key, {nome: pontuacao})
        print(f'Jogador {nome} registrado/atualizado com pontuação de {pontuacao}.')
    def listar_top_5(self):
        top5 = self.redis.zrevrange(self.key, 0, 4, withscores=True)
        print("🏆 Top 5 Jogadores:")
        for i, (nome, pontuacao) in enumerate(top5, start=1):
            print(f"{i}. {nome} - {pontuacao}")