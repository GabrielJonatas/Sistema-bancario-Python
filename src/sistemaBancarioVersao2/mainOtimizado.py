MENU = ["Sair","Criar usuário","Criar conta","Entrar na conta","Deposito","Saque","Extrato"]

saldo = []
extrato = []
limite = []
LIMITE_DIARIO = 3
LIMITE_SAQUE = 500
usuarios = {}
contas = {}
contadorUsuario = 0
contadorConta = 0

def saque (*, saldo, extrato, limite, LIMITE_SAQUE, LIMITE_DIARIO):
    if saldo > 0:
        saque = float(input("Digite o valor de saque: "))
        if saque <= saldo and saque <= LIMITE_SAQUE and limite < LIMITE_DIARIO:
            saldoFinal = saldo - saque
            print("Saque realizado com sucesso!")
            limiteFinal = limite + 1
            extratoFinal = extrato
            extratoFinal.append(f"Saque: R$ {saque: .2f}")
            return (saldoFinal, limiteFinal, extratoFinal)
        else:
            if saque >= saldo:
                print("O saldo é menor que o saque solicitado.")
            elif saque > LIMITE_SAQUE:
                print("Saque maior que o limite de R$500,00 por saque.")
            elif limite == LIMITE_DIARIO:
                print("Desculpe, mas você atingiu o limite de saques diarios. Tente outra operação.")
            return (saldo, limite, extrato)
    else:
        print("Você não possui saldo para saque. Realize depósitos antes.")
        return (saldo, limite, extrato)

def deposito (saldo, extrato):
    while True:
            deposito = float(input("Digite o valor que deseja depositar: "))
            if deposito > 0:
                saldoFinal = saldo + deposito
                extratoFinal = extrato
                extratoFinal.append(f"Deposito: R$ {deposito: .2f}")
                print("\nDeposito realizado com sucesso!")
                return (saldoFinal, extratoFinal)
            else:
                print("Operação encerrada. Tente novamente.\n")
                return (saldo, extrato)

def historico (saldo, /, *, extrato):
    if extrato != []:
            for i in extrato:
                print(i)
            print(f"saldo atual da conta é de R$ {saldo: .2f}")
    else:
        print("Nao foram realizadas movimentações")
        print(f"saldo atual da conta é de R$ {saldo: .2f}")

def criarConta(contadorConta, usuario):
    return {
        f"Conta {contadorConta}": {"agencia": "0001", "Número da conta": f"{contadorConta+1}", "Usuário": usuario
        }}

def criarUsuario(contadorUsuario,nome,dataNascimento,cpf,numero,bairro,cidade,siglaEstado):
    return {
        f"Usuario {contadorUsuario}": {"nome": nome, "data de nascimento": dataNascimento, "CPF": cpf, 
        "logradouro": {"número": numero, "bairro": bairro, "cidade":cidade,"Sigla Estado": siglaEstado},
        }}

while True:
    opcao = int(input("""
        Olá usuário!
    
        Escolha uma dentre as opções abaixo
            
        0 - [Sair]              
        1 - [Criar usuário]
        2 - [Criar conta]
        3 - [Entrar na conta]                              
              
        """))
    
    if opcao < 0 or opcao > 3:
        print("Operação encerrada. Tente novamente.\n")
    elif MENU[opcao] == "Sair":
        print("\nObrigado por utilizar nossos serviços, até outro dia!")
        break
    elif MENU[opcao] == "Criar usuário":
        nome = input("Digite seu nome: ")
        dataNascimento = input("Digite data de nascimento: ")
        cpf = input("Digite seu CPF")
        numero = input("Digite seu número: ")
        bairro = input("Digite seu bairro: ")
        cidade = input("Digite sua cidade: ")
        estado = input("Digite seu estado/sigla: ")
        while True:
            i = True
            for chave in usuarios:
                if (cpf == usuarios[chave].get("CPF", {})):
                    i = False
                    break
            if (i):
                usuarios.update(criarUsuario(contadorUsuario, nome, dataNascimento, cpf, numero, bairro, cidade, estado))
                contadorUsuario += 1
                print("usuario criado com sucesso!")
                break
            else:
                print("Usuario já existe!")
                break
    elif MENU[opcao] == "Criar conta":
        usuario = input("Digite seu CPF: ")
        while True:
            j = True
            for chave in usuarios:
                if (usuario == usuarios[chave].get("CPF", {})):
                    contas.update(criarConta(contadorConta, chave))
                    j = False
                    contadorConta += 1
                    saldo.append(0)
                    extrato.append([])
                    limite.append(0)
                    print("Conta criada com sucesso!")
                    break
            if (j):
                print("Usuário informado não existe, crie seu usuário primeiro.")
            break
    elif MENU[opcao] == "Entrar na conta":
        conta = input("Digite o numero da sua conta:")
        cpf = input("Digite seu CPF: ")
        m = False
        for chave in contas:
                if (conta == contas[chave].get("Número da conta", {})):
                    for segredo in usuarios:
                        if (cpf == usuarios[segredo].get("CPF", {})):
                            m = True
                    break
        if (m):
            while True:
                opcao = int(input("""
                    Olá usuário!
                
                    Escolha uma dentre as opções abaixo
                          
                    0 - [Sair]
                    4 - [Deposito]
                    5 - [Saque]
                    6 - [Extrato]                              
                          
                    """))
                
                if opcao < 0 or (0 < opcao and opcao < 4) or opcao > 6:
                    print("Operação encerrada. Tente novamente.\n")
                elif MENU[opcao] == "Sair":
                    print("\nObrigado por utilizar nossos serviços, até outro dia!")
                    break
                elif MENU[opcao] == "Deposito":
                    depositar = deposito(saldo[int(conta)-1], extrato[int(conta)-1])
                    saldo[int(conta)-1] = depositar[0]
                    extrato[int(conta)-1] = depositar[1] 
                elif MENU[opcao] == "Saque":
                    sacar = saque(saldo = saldo[int(conta)-1], extrato = extrato[int(conta)-1], limite = limite[int(conta)-1], LIMITE_SAQUE = LIMITE_SAQUE, LIMITE_DIARIO = LIMITE_DIARIO)
                    saldo[int(conta)-1] = sacar[0]
                    limite[int(conta)-1] = sacar[1]
                    extrato[int(conta)-1] = sacar[2]
                elif MENU[opcao] == "Extrato":
                    historico(saldo[int(conta)-1], extrato=extrato[int(conta)-1])
        else:
            print("Conta não existente ou CPF digitado incorretamente. Caso não tenha uma conta, crie uma por favor!")
