from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__ (self, nome, CPF, email,endereco):
        Funcionario.__init__(self,nome,CPF,email,endereco)
        self.adicional=500
        
    def setCargaHorariaMensal(self):
        Funcionario.setCargaHorariaMensal(self, 160)
                    
    def calculaSalario(self):
        self.salario=(self.CHMensal*20)+self.adicional

    def __str__ (self):
        return """Cargo:\t\t{}\nNome:\t\t{}\nCPF:\t\t{}\nIdade:\t\t{}\nE-mail:\t\t{}\nEndereço:\t{}\nCarga Horaria:\t{}\nSalario:\tR${}\n\n""".format("Gerente", self.nome, self.CPF, self.idade, self.email, self.endereco, self.CHMensal, self.salario)
