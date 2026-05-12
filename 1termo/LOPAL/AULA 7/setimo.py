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



# print("Bem-vindo ao Menu:")
# print("Formas de acesso")
# print("Opção 1: Emitir ticket")
# print("Opção 2: Verificar TAG")
# print("Opção 3: Interfone")
# acesso = int(input("Digite o número da opção desejada: "))
# placa = input("Digite a placa do veículo: ")
# modelo = input("Digite a marca e o modelo do carro")


# if acesso == 1:
#     print("Bem-vindo ao shopping")
#     valor_estacionamento = float(input("Digite o valor a ser cobrado por hora: "))
#     hora_de_entrada = float(input("Digite a hora de entrada: "))
#     hora_de_saida = float(input("Digite a hora de saída: "))
#     total_permanencia = hora_de_saida - hora_de_entrada
#     print(f"O tempo de permanência total em horas foi de: {total_permanencia} horas")
#     total_estacionamento = total_permanencia * valor_estacionamento
#     print(f"O valor a ser cobrado foi de {total_estacionamento:.2f}")
#     print("devolver o ticket")
# elif acesso == 2:
#     print("Bem-vindo ao shopping")
#     print(f"O valor cobrado por hora pelo estacionamento é {valor_estacionamento}")
# elif acesso == 3:
#     print("Acionando interfone")
#     print("Bem-vindo ao shopping")
#     print("Liberando acesso pelo Interfone")
#     print("Não esqeuça que sua saída deverá ser realiza também pelo Inteforne")
# else:
#     print("Encerrando sistema.")