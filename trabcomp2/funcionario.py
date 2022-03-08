from datetime import date
class Funcionario:
    def __init__(self, nome, CPF,email,endereco):
        self.nome = nome
        self.CPF= CPF
        self.idade= 0
        self.email= email
        self.endereco =endereco
        self.CHMensal=0
        self.salario=0

    def setCargaHorariaMensal(self,CHMensal):
        CHMensalValidas= {80,160}
        if CHMensal in CHMensalValidas:
            self.CHMensal=CHMensal
        else:
            print("Carga horaria invalida para o cargo")
            
    def calculaSalario(self):
        self.salario=self.CHMensal*20

    def calculaIdade(self,ano,mes,dia):
        ano = (date.today() - date(ano,mes,dia))//365
        self.idade = ano.days
    
                
    def __str__ (self):
        return """Cargo:\t\t{}\nNome:\t\t{}\nCPF:\t\t{}\nIdade:\t\t{}\nE-mail:\t\t{}\nEndereço:\t{}\nCarga Horaria:\t{}\nSalario:\tR${}\n\n""".format("Funcionário", self.nome, str(self.CPF), self.idade, self.email, self.endereco, self.CHMensal, self.salario)


