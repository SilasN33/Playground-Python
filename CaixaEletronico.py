from time import sleep

cliente = input("Digite seu nome") 
cpf = input("Digite seu cpf:")
saldo = 0
celular = 0 
sleep(5)
print("Bem vindo" + cliente)
print("CPF:" + cpf)


while True:
    print("Menu de opções:")
    print("1. Consultar saldo")
    print("2. Depositar valor $$")
    print("3. Pix ou Recarga de Celular")
    print("4. Sair")
    opção = input("Escolha uma opção: ")
    if opção == "1":
        print (saldo)
    elif opção == "2":
        quantia = input("Digite a quantia para deposito")
        saldo = int(saldo) + int(quantia)
        print("deposito realizado")
        sleep(2)
        print("SALDO ATUAL  : " + str (saldo))
    elif opção == "3":
        while True:
            print("Menu de opções:")
            print("1. Pix")
            print("2. Recarga Celular")
            print("3. Consultar saldo Celular")
            print("4. Voltar")
            opção = input("Escolha uma opção: ")
            if opção == "1":
                quantia2 = input("Selecione o valor que deseja transferir:")
                saldo = int(saldo) + int(quantia2)
                sleep(2)
                print("SALDO ATUAL : " + str(saldo ))
            elif opção == "2":
                operadora = input("Digite sua operadora")
                sleep(2)
                print("Operadora " + str(operadora))
                sleep (2)
                recarga = input("Informe o valor da recarga :")
                celular = int(celular) + int(recarga)
                sleep(2)
                print("recarga feita com sucesso")
                print("Seu saldo de telefone é :" + str(celular))
            elif opção == "3":
                print("SALDO ATUAL:" + str(celular))
            elif opção == "4":
                break       
    elif opção == "4":
        break
    else:
        print("Opção inválida. Escolha novamente.")