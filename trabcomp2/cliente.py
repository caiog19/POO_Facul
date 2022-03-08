class Cliente():
    def __init__(self):
        self.type_service=''
        self.nome_c=''
        self.idade_c=0
        self.cpf_c=0
        self.email_c=''

    def verificaCadastro(self):
        #Verifica se existe cadastro
        sn='sn'
        while True:
            try:
                s_n = input('\nJa possui cadastro? S/N ')
                s_n1 = s_n.lower()
                if s_n1 in sn and len(s_n1) == 1:
                    break
                else:
                    print('\n !!!-Responda apenas com S ou N-!!! \n')
            except:
                print('\n Responda com S ou N, \n')
        if s_n1 == 's':
            self.nome_c= 'Fulano Ciclano'
            self.idade_c= 40
            self.cpf_c= 12312312312
            self.email_c= 'fulano@email.com'
            self.clien()
        else:
            self.cadastroClien()


    def cadastroClien(self):
        #Cadastro do Cliente
        print('\n-NOME-\n')
        while True:
            try:
                self.nome_c=input('Digite seu nome: ')
                if self.nome_c != '':
                    break
                else:
                    print('\n!!!-Nome invalido-!!!\n')
            except:
                print('\n!!!-Nome invalido-!!!\n')
        print('\n-IDADE-\n')
        while True:
            try:
                self.idade_c=int(input('Digite seu nome: '))
                if self.idade_c > 0 :
                    break
                else:
                    print('\n!!!-Idade invalido-!!!\n')
            except:
                print('\n!!!-Idade invalido-!!!\n')
        print('\n-CPF-\n')
        while True:
            try:
                self.cpf_c=int(input('Digite seu CPF: '))
                cpf = str(self.cpf_c)
                if len(cpf) == 11 :
                    break
                else:
                    print('\n!!!-CPF invalido-!!!\n')
            except:
                print('\n!!!-CPF invalido-!!!\n')
        print('\n-Email-\n')
        while True:
            try:
                self.email_c=input('Digite seu email: ')
                if self.email_c != '':
                    break
                else:
                    print('\n!!!-Email invalido-!!!\n')
            except:
                print('\n!!!-Email invalido-!!!\n')
        self.clien()

    def clien(self):
        #Escolha do serviço que deseja
        nome= self.nome_c.split()
        text_service=f'\nOlá {nome[0].title()}, qual serviço você procura? \n\n 1-Serviços(Banho, Tosa ou Veterinario) \n 2-Produtos(Brinquedos, Alimentos ...) \n 3-Adoção(...)\n 4-Voltar'
        while True:
            try:
                print(text_service)
                service=int(input('Informe o número do serviço: '))
                
                if service == 1:
                    self.type_service= 'Serviços'
                    print('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
                    break
                elif service == 2:
                    self.type_service= 'Produtos'
                    print('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
                    break
                elif service == 3:
                    self.type_service= 'Adoção'
                    print('\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
                    break
                elif service == 4:
                    self.type_service= 'Encerrar'
                    print('---------Programa Encerrado---------')
                    break
                else:
                    print('\n!!!-Não temos esse serviço-!!!\n')
                    text_service=f'{nome[0].title()}, possuimos apenas estes serviços: \n\n 1-Serviços(Banho, Tosa ou Veterinario) \n 2-Produtos(Brinquedos, Alimentos ...) \n 3-Adoção(...)\n 4-Voltar'
            except ValueError:
                print('\n!!!-Não temos esse serviço-!!!\n')
                text_service=f'{nome[0].title()}, possuimos apenas estes serviços: \n\n 1-Serviços(Banho, Tosa ou Veterinario) \n 2-Produtos(Brinquedos, Alimentos ...) \n 3-Adoção(...)\n 4-Voltar'
    
        
