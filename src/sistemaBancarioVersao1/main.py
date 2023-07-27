MENU = ["Sair","Deposito","Saque","Extrato"]

saldo = 0
extrato = []
limite = 0
LIMITE_DIARIO = 3
LIMITE_SAQUE = 500

while True:
    opcao = int(input("""
        Olá usuário!
    
        Escolha uma dentre as opções abaixo
              
        0 - [Sair]
        1 - [Deposito]
        2 - [Saque]
        3 - [Extrato]                              
              
        """))
    
    if opcao < 0 or opcao > 3:
        print("Operação encerrada. Tente novamente.\n")
    elif MENU[opcao] == "Sair":
        print("\nObrigado por utilizar nossos serviços, até outro dia!")
        break
    elif MENU[opcao] == "Deposito":
        while True:
            deposito = float(input("Digite o valor que deseja depositar: "))
            if deposito > 0:
                saldo += deposito
                extrato.append(f"Deposito: R$ {deposito: .2f}")
                print("\nDeposito realizado com sucesso!")
                break
                
            print("Valor inválido!")
    elif MENU[opcao] == "Saque":
        if saldo > 0:
            saque = float(input("Digite o valor de saque: "))
            if saque <= saldo and saque <= LIMITE_SAQUE and limite < LIMITE_DIARIO:
                saldo -= saque
                print("Saque realizado com sucesso!")
                limite += 1
                extrato.append(f"Saque: R$ {saque: .2f}")
            else:
                if saque >= saldo:
                   print("O saldo é menor que o saque solicitado.")
                elif saque > LIMITE_SAQUE:
                    print("Saque maior que o limite de R$500,00 por saque.")
                elif limite == LIMITE_DIARIO:
                    print("Desculpe, mas você atingiu o limite de saques diarios. Tente outra operação.")
        else:
            print("Você não possui saldo para saque. Realize depósitos antes.")
        continue
    elif MENU[opcao] == "Extrato":
        if extrato != []:
            for i in extrato:
                print(i)
            print(f"Saldo atual da conta é de R$ {saldo: .2f}")
        else:
            print("Nao foram realizadas movimentações")
    
      