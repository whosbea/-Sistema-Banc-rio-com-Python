menu = """
[0] Sair
[1] Depósito
[2] Saque
[3] Extrato
"""
saldo = 1000
depositos = []
saques = []
qnt_saque = 0

def escolher_acao():
    while True:    
        acao = int(input(f"{menu}\n"))

        match acao:
            case 0:
                break
            case 1:
                depositar()
            case 2:
                sacar()
            case 3:
                exibir_extrato()

def depositar():
    global saldo
    
    deposito = float(input(f"Quanto deseja depositar ? \nR$ "))
    
    if deposito > 0:
        saldo = saldo + deposito
        print(f"Você depositou R$ {deposito:.2f}. Seu saldo atual é R$ {saldo:.2f}")
        depositos.append(f"R$ {deposito:.2f}")
    else:
        print("Valor inválido.")
        
#permite realizar 3 saques diários com limite de 500 por saque    
def sacar():
    global saldo, qnt_saque
    
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
        
def exibir_extrato():
    global saldo, depositos, saques
    
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

       
if __name__ == "__main__":
    escolher_acao()

