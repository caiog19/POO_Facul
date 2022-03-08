class Servico:
    def __init__(self):
        self.servicos=[['Tosa',100,'Funcionário'],['Banho',50,'Funcionário'],['Consulta',150,'Veterinário']]
        self.servicoEs=[]

    def meuServicos(self):
        while True:
            try:
                print("\n\n==== Escolha o Módulo ====\n\n")
                print(" 1-Escolher servicos")
                print(" 0-Sair\n")
                opt=int(input("Escolha a opção desejada:"))

                if (opt == 1):
                    self.escolhaServico()
                if (opt == 0):
                    break
                
            except ValueError:
                    print("\nOpção inválida")
        
        if len(self.servicoEs)>0:
            print('\nServiços Escolhidos:\n')
            for x in range(len(self.servicoEs)):
                print(f' {x+1}-{self.servicoEs[x][0]} - R${self.servicoEs[x][1]} - {self.servicoEs[x][2]}')
        else:
            print('\nNenhum serviço escolhido!\n')

    def cadastroServico (self):
        servico=[]
        #tipo
        while True:
            try:
                tipo=input('Qual o nome do serviço novo:')
                break
            except:
                print('\n!!!-Nome Invalido-!!!\n')
        servico.append(tipo)
        #Valor
        while True:
            try:
                valor = int(input('Valor do serviços:'))
                break
            except:
                print('\n!!!-Valor Invalido-!!!\n')
        servico.append(valor)
        #Quem faz
        print('Quem faz o serviço:')
        print(' 1-Funcionário')
        print(' 2-Veterinário')
        while True:
            try:
                quem=int(input('Informe o número:'))
                if quem == 1:
                    servico.append('Funcionário')
                    break
                elif quem == 2:
                    servico.append('Veterinário')
                    break
                else:
                    print('\n!!!-Valor Errado-!!!\n')
            except:
                print('\n!!!-Digite apenas números-!!!\n')
        self.servicos.append(servico)
        
        
            

    def escolhaServico(self):

        print("\n\n==== Consultar Servicos ====\n\n") 
        

        for x in range(len(self.servicos)):
            print(f' {x+1}-{self.servicos[x][0]} - R${self.servicos[x][1]} - {self.servicos[x][2]}')
        while True:
            try:
                escolha = int(input('\nInforme o número do serviço:'))
                escolha-=1
                if escolha <len(self.servicos) and escolha>=0:
                    self.servicoEs.append(self.servicos[escolha])
                    break
                else:
                    print('\n!!!-Não possuimos este serviço-!!!\n')
            except:
                print('\n!!!-Não possuimos este serviço-!!!\n')

    def __str__(self):
        return """Servico: \t\t{}\nFuncionario responsavel: \t\t{}\nValor: \t\tR${}\n\n""".format(self.nomeServico, self.funcionarioResponsavel, self.valorUni)

