from abc import ABC, abstractmethod, abstractproperty


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
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

        if valor > self._saldo:
            print(f"\nOperação inválida, você não tem saldo suficiente. Saldo atual: R${self._saldo:.2f}")

        elif valor > 0:
            self._saldo -= valor
            print("\nSacando...")
            print(f"\nSaque no valor de R${valor:.2f} realizado com sucesso!")
            return True

        else:
            print("\nValor inválido, tente novamente.")

        return False

    def depositar(self, valor):

        if valor < 0:
            print("\nValor inválido, tente novamente.")

        else:
            self._saldo += valor
            print("\nDepositando...")
            print(f"\nDeposito no valor de R${valor:.2f} realizado com sucesso!")
            return True

        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico._transacoes if transacao["tipo"] == Saque.__name__])
        if self.limite_saques >= numero_saques:
            if valor <= 500:
                super().sacar(valor)
            else:
                print("Valor superior ao limite por saque, por favor tente novamente.")
        else:
            print("Limite de saques diarios atingidos.")

        return False

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
    """


class Historico():
    def __init__(self):
        self._transacoes = []
        pass

        @property
        def transacoes(self):
            return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )


class Cliente:
    def __init__(self, endereco, contas) -> None:
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco, contas)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


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


def menu():
    menu = """
        [0] Sair
        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Cadastrar Usuario
        [5] Criar Conta Corrente
        [6] Listar contas\n
    """

    return int(input(menu))


def criar_cliente(clientes):
    cpf = str(input("Digite seu cpf: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        nome = str(input('Digite seu nome completo: '))
        data_nascimento = str(
            input('Digite sua data de nascimento (dd/mm/aaaa): '))
        endereco = str(
            input("Digite seu endereço (rua, numero - bairro - cidade/sigla estado):"))

        cliente = PessoaFisica(
            nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
        clientes.append(cliente)

        print(f"\nCadastro realizado com sucesso {nome}, agora crie sua conta no banco.")
    else:
        print("\nJa existe um cliente cadastrado com esse cpf!")


def criar_conta(numero_conta, clientes, contas):
    cpf = str(input("Digite o cpf do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\nCliente não encontrado, operação encerrada.')
    else:
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta)

        print('\nConta corrente criada com sucesso.')


def listar_contas(contas):
    print('Lista de contas'.center(45, '-'))
    for conta in contas:
        print(conta)
    print('-'*45)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = []
    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes_filtrados.append(cliente)
    return clientes_filtrados[0] if clientes_filtrados else None
# retorna o cliente se ele ja existir, se não retorna "None"


def resgatar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nO cliente não tem uma conta neste banco.")
        return
    return cliente.contas[0]


def depositar(clientes):
    cpf = str(input("Digite o cpf do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nO cliente não é cadastrado nesse banco.")
        return
    else:
        conta = resgatar_conta_cliente(cliente)

        if not conta:
            return
        else:
            valor = float(input("Qual valor do deposito? R$"))
            transacao = Deposito(valor)
            cliente.realizar_transacao(conta, transacao)
        return


def sacar(clientes):
    cpf = str(input("Digite o cpf do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nO cliente não tem uma conta neste banco.")
        return

    valor = float(input("Qual valor do saque? R$"))
    transacao = Saque(valor)

    conta = resgatar_conta_cliente(cliente)

    if not conta:
        return
    else:
        cliente.realizar_transacao(conta, transacao)
        return


def exibir_extrato(clientes):
    cpf = str(input("Digite o cpf do cliente: "))
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nO cliente não tem uma conta neste banco.")
        return

    conta = resgatar_conta_cliente(cliente)

    if not conta:
        return
    else:
        transacoes = conta.historico._transacoes
        print('Extrato'.center(27, "-"))

        if not transacoes:
            return print(f"\nNão foram feitas transações.\nSeu saldo é de R${conta.saldo:.2f}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            for transacao in transacoes:
                print(f"{transacao['tipo']} de R${transacao['valor']:.2f}")

    print(f"\nSeu saldo é de R${conta.saldo:.2f}")
    print("-"*27)


if __name__ == "__main__":
    clientes = []
    contas = []

    while True:
        opcao = menu()

        match opcao:
            case 0:
                break
            case 1:
                depositar(clientes=clientes)
            case 2:
                sacar(clientes=clientes)
            case 3:
                exibir_extrato(clientes=clientes)
            case 4:
                criar_cliente(clientes=clientes)
            case 5:
                numero_conta = len(contas) + 1
                criar_conta(numero_conta=numero_conta,
                            clientes=clientes, contas=contas)
            case 6:
                listar_contas(contas=contas)
