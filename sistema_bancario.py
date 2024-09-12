menu = """

[d] Depositar
[s] Sacar
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
        print("Depósito")
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou. O valor informado é inválido")

    elif opcao == "s":
        print("Sacar")
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou. Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou. O valor do saque excede o limite autorizado.")

        elif excedeu_saques:
            print("Operação falhou. Você já realizou a quantidade de saques autorizadas por dia.")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
        
        else:
            print("Operação falhou. O valor informado é inválido.")

    elif opcao == "e":
        print("\n========EXTRATO========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("========================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida. Por favor, selecione novamente a operação desejada.")
