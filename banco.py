menu = """"

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo+= valor
            extrato += f"deposito : R$ {valor:.2f}\n"

        else:
            print("operação invalida")

    elif opcao == "2":
        valor = float(input("informe o valor do saque"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite
    
        excedeu_saque = numero_saques >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficente.")

        elif excedeu_limite:
            print("operação falho! o valor do saque excede o limite.") 

        elif excedeu_saque:
            print("operação falhou! numero máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque R$ {valor: .2f}\n"
            numero_saques +=1
        
        else:
            print("operação falhou!o valor informado é invalido")

    elif opcao == "3":
        print("======== extrato ==========")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"saldo R$ {saldo: .2f}")
        print("============================")


    elif opcao == "4":
        break

    else:
        print("operação invalida, por favor selecione novamente alguma operação")