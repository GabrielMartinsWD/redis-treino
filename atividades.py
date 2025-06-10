import uuid
import json
class Atividades:
    def __init__(self, r):
        self.reddis = r
        self.key = "Atividades"
    def adicionar_atividade(self, nome_atividade, descricao):
        atividade_dados = {
            "nome" : nome_atividade,
            "descricao" : descricao
        }
        atividade_json = json.dumps(atividade_dados)
        self.reddis.rpush(self.key, atividade_json)
    def listar_atividades(self):
        atividades_json = self.reddis.lrange(self.key,0, -1)
        if not atividades_json:
            print("NÃo tem atividades.")
            return []
        atividades = []
        for atv in atividades_json:
            atividades.append(json.loads(atv))
        return atividades
    def remover_atividade(self, nome_atividade):
        atividades_atuais = self.listar_atividades()
        encontrado = False
        for i in atividades_atuais:
            if i.get("nome") == nome_atividade:
                self.reddis.lrem(self.key, 1, json.dumps(atividades_atuais))
                encontrado = True
                break
        if not encontrado:
            print(F'Atividade: {nome_atividade} - Não encontrada')

        

    