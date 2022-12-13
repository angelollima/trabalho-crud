import json
import os.path

nome_arquivo = 'dados.json'

class JsonStorage:
    def lerJson(self):
        if not os.path.isfile(nome_arquivo):
            JsonStorage.criarArquivo()

        arq = open(nome_arquivo, 'r', encoding='utf-8')
        data = arq.read()

        if len(data) == 0:
            return []

        data = json.loads(data)
        arq.close()

        return data


    def gravarJson(self, dados):
        arq = open(nome_arquivo, 'w+', encoding='utf-8')
        data = json.dumps(dados, indent=4)
        arq.write(data)
        arq.close()


    def criarArquivo(self):
        arq = open(nome_arquivo, 'w+', encoding='utf-8')
        arq.close()