from funcionario import Funcionario
from gerente import Gerente
from vendedor import Vendedor
from veterinario import Veterinario

class viewFuncionario():
    def __init__(self):
        self.funcionarios=[]
        
#Início das Funções do menu Funcionário
                
    def menuFuncionario(self):
        while True:
            try:
                print("\n\n==== Módulo Funcionários ====\n\n")
                print("1-Incluir Funcionário")
                print("2-Definir Carga Horária")
                print("3-Consultar Funcionário")
                print("4-Sair")
                print("\n\n")

                opt=int(input("Escolha a opção desejada:"))

                if(opt==1):
                    self.incluirFuncionario()       
                if(opt==2):
                    self.definirCargaHoraria()             
                if(opt==3):
                    self.consultarFuncionario()
                if(opt==4):
                    break
                if(opt>4 or opt<1):
                    print("Opção inválida")        
            except ValueError:
                print("Opção inválida")
        print("Programa encerrado")

    def incluirFuncionario(self):
        self.funcionarios.clear()
        print("\n\n====== Inclusão de Funcionário ======\n\n")
        nome=input("Nome: ")
        cpf=input("CPF: ")
        email=input("e-mail: ")
        Dnas=input("Data de Nascimento (dd/mm/aaaa): ")
        endereco=input("Endereço: ")
        while True:
            print("\nCargo:\n")
            print("1-Funcionário")
            print("2-Gerente")
            print("3-Veterinario")
            print("4-Vendedor")
            cargo=int(input("Escolha a opção desejada:"))
            if(cargo==1):
                funcionario = Funcionario(nome,cpf,email,endereco)
                funcionario.calculaIdade(int(Dnas[6:]),int(Dnas[3:5]),int(Dnas[0:2]))
                break
            elif(cargo==2):
                funcionario=Gerente(nome,cpf,email,endereco)
                funcionario.calculaIdade(int(Dnas[6:]),int(Dnas[3:5]),int(Dnas[0:2]))
                break
            elif(cargo==3):
                crmv=input("imforme o CRMV do veterinário: ")
                funcionario=Veterinario(nome,cpf,email,endereco)
                funcionario.calculaIdade(int(Dnas[6:]),int(Dnas[3:5]),int(Dnas[0:2]))
                funcionario.crmv(crmv)
                break
            elif(cargo==4):
                funcionario=Vendedor(nome,cpf,email,endereco)
                funcionario.calculaIdade(int(Dnas[6:]),int(Dnas[3:5]),int(Dnas[0:2]))
                break
            else:
                print("Cargo inválido")

        while True:
            confirma = input("\n\nConfirma Inclusão do Funcionário? (S/N): ")
            if confirma=="S":
                if cargo == 3:
                    baseFunci=open("funcionarios.txt","a")
                    linha=str(cargo)+";"+funcionario.CPF+";"+funcionario.nome+";"+funcionario.email+";"+str(funcionario.idade)+";"+funcionario.endereco+";0;"+funcionario.CRMV+";\n"
                    baseFunci.write(linha)
                    baseFunci.close()
                    print("\nFuncionário incluído com sucesso")
                    break
                else:
                    baseFunci=open("funcionarios.txt","a")
                    linha=str(cargo)+";"+funcionario.CPF+";"+funcionario.nome+";"+funcionario.email+";"+str(funcionario.idade)+";"+funcionario.endereco+";"+"0;\n"
                    baseFunci.write(linha)
                    baseFunci.close()
                    print("\nFuncionário incluído com sucesso")
                    break
            elif confirma=="N":
                print("\nInclusão cancelada")
                break
            else:
                print("\nOpção inválida!")
                
    def definirCargaHoraria(self):
        print("\n\n==== Definir Carga Horária ====\n\n")
        self.recuperarFuncionarios()
        i=0
        for funcionario in self.funcionarios:
            i=i+1
            print(i," ",funcionario.CPF," ",funcionario.nome," ",funcionario.CHMensal)        
        
        if(i>0):
            opt=int(input("\n\nInforme o numero do funcionario: "))
            if(opt>=1 and opt<=i):         
                funcionario=self.funcionarios.pop(opt-1)
                if(isinstance(funcionario, Gerente) or isinstance(funcionario, Veterinario)):
                    funcionario.setCargaHorariaMensal()
                else:
                    ch=int(input("\n\nInforme a carga horária do funcionário (80/160): "))
                    funcionario.setCargaHorariaMensal(ch)
                self.funcionarios.append(funcionario)
                while(True):
                    confirma=input("\n\nConfirma alteração da carga horária? (S/N): ")
                    if confirma=='S':
                        self.updateFuncionarios()
                        print("\nCarga horária atualizada com sucesso")
                        break
                    else:
                        if confirma=='N':
                            print("\nAlteração cancelada")
                            break
                        else:
                            print("\nOpção inválida!")
            else:
                print("Numero inválido")
                
    def consultarFuncionario(self):
        print("\n\n==== Consultar Funcionário ====\n\n")
        self.recuperarFuncionarios()
        i=0
        for funcionario in self.funcionarios:
            i=i+1
            funcionario.calculaSalario()
            print(i," ",funcionario.CPF," ",funcionario.nome," ",funcionario.CHMensal)        
        
        if(i>0):
            opt=int(input("\n\nInforme o numero do funcionario: "))
            if(opt>=1 and opt<=i):         
                funcionario=self.funcionarios.pop(opt-1)
                print(funcionario)
            else:
                print("Numero inválido")

    def recuperarFuncionarios(self):
        self.funcionarios.clear()
        try:
            baseFunci= open('funcionarios.txt','r')
            cargo=0
            for line in baseFunci:
                pos=pos_old=0
                i=0
                funci=[]
                while True:
                    try:
                        pos=line.index(";",pos_old)
                        funci.append(line[pos_old:pos])
                        pos_old=pos+1
                    except ValueError:
                        break        
                try:
                    cargo = funci.pop(0)
                    cpf = funci.pop(0)
                    nome = funci.pop(0)
                    email = funci.pop(0)
                    idade = funci.pop(0)
                    endereco = funci.pop(0)
                    ch = funci.pop(0)
                    if(cargo=='1'):
                        funcionario=Funcionario(nome,cpf,email,endereco)
                        if(ch!='0'):
                            funcionario.setCargaHorariaMensal(int(ch))
                    if(cargo=='2'):
                        funcionario=Gerente(nome,cpf,email,endereco)
                        if(ch!='0'):
                            funcionario.setCargaHorariaMensal()
                    if(cargo=="3"):
                        funcionario=Veterinario(nome,cpf,email,endereco)
                        crmv = funci.pop(0)
                        funcionario.crmv(crmv)
                        if(ch!="0"):
                            funcionario.setCargaHorariaMensal()
                    if(cargo=='4'):
                        funcionario=Vendedor(nome,cpf,email,endereco)
                        if(ch!='0'):
                            funcionario.setCargaHorariaMensal(int(ch))
                    self.funcionarios.append(funcionario)
                    funcionario.idade=idade
                except IndexError:
                    baseFunci.close()  
                    break
            baseFunci.close()  
        except IOError:
            print("Problemas para acessar a base de funcionários!")


    def updateFuncionarios(self):
        try:
            baseFunci= open('funcionarios.txt','w')
            baseFunci.close()
            baseFunci= open('funcionarios.txt','w')
            for funcionario in self.funcionarios:
                if isinstance(funcionario,Funcionario):
                    cargo='1'
                if isinstance(funcionario,Gerente):
                    cargo='2'
                if isinstance(funcionario,Veterinario):
                    cargo="3"
                if isinstance(funcionario,Vendedor):
                    cargo='4'         
                linha=cargo+";"+funcionario.CPF+";"+funcionario.nome+";"+funcionario.email+";"+funcionario.idade+";"+funcionario.endereco+";"+str(funcionario.CHMensal)+";"
                if cargo=="3":
                    linha+=funcionario.CRMV+";"
                linha+="\n"
                baseFunci.write(linha)         
            baseFunci.close()
        except IOError:
            print("Problemas para acessar a base de funcionários!")

#Final das Funções do menu Funcionário
