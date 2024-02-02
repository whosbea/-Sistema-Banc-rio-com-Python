import random

menu = """
[0] Sair
[1] Depósito
[2] Saque
[3] Extrato
[4] Cadastrar Usuario
[5] Criar Conta Corrente
"""
saldo = 1000
depositos = []
saques = []
qnt_saque = 0
usuarios = [
    ['09077673199', 'Beatriz', '19/09/2004', 'Rua das Clareiras, 67 - Bairro Morros - Teresina/PI'],
    ['08854693779', 'Pedro', '10/04/2008', 'Rua das Clareiras, 67 - Bairro Morros - Teresina/PI'],
    ['78987543530', 'Iris', '27/07/1940', 'Av Universitaria, 309 - Bairro Ininga - Teresina/PI']
]
contas = [
    {"Usuario": "09077673199", "Agencia": "0001", "Numero da Conta": [155, 123]},
    {"Usuario": "08854693779", "Agencia": "0001", "Numero da Conta": [156]},
    {"Usuario": "78987543530", "Agencia": "0001", "Numero da Conta": [187, 174, 145]}
]

def escolher_acao():
    while True:    
        acao = int(input(f"{menu}\n"))

        match acao:
            case 0:
                break
            case 1:
                depositar(saldo, depositos)
            case 2:
                sacar(qnt_saque=qnt_saque, saldo=saldo,saques=saques)
            case 3:
                exibir_extrato(saldo, depositos=depositos, saques=saques)
            case 4:
                cadastrar_usuario(usuarios)
            case 5: 
                cadastrar_conta(contas)

def depositar(saldo, depositos):
    deposito = float(input(f"Quanto deseja depositar ? \nR$ "))
    
    if deposito > 0:
        saldo = saldo + deposito
        print(f"Você depositou R$ {deposito:.2f}. Seu saldo atual é R$ {saldo:.2f}")
        depositos.append(f"R$ {deposito:.2f}")
    else:
        print("Valor inválido.")
        
    return saldo, depositos
        
#Permite realizar 3 saques diários com limite de 500 por saque    
def sacar(qnt_saque, saldo, saques):
    if qnt_saque < 3:
        saque = float(input(f"O saldo disponivel é R$ {saldo:.2f}. Quanto deseja sacar? \nR$ "))
        if saldo >= saque:
            if saque > 500:
                print(f"Seu limite de saque é R$ 500.00, tente um valor menor.")   
            else:
                saldo = saldo - saque
                print(f"Você sacou R$ {saque:.2f}, o saldo atual é R$ {saldo:.2f}")
                saques.append(f"R$ {saque:.2f}")
                qnt_saque += 1   
        elif saldo < saque:
            print(f"Seu saldo é insuficiente.")
        else:
            print("Valor inválido")  
    else:
        print("Seu limite de saques diários foi atingido.")
    
    return saldo, saques, qnt_saque
        
def exibir_extrato(saldo, depositos, saques):  
    lista_depositos = "\n".join(depositos)
    lista_saques = "\n".join(saques)
    
    print("Depositos feitos:\n")
    if len(depositos) == 0:
        print("Não foram realizadas movimentações.\n")
    elif len(depositos) >= 1:
        print(lista_depositos, "\n")
    
    print("Saques feitos:\n")
    if len(saques) == 0:
        print("Não foram realizadas movimentações.\n")
    elif len(saques) >=1:
        print(lista_saques, "\n")

    print(f"Saldo atual: R$ {saldo:.2f}")


def cadastrar_usuario(usuarios):
    cpf_existe = False
    cpf = input("Digite seu CPF (formato: 00000000000):\n")
    
    for usuario in usuarios:
        if usuario[0] == cpf:
            print("CPF já cadastrado.")
            cpf_existe = True
            break
    
    if not cpf_existe:
        user = [cpf]
        nome = input("Digite seu nome:\n")
        user.append(nome)  
        data_nascimento = input("Digite sua data de nascimento (formato: DD/MM/AAAA):\n")
        user.append(data_nascimento)
        endereco = input("Digite seu endereço (formato: logradouro, numero - bairro - cidade/sigla estado):\n")
        user.append(endereco)
        
        usuarios.append(user)
        nova_conta = {"Usuario": cpf, "Agencia": "001", "Numero da Conta": []}
        contas.append(nova_conta)
        print(f"Usuário cadastrado com sucesso.\n{user}")
    
    return usuarios
    

def cadastrar_conta(contas):
    usuario_existe = False
    usuario = input("Digite seu usuario (Cpf):")
    # agencia = "0001"
    
    while True:
        num_conta = gerar_num_conta(contas)
        
        if num_conta is not None:
            # print(f"Número gerado e verificado: {num_conta}")
            break

    for conta in contas:
        if conta["Usuario"] == usuario:
            usuario_existe = True
            opcao = input(f"Usuario ja existe:\n{conta}\n\nDeseja criar uma nova conta?\n[S]- Sim\n[N]- Não\n")
            opcao = opcao.upper()
            match opcao:
                case "S":
                    # modelo_dict_conta = {"Usuario": usuario, "Agencia": agencia, "Numero da Conta": num_conta}
                    conta["Numero da Conta"].append(num_conta)
                    print(f"Conta criada com sucesso, o numero da sua nova conta é {num_conta}.")
                
                case "N":
                    break
    
    if not usuario_existe:
        print("O usuario ainda não existe, por favor cadastre seu usuário.")
        cadastrar_usuario(usuarios)
    
def gerar_num_conta(contas):
    #Usar o random pra gerar um numero de conta aleatorio não existente
    num_conta = random.randint(100,200)
    # print("Número gerado:", num_conta)
    
    for conta in contas:
        lista_num_conta = conta["Numero da Conta"]
        # print("Lista de números da conta:", lista_num_conta)
        
        for num in lista_num_conta:
            if num == num_conta:
                # print("O número já existe. Gerando um novo número.")
                return None  # Retorna None para indicar que um novo número deve ser gerado
    
    return num_conta

if __name__ == "__main__":
    escolher_acao()

