# inicial.py
def cadastrar_conta(lista_contas, numero_conta, nome_titular, tipo_conta, saldo_inicial):
    conta = {
        'numero_conta': numero_conta,
        'nome_titular': nome_titular,
        'tipo_conta': tipo_conta,
        'saldo': saldo_inicial
    }
    lista_contas.append(conta)
    return lista_contas

def sacar(lista_contas, numero_conta, valor_saque):
    for conta in lista_contas:
        if conta['numero_conta'] == numero_conta:
            if conta['saldo'] >= valor_saque:
                conta['saldo'] -= valor_saque
                print('Saque realizado!')
                return True
            else:
                print("Você não possui saldo suficiente!")
                return False
    print("Conta não encontrada!")
    return False

def depositar(lista_contas, numero_conta, valor_deposito): 
    for conta in lista_contas:
        if conta['numero_conta'] == numero_conta:
            conta['saldo'] += valor_deposito
            print('Valor depositado com sucesso!')
            return True
    print("Conta não encontrada!")
    return False

def buscar_conta(lista_contas, chave):
    resultado = []
    for conta in lista_contas:
        if str(conta['numero_conta']).count(chave) > 0 or conta['nome_titular'].count(chave) > 0:
            resultado.append(conta)
    return resultado

def excluir_conta(lista_contas, numero_conta):
    nova_lista_contas = [] #cria uma nova lista para armazenar sem o usuario 
    conta_encontrada = False # começa como falso, caso seja true será excluida 

    for conta in lista_contas: #percorre a lista 
        if conta['numero_conta'] == numero_conta:# se o numero da conta for igual a um existente 
            conta_encontrada = True 
        else:
            nova_lista_contas.append(conta)

    if conta_encontrada: # se for true
        print(f"Conta {numero_conta} conta excluida com sucesso!")
        return nova_lista_contas # retorna o valor para a lista nova 
    else:
        print("Conta não encontrada!")
        return lista_contas  

def editar_conta(lista_contas, numero_conta, novo_nome_titular, novo_tipo_conta):
    for conta in lista_contas:
        if conta['numero_conta'] == numero_conta:
            conta['nome_titular'] = novo_nome_titular
            conta['tipo_conta'] = novo_tipo_conta
            print('conta editada com sucesso!')
            return True
    print("Conta não encontrada!")
    return False

def transferir(lista_contas, conta_origem, conta_destino, valor_transferencia):
    if sacar(lista_contas, conta_origem, valor_transferencia):#verifica se é possivel sacar chamando a função  sacar
        depositar(lista_contas, conta_destino, valor_transferencia)  #adiciona o valor a conta destino
        print('Transferência realizada com sucesso!')
        return True
