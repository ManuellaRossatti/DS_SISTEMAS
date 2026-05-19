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
registros = []

while True:
    print("Bem-vindo ao Menu:")
    print("Formas de acesso")
    print("Opção 1: Emitir ticket")
    print("Opção 2: Verificar TAG")
    print("Opção 3: Interfone")
    print("Opção 4: Relatório")
    print("Opção 0: Sair")

    try:
        acesso = int(input("Digite o número da opção desejada: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if acesso == 1:
        placa = input("Digite a placa do veículo: ").strip().upper()
        modelo = input("Digite a marca e o modelo do carro: ").strip()
        print("Bem-vindo ao shopping")

        valor_estacionamento = float(input("Digite o valor a ser cobrado por hora: "))
        hora_de_entrada = float(input("Digite a hora de entrada: "))
        hora_de_saida = float(input("Digite a hora de saída: "))

        total_permanencia = hora_de_saida - hora_de_entrada
        total_estacionamento = total_permanencia * valor_estacionamento

        print("O tempo de permanência total em horas foi de:", total_permanencia, "horas")
        print("O valor a ser cobrado foi de:", total_estacionamento)
        print("devolver o ticket")

        registros = registros + [{
            "tipo": "Ticket",
            "placa": placa,
            "modelo": modelo,
            "entrada": hora_de_entrada,
            "saida": hora_de_saida,
            "tempo": total_permanencia,
            "valor": total_estacionamento
        }]

    elif acesso == 2:
        placa = input("Digite a placa do veículo: ").strip().upper()
        modelo = input("Digite a marca e o modelo do carro: ").strip()
        print("Bem-vindo ao shopping")

        # (exemplo) aqui você faria sua validação real da TAG
        print("TAG Identificada: O valor será gerado na fatura.")

        registros = registros + [{
            "tipo": "TAG",
            "placa": placa,
            "modelo": modelo,
            "entrada": "",
            "saida": "",
            "tempo": "",
            "valor": ""
        }]

    elif acesso == 3:
        placa = input("Digite a placa do veículo: ").strip().upper()
        modelo = input("Digite a marca e o modelo do carro: ").strip()
        print("Acionando interfone")
        print("Bem-vindo ao shopping")
        print("Liberando acesso pelo Interfone")
        print("Não esqueça que sua saída deverá ser realizada também pelo Interfone")

        registros = registros + [{
            "tipo": "Interfone",
            "placa": placa,
            "modelo": modelo,
            "entrada": "",
            "saida": "",
            "tempo": "",
            "valor": ""
        }]

    elif acesso == 4:
        print("--- RELATÓRIO DE MOVIMENTAÇÃO ---")
        if not registros:
            print("Nenhum veículo registrado até o momento.")
        else:
            for item in registros:
                print("Tipo:", item["tipo"],
                      "| Placa:", item["placa"],
                      "| Modelo:", item["modelo"],
                      "| Entrada:", item["entrada"],
                      "| Saída:", item["saida"],
                      "| Tempo:", item["tempo"],
                      "| Total: R$", item["valor"])

    elif acesso == 0:
        print("Encerrando sistema.")
        break

    else:
        print("Opção inválida.")
