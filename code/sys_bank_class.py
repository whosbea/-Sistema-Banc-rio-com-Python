from abc import ABC, abstractmethod, abstractproperty


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico(transacoes_cliente)

    def __str__(self):
        return f"{self.__class__.__name__}: {", ". join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    def mostrar_saldo(self):
        print("Mostrando saldo...")
        print(f"Saldo de {self.saldo} reais")
        pass

    def criar_conta(self):
        cliente = Cliente(end_cliente, contas_cliente)
        numero = 12345
        print("Criando conta...")
        print(f"As informações da sua conta são: {self}")
        pass

    def sacar(self, valor):
        self.valor = valor
        return True
        

    def depositar(self, valor):
        self.valor = valor
        return True


class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, historico, limite, limite_saques):
        super().__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

    def __str__(self):
        return f"{self.__class__.__name__}: {", ". join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Historico():
    def __init__(self, trasacoes):
        self.transacoes = trasacoes
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ". join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    def adicionar_transacao(self, transacao):
        print("Adicionando transação...")
        print(f"{transacao} adicionada.")


class Cliente:
    def __init__(self, endereco, contas) -> None:
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(self, conta, transacao):
        transacao = input("Qual tipo de transação gostaria de fazer? ")
        conta = input("Para qual conta quer realizar a transação? ")
        
        print(f"Realizando {transacao} para conta {conta}...")
        print(f"{transacao} realizado com sucesso.")

    def adicionar_conta(self, conta):
        conta = input("Qual conta gostaria de adicionar? ")
        
        print(f"Adicionando {conta}...")
        print(f"{conta} adicionada.")


class PessoaFisica():
    def __init__(self, cpf, nome, data_nascimento) -> None:
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ". join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"    


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        self.conta = conta

        print("Registrando transações...")
        print("Transações registradas")
        pass


class Deposito(Transacao):
    @abstractmethod    
    def depositar(self):
        valor = float(input("Quanto deseja depositar? "))

        print("Depositando...")
        print(f"Valor de R${valor:.2f} depositado com sucesso.")


class Saque(Transacao):
    @abstractmethod
    def sacar(self):
        valor = float(input("Quanto deseja sacar? "))

        print("Sacando...")
        print(f"Valor de R${valor:.2f} sacado com sucesso.")


end_cliente = "Rua 3"
contas_cliente = "1"

transacoes_cliente = "retirou 1 real"


cliente1 = Cliente(end_cliente, contas_cliente)
historico_cliente1 = Historico()
cliente1.adicionar_conta(Conta(1000, 1234, "0001", cliente1, historico_cliente1))

transacao_deposito = Deposito()
transacao_deposito.registrar(cliente1.contas[0])
cliente1.contas[0].mostrar_saldo()

transacao_saque = Saque()
transacao_saque.registrar(cliente1.contas[0])
cliente1.contas[0].mostrar_saldo()