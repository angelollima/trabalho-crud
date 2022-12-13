import os

class Metodos:
    def cadastrarMoto():
        Metodos.limparTela()
        print("-------- Cadastro de Motos --------")
        moto = {}
        moto['chassi'] = input('Chassi: ')
        moto['marca'] = input('Marca: ')
        moto['cilindrada'] = input('Cilindrada: ')
        moto['cor'] = input('Cor: ')
        moto['pneu'] = input('Pneu: ')

        return moto


    def editarMoto():
        Metodos.limparTela()
        print("-------- Edição de Motos --------")
        moto = {}
        moto['id'] = int(input('Id: '))
        moto['chassi'] = input('Chassi: ')
        moto['marca'] = input('Marca: ')
        moto['cilindrada'] = input('Cilindrada: ')
        moto['cor'] = input('Cor: ')
        moto['pneu'] = input('Pneu: ')
        return moto


    def excluirMoto():
        print("-------- Exclusão de Motos --------")
        Metodos.limparTela()
        id = int(input('Id: '))
        return id


    def selecionarMoto():
        Metodos.limparTela()
        print("-------- Seleção de Motos --------")
        id = int(input('Id: '))
        return id


    def exibirMoto(moto):
        print("-------- Produto --------")
        print(f"Id: {moto['id']}")
        print(f"Chassi: {moto['chassi']}")
        print(f"Marca: {moto['marca']}")
        print(f"Cilindrada: {moto['cilindrada']}")
        print(f"Cor: {moto['cor']}")
        print(f"Pneu: {moto['pneu']}")


    def exibirMotos(motos):
        Metodos.limparTela()
        print("---------------- Motos ----------------")
        for moto in motos:
            Metodos.exibirMoto(moto)
        Metodos.travarTela()


    def limparTela():
        os.system('clear' if os.name == 'posix' else 'cls')


    def travarTela():
        input('Pressione ENTER para continuar...')


    def exibirMsg(msg):
        print(msg)
        Metodos.travarTela()