import inicial
import os

contas = []

while True:
    os.system('cls')
    print('_________________________________________________________')
    print('==================== SISTEMA BANCÁRIO====================')
    print('_________________________________________________________')
    print('1 - CADASTRAR CONTA')
    print('2 - SACAR')
    print('3 - DEPOSITAR')
    print('4 - BUSCAR CONTA')
    print('5 - EXCLUIR CONTA')
    print('6 - EDITAR CONTA')
    print('7 - TRANSFERIR')
    print('0 - SAIR')
    print('_________________________________________________________')
    
    opcao = input('Qual opção você desja ')
    print('_________________________________________________________')
    

    if opcao == '0':
        os.system('cls')
        break
    elif opcao == '1':
        numero_conta = input('Numero da Conta: ')
        nome_titular = input('Seu nome: ')
        tipo_conta = input('Tipo de Conta:(corrente ou poupança) ')
        saldo_inicial = float(input('Qual valor incial para iniciar sua conta '))
        contas = inicial.cadastrar_conta(contas, numero_conta, nome_titular, tipo_conta, saldo_inicial)
    elif opcao == '2':
        numero_conta = input('Número da sua Conta: ')
        valor_saque = float(input('Quanto deseja sacar: '))
        inicial.sacar(contas, numero_conta, valor_saque)
    elif opcao == '3':
        numero_conta = input('Número da Conta: ')
        valor_deposito = float(input('Quanto deseja Depósitar '))
        inicial.depositar(contas, numero_conta, valor_deposito)
    elif opcao == '4':
        chave_busca = input('Digite o numeros da conta ou seu nome: ')
        resultado = inicial.buscar_conta(contas, chave_busca)
        print(resultado)
    elif opcao == '5':
        numero_conta = input('Digite o numero da conta conta que dseja excluir ')
        contas = inicial.excluir_conta(contas, numero_conta)
    elif opcao == '6':
        numero_conta = input('Numero da Conta que deseja editar: ')
        novo_nome_titular = input('Novo Nome do usuario: ')
        novo_tipo_conta = input('Novo Tipo de Conta:(corrente ou poupança) ')
        inicial.editar_conta(contas, numero_conta, novo_nome_titular, novo_tipo_conta)
    elif opcao == '7':
        conta_origem = input('Numero da sua conta ')
        conta_destino = input('Numero da Conta para qual dseja transferir ')
        valor_transferencia = float(input('Valor da Transferência: '))
        inicial.transferir(contas, conta_origem, conta_destino, valor_transferencia)
    else:
        print('OPÇÃO INVALIDA!')

print('PROGRAMA ENCERRADO')


