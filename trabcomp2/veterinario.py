from funcionario import Funcionario

class Veterinario(Funcionario):
    def __init__ (self, nome, CPF, email,endereco):
        Funcionario.__init__(self,nome,CPF,email,endereco)
        self.CRMV = 0
        
    def setCargaHorariaMensal(self):
        Funcionario.setCargaHorariaMensal(self, 160)

    def crmv(self,crmv):
        self.CRMV = crmv
                    
    def calculaSalario(self):
        self.salario=(self.CHMensal*50)

    def __str__ (self):
        return """Cargo:\t\t{}\nNome:\t\t{}\nCPF:\t\t{}\nCRMV:\t\t{}\nIdade:\t\t{}\nE-mail:\t\t{}\nEndereço:\t{}\nCarga Horaria:\t{}\nSalario:\tR${}\n\n""".format("Veterinário", self.nome, self.CPF, self.CRMV, self.idade, self.email, self.endereco, self.CHMensal, self.salario)
