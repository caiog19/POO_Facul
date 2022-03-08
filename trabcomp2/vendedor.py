from funcionario import Funcionario

class Vendedor (Funcionario):
    
    def __init__ (self, nome, CPF, email,endereco):
        Funcionario.__init__(self,nome,CPF,email,endereco)
        self.valorVendas=0
         
    def registraVenda(self,valorVenda):
        self.valorVendas=self.valorVendas+valorVenda
        
    def calculaSalario(self):
        self.salario=(self.CHMensal*20)+(self.valorVendas*0.05)

    def __str__ (self):
        return """Cargo:\t\t{}\nNome:\t\t{}\nCPF:\t\t{}\nIdade:\t\t{}\nE-mail:\t\t{}\nEndereço:\t{}\nCarga Horaria:\t{}\nSalario:\tR${}\n\n""".format("Vendedor", self.nome, self.CPF, self.idade, self.email, self.endereco, self.CHMensal, self.salario)
