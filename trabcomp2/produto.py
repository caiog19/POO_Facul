class Produto:
    def __init__(self):
        self.produtos=[['Shampoo',50],['Ração',100]]
        self.produtoEs=[]

    def meusProdutos(self):
        while True:
            try:
                print('\n==== Escolha o Módulo ====\n')
                print(' 1-Escolher Produto')
                print(' 0-Sair\n')
                opt = int(input('Escolha a opção desejada: '))
                if opt ==1:
                    self.escolhaProduto()
                elif opt == 0:
                    break
                else:
                    print ("\nOpção invalida")
            except ValueError:
                    print("\nOpção inválida")

        if len(self.produtoEs)>0:
            print('\nServiços Escolhidos:\n')
            for x in range(len(self.produtoEs)):
                print(f' {x+1}-Produto: {self.produtoEs[x][0]} - R${self.produtoEs[x][1]}')
        else:
            print('\nNenhum serviço escolhido!\n')

    def escolhaProduto(self):
        print('\n==== Escolha de Produtos ====\n')
        for x in range(len(self.produtos)):
            print(f' {x+1}-Produto: {self.produtos[x][0]} - R${self.produtos[x][1]}')
        while True:
            try:
                escolha = int(input('\nInforme o número do produto: '))
                escolha-=1
                if escolha <len(self.produtos) and escolha>=0:
                    self.produtoEs.append(self.produtos[escolha])
                    break
                else:
                    print('\n!!!-Não possuimos este produto-!!!\n')
            except:
                print('\n!!!-Não possuimos este produto-!!!\n')

    def registraProduto(self):
        produto=[]
        while True:
            try:
                tipo=input('Qual o nome do produto novo: ')
                break
            except:
                print('\n!!!-Nome Invalido-!!!\n')
        produto.append(tipo)
        while True:
            try:
                valor = int(input('Valor do produto: '))
                break
            except:
                print('\n!!!-Valor Invalido-!!!\n')
        produto.append(valor)
        self.produtos.append(produto)

    
