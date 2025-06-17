menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f">>> Depósito realizado: R$ {valor:.2f}\n"
            print(extrato)
            print(f">>> Saldo atual: {saldo:.2f}\n")
        else:
            print("Operação falhou! O valor informado é inválido.")
        
    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))
        
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        excedeu_saldo = valor > saldo
        
        if excedeu_limite:
            print(f"Falha! O valor do saque excede o limite permitido de R$ {limite:.2f}.\n")
        elif excedeu_saques:
            print("Número de saques diários excedidos. Não é possível realizar mais saques.")
        elif excedeu_saldo:
            print("Falha! Você não tem saldo suficiente para realizar essa operação.")
            print(f">>> Saldo atual: {saldo:.2f}\n")
        elif valor > 0:
            saldo -= valor
            extrato += f">>> Saque realizado: R$ {valor:.2f}\n"
            numero_saques += 1
            print(extrato)
            print(f">>> Saldo atual: {saldo:.2f}\n")
        else:
            print("Ocorreu um erro ao realizar o saque. Por favor, tente novamente.")
        
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "q":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")