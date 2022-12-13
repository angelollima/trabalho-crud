from telas import *
from persistencia import *

def menu():
    Metodos.limparTela()
    print("-------- Sistema de Motos --------")
    print("1 - Cadastrar Moto")
    print("2 - Editar Moto")
    print("3 - Excluir Moto")
    print("4 - Selecionar Moto")
    print("5 - Listar Motos")
    print("6 - Sair")
    print("----------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    return opcao


while True:
    opcao = menu()

    if opcao == 1:
        moto = Metodos.cadastrarMoto()
        criar(moto)
        Metodos.exibirMsg("Moto cadastrada com sucesso!")
    elif opcao == 2:
        moto = Metodos.editarMoto()
        editar(moto)
        Metodos.exibirMsg("Moto editada com sucesso!")
    elif opcao == 3:
        Metodos.limparTela()
        id = Metodos.excluirMoto()
        excluir(id)
        Metodos.exibirMsg("Moto excluída com sucesso!")
    elif opcao == 4:
        id = Metodos.selecionarMoto()
        moto = selecionar(id)
        if moto == None:
            Metodos.exibirMsg("Moto não encontrada!")
        else:
            Metodos.exibirMoto(moto)
            Metodos.travarTela()
    elif opcao == 5:
        motos = selecionar_todos()
        Metodos.exibirMotos(motos)
    elif opcao == 6:
        break