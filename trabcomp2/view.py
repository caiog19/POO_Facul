from cliente import Cliente
from adocao import Adocao
from viewFuncionario import viewFuncionario
from servico import Servico
from produto import Produto
class View(Cliente, Adocao, Servico, Produto):
    def __init__(self):
        Cliente.__init__(self)
        Adocao.__init__(self)
        Servico.__init__(self)
        Produto.__init__(self)
        self.position = ''
        self.ser_or_fun=0
        self.reg=0
        self.valorF=0
        


        
    
    def view(self):
        print('\n-Bem vindo a Pet Shop-\n')
        self.cli_fun()

        # Classe Funcionario / Registro de Contratos
        if self.position == 'Funcionário':
            self.ani_ser_pro()
            if self.ser_or_fun == 1:
                self.escolha_con()
                if self.reg == 1:#Registrar animal
                    self.registrarAnimal()
                    exit(self.view())
                    self.view()
                elif self.reg == 2:#Registrar serviço
                    self.cadastroServico()
                    exit(self.view())
                    self.view()
                elif self.reg == 3:#Regsitrar produto
                    self.registraProduto()
                    exit(self.view())
                    self.view()
            else:
                viewFuncionario().menuFuncionario()
                exit(self.view())
                self.view()
            

        # Classe Cliente / Contratos
        if self.position == 'Cliente':
            self.verificaCadastro()
            if self.type_service == 'Serviços':
                # Função Compra de Serviços entra aqui!!!
                while self.type_service == 'Serviços':
                    self.meuServicos()
                    self.clien()
                
            if self.type_service == 'Produtos':
                # Função Compra de Produtos entra aqui!!!
                while self.type_service == 'Produtos':
                    self.escolhaProduto()
                    self.clien()
                
            if self.type_service == 'Adoção':
                while self.type_service == 'Adoção':
                    self.menu()
                    self.clien()
                
            if self.type_service == 'Encerrar':
                self.carrinho()
                exit(self.view())
                exit(self.clien())
                self.view()
            
                
            
        if self.position == 'fim':
            print('-----------Fim do Programa-----------')
            pass
        
    def cli_fun(self):
        while True:
            try:
                position = int(input('Voce é:\n 0-Encerrar\n 1-Funcionario \n 2-Cliente \nInforme o número da posição: '))
                if position == 1:
                    self.position= 'Funcionário'
                    break
                elif position == 2:
                    self.position = 'Cliente'
                    break
                elif position == 0:
                    self.position = 'fim'
                    break
                else:
                    print('Número Invalido')
                
            except ValueError:
                print('Posição invalidada')

    def ani_ser_pro(self):
        print('\nQuer fazer o que?')
        print(' 1-Gerenciar os tipos de contratos.')
        print(' 2-Gerenciar os funcionarios.')
        while True:
            try:
                a=int(input('Informe o número: '))
                if a == 1 or a == 2:
                    break
                else:
                    print('\nNumero Invalido\n')
            except:
                print('\nInforme apenas números.\n')
        if a == 1:
            self.ser_or_fun=1
        elif a== 2:
            self.ser_or_fun=2

    def escolha_con(self):
        print('\nO que deseja:')
        print(' 1-Registrar animal para adoçao.')
        print(' 2-Registrar um novo serviço.')
        print(' 3-Registrar um novo produto.')
        while True:
            try:
                a=int(input('Informe o número: '))
                if a == 1 or a == 2 or a==3:
                    break
                else:
                    print('\nNumero Invalido\n')
            except:
                print('\nInforme apenas números.\n')
        if a == 1:
            self.reg=1
        elif a== 2:
            self.reg=2
        elif a== 3:
            self.reg=3

    def carrinho(self):
        print('\n==== Carrinho ====\n')
        print('Serviços Escolhidos:\n')
        if len(self.servicoEs) != 0:
            for x in range(len(self.servicoEs)):
                print(f' {x+1}-{self.servicoEs[x][0]} - R${self.servicoEs[x][1]} - {self.servicoEs[x][2]}')
        else:
            print('\nNenhum serviço escolhido')
        print('\nProdutos Escolhidos:\n')
        if len(self.produtoEs) != 0:
            for y in range(len(self.produtoEs)):
                print(f' {y+1}-{self.produtoEs[y][0]} - R${self.produtoEs[y][1]}')
        else:
            print('\nNenhum produto escolhido')
        print('\nAnimais adotados:')
        if len(self.adotados)!=0:
            for z in range(len(self.adotados)):
                print(f'{z+1} - Animal: {self.adotados[z][4]} / Raça: {self.adotados[z][0]} / Peso: {self.adotados[z][1]} / Idade: {self.adotados[z][2]} / Nome: {self.adotados[z][3]}')
        else:
            print('\nNenhum animal adotado')
        for x1 in range(len(self.servicoEs)):
            self.valorF+=self.servicoEs[x1][1]
        for y1 in range(len(self.produtoEs)):
            self.valorF+=self.produtoEs[y1][1]
        if len(self.adotados) != 0:
            print('\nPor você ter adotado um animal ou mais, ganhou um desconto de 20%')
            valor = self.valorF 
            self.valorF = self.valorF*0.8
            print(f'Desconto, de R${valor} foi para R${self.valorF}')
        print(f'\nValor Da compra: R${self.valorF}')
        print('\n==== Fim do Carrinho ====')



    def __str__(self):
        if self.position == 'funcionario':
            return f'Posição: {self.position} Cargo: {self.post}'
        else:
            return f'Posição: {self.position} Serviço: {self.type_service}'


    
        
a=View()
a.view()
                
