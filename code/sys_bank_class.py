from abc import ABC, abstractmethod

class Conta: 
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico(transacoes_cliente)
        
    def __str__(self):
        return f"{self.__class__.__name__}: {", ". join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
    def mostrar_saldo(self):
        print("Mostrando saldo...")
        print("Saldo de 1000 reais")
        pass
    
    def criar_conta(self):
        cliente = Cliente(end_cliente, contas_cliente)
        numero = 12345
        print("Criando conta...")
        print(f"As informações da sua conta são: {Conta}")
        pass
    
    def sacar(self):
        pass
    
    def depositar(self):
        pass
    
class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques):
        self.limite = limite
        self.limite_saques = limite_saques
    
class Historico():
    def __init__(self, adicionar_transacao):
        self.adicionar_transacao = adicionar_transacao
        
class Cliente:
    def __init__(self, endereco, contas) -> None:
        self.endereco = endereco
        self.contas = contas
    
    def realizar_transacao(self, conta, transacao):
        pass
    
    def adicionar_conta(self,conta):
        pass
    
class PessoaFisica():
    def __init__(self, cpf, nome, data_nascimento) -> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    pass

class Saque(Transacao):
    pass

end_cliente = "Rua 3"
contas_cliente = "1"

transacoes_cliente = "retirou 1 real"