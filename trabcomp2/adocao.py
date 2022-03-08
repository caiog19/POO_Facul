class Adocao:
        
    def __init__(self):
        self.caes=[['Shitsu','8','12','Joy'],['Labrador','12','6','Sun']]
        self.gatos=[['Perça','4','5','Perciana'],['Siames','3','7','Siano']]
        self.hamsters=[['Russo','2','5','Russiano'],['Indiano','1','9','India']]
        self.adotados=[]

        

    def menu(self):
        """ """
        while True:
            try:
                opt=int(input("Informe o que deseja fazer:\n 1-Adotar um animal\n 2-Sair\nInforme apenas o número: "))
                if opt==1:
                    self.adotar()
                elif opt==2:
                    break
                else:
                    print('\nNumero Invalido\n')
                    
            except:
                print("!!!Digite apenas números!!!")
        print('\nAnimais adotados:')
        for x in range(len(self.adotados)):
            print(f'{x+1} - Animal: {self.adotados[x][4]} / Raça: {self.adotados[x][0]} / Peso: {self.adotados[x][1]} / Idade: {self.adotados[x][2]} / Nome: {self.adotados[x][3]}')
                    
    def adotar(self):
        """Função Main"""
        while True:
            try:
                qual_animal= int(input('\nQual animal vc deseja adotar:\n 1-Cão\n 2-Gato\n 3-Hamster\n 4-Sair para o menu\nInforme o número:'))
                if qual_animal==1:
                    self.adotarCao()
                    break
                elif qual_animal==2:
                    self.adotarGato()
                    break
                elif qual_animal==3:
                    self.adotarHamster()
                    break
                elif qual_animal==4:
                    print("\nVoltando para o menu...\n")
                    break
                else:
                    print('\n!!!-Não temos esse animal-!!!\n')
            except:
                print('\n!!!-Digite apenas números-!!!')
        

    def adotarCao(self):
        """Função que põe os cachorros na lista de adotados e remove os mesmos"""
        if len(self.caes)>0:
            print('\nTemos estes cachorros disponiveis para a adoção:\n')
            for x in range(len(self.caes)):
                print(f'{x+1} - Raça: {self.caes[x][0]} Peso: {self.caes[x][1]} Idade: {self.caes[x][2]} Nome: {self.caes[x][3]}')
            while True:
                try:
                    qual=int(input('\nQual desses você deseja:'))
                    if qual<=len(self.caes) and qual>=0:
                        print(f'\nVoce escolheu {self.caes[qual-1]}\n')
                        break
                    else:
                        print('!!!-Número invalido-!!!')
                except:
                    print('\n!!!-Digite apenas números-!!!')
            self.caes[qual-1].append('Cachorro')
            self.adotados.append(self.caes[qual-1])
            self.caes.pop(qual-1)
        else:
            print('\nNão possuimos nenhum cachorro para adoção!\n')
                    

    def adotarGato(self):
        """Função que põe os gatos na lista de adotados e remove os mesmos"""
        if len(self.gatos)>0:
            print('\nTemos estes gatos disponiveis para a adoção:\n')
            for x in range(len(self.gatos)):
                print(f'{x+1} - Raça: {self.gatos[x][0]} Peso: {self.gatos[x][1]} Idade: {self.gatos[x][2]} Nome: {self.gatos[x][3]}')
            while True:
                try:
                    qual=int(input('\nQual desses você deseja:'))
                    if qual<=len(self.gatos) and qual>=0:
                        print(f'\nVoce escolheu {self.gatos[qual-1]}\n')
                        break
                    else:
                        print('!!!-Número invalido-!!!')
                except:
                    print('\n!!!-Digite apenas números-!!!')
            self.gatos[qual-1].append('Gato')
            self.adotados.append(self.gatos[qual-1])
            self.gatos.pop(qual-1)
        else:
            print('\nNão possuimos nenhum gato para adoção!\n')

    def adotarHamster(self):
        """Função que põe os hamsters na lista de adotados e remove os mesmos"""
        if len(self.hamsters)>0:
            print('\nTemos estes hamsters disponiveis para a adoção:\n')
            for x in range(len(self.hamsters)):
                print(f'{x+1} - Raça: {self.hamsters[x][0]} Peso: {self.hamsters[x][1]} Idade: {self.hamsters[x][2]} Nome: {self.hamsters[x][3]}')
            while True:
                try:
                    qual=int(input('\nQual desses você deseja:'))
                    if qual<=len(self.hamsters) and qual>=0:
                        print(f'\nVoce escolheu {self.hamsters[qual-1]}\n')
                        break
                    else:
                        print('!!!-Número invalido-!!!')
                except:
                    print('\n!!!-Digite apenas números-!!!')
                
            self.hamsters[qual-1].append('Hamster')
            self.adotados.append(self.hamsters[qual-1])
            self.hamsters.pop(qual-1)
        else:
            print('\nNão possuimos nenhum hamster para adoção!\n')
            
    def registrarAnimal(self):
        """Função para adicionar animais na lista de adoção"""
        #Qual animal add
        
        
        while True:
            try:
                opt_anm= int(input('Qual animal você quer registrar:\n 1-Cachorro\n 2-Gato\n 3-Hamster\n 4-Voltar para o menu!'))
                if opt_anm==1:
                    animal=self.infosAni()
                    self.caes.append(animal)
                    break
                elif opt_anm==2:
                    animal=self.infosAni()
                    self.gatos.append(animal)
                    break
                elif opt_anm==3:
                    animal=self.infosAni()
                    self.hamsters.append(animal)
                    break
                elif opt_anm==4:
                    
                    break
                else:
                    print('!!!-Número Inválido-!!!')
            except:
                print('!!!-Digite apenas números-!!!')
    def infosAni(self):
        #raça peso idade nome
        infos=[]
        while True:
            try:
                raca = input('Qual a raça do animal:')
                break
            except:
                print('!!!-Incorreto-!!!')
        infos.append(raca)
        while True:
            try:
                peso = input('Qual o peso do animal:')
                break
            except:
                print('!!!-Incorreto-!!!')
        infos.append(peso)
        while True:
            try:
                idade = input('Qual a idade do animal:')
                break
            except:
                print('!!!-Incorreto-!!!')
        infos.append(idade)
        while True:
            try:
                nome = input('Qual a nome do animal:')
                break
            except:
                print('!!!-Incorreto-!!!')
        infos.append(nome)
        return infos
            
       

