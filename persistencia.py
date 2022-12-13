from json_storage import *

chamarJsonStorage = JsonStorage()

def criar(dado: dict) -> dict:
    dados = chamarJsonStorage.lerJson()
    dado['id'] = gerarId()
    dados.append(dado)
    chamarJsonStorage.gravarJson(dados)


def editar(dado: dict) -> None:
    dados = chamarJsonStorage.lerJson()
    for i, data in enumerate(dados):
        if data['id'] == dado['id']:
            dados[i] = dado
    chamarJsonStorage.gravarJson(dados)


def excluir(id: int) -> None:
    dados = chamarJsonStorage.lerJson()
    for dado in dados:
        if dado['id'] == id:
            dados.remove(dado)
    chamarJsonStorage.gravarJson(dados)


def selecionar(id: int) -> dict | None:
    dados = chamarJsonStorage.lerJson()
    for dado in dados:
        if dado['id'] == id:
            return dado
    return None


def selecionar_todos() -> list:
    return chamarJsonStorage.lerJson()


def gerarId() -> int:
    dados = chamarJsonStorage.lerJson()
    if len(dados) == 0:
        return 1
    return dados[-1]['id'] + 1