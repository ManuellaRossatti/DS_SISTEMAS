#Projeto cancela automática

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.

# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código


while True:
    print("Bem-vindo ao Menu:")
    print("Formas de acesso")
    print("Opção 1: Emitir ticket")
    print("Opção 2: Verificar TAG")
    print("Opção 3: Interfone")
    print("Opção 4: Relatório")
    acesso = int(input("Digite o número da opção desejada: "))
    placa = input("Digite a placa do veículo: ")
    modelo = input("Digite a marca e o modelo do carro: ")

    relatorio_veiculos = []
    valor_por_hora_padrao = 15.00 
    #ENTRADA 
    if acesso == 1:
        print("Bem-vindo ao shopping")
        valor_estacionamento = float(input("Digite o valor a ser cobrado por hora: "))
        hora_de_entrada = float(input("Digite a hora de entrada: "))
        hora_de_saida = float(input("Digite a hora de saída: "))
        total_permanencia = hora_de_saida - hora_de_entrada
        print(f"O tempo de permanência total em horas foi de: {total_permanencia} horas")
        total_estacionamento = total_permanencia * valor_estacionamento
        print(f"O valor a ser cobrado foi de {total_estacionamento:.2f}")
        print("devolver o ticket")
    elif acesso == 2:
        print("Bem-vindo ao shopping")
        if placa:
            print(f"TAG Identificada: O valor será gerado na fatura.")
    elif acesso == 3:
        print("Acionando interfone")
        print("Bem-vindo ao shopping")
        print("Liberando acesso pelo Interfone")
        print("Não esqeuça que sua saída deverá ser realiza também pelo Interfone")
    elif acesso == 4:
        print("\n--- RELATÓRIO DE MOVIMENTAÇÃO ---")
        print("Nenhum veículo registrado até o momento.")
        print(f"Placa: {placa} | Modelo: {modelo} | Tempo:{total_permanencia} horas | Valor: R$ {valor_estacionamento}")
    else:
        print("Encerrando sistema.")
    
    

