from abc import ABC, abstractmethod, abstractproperty


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def __str__(self):
        return f"{self.__class__.__name__}: {", ". join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    @classmethod
    def nova_conta(cls, cliente, numero):
        #logica...
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        valor = self._saldo
        #logica... return true return false
        
    def depositar(self, valor):
        #logica...return true return false
        self._saldo += valor
    


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    #sobrescrita do metodo sacar
    def sacar(self, valor):
        #logica com os limites... super().sacar(valor)
        pass
    
    def __str__(self):
        return f"""
    """

class Historico():
    def __init__(self):
        self._transacoes = []
        pass

        @property
        def transacoes(self):
            return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            
        })


class Cliente:
    def __init__(self, endereco, contas) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super.__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ". join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"    


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
       self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
       self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


