# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"
# print(" Perfil do Gamer")
# nick = input("Qual é o nome do jogador? ... ")
# nivel = int(input("Digite seu nível atual: "))
# print(f"O jogador {nick} está no nível {nivel} e pronto para a partida!")


# # 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# # multiplique por 4 para mostrar quanto ele terá no final do mês.
# print("Calculadora de Mesada")
# valor_semana = float(input("Quanto você ganha por semana? ..."))
# total = valor_semana * 4
# print(f"Sua mesada no fim do mês foi deserá de... {total}")


# # 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# # Megabytes (MB) (multiplique por 1024).
# print("Conversor de internet")
# gigi = float(input("Digite o valor em Gigabytes: "))
# meg = gigi * 1024 
# print(f"O resultado em Megabytes é: {meg}")

# # 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# # média final.
# print("Média das Notas")
# mat = float(input("Digite sua nota de Matemática: "))
# port = float(input("Digite sua nota de Português: "))
# media = (mat + port) / 2
# print(f"Sua média de Matemática e Português... {media}")

# # 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# # o aluno ganhou hoje. Exiba o total atualizado.
# print("Seguidores")
# seg_atual = int(input("Quantos seguidores você possui? "))
# seg_novos = int(input("Quantos novos voc~e ganhou? "))
# seg_atualizado = seg_atual + seg_novos
# print(f"Você possui {seg_atualizado} um total atualizado de seguidores!")

# # 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# # ele já viveu (idade * 365).
# print("Idade em Dias")
# idade = int(input("Digite sua idade: "))
# idade_dias = idade * 365
# print(f"A quantidade de dias vividos são {idade_dias}")

# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.
# print("Consumo do Lanche")
# salgado = float(input("Qual é o valor do salgado? "))
# suco = float(input("Qual é o valor do suco? "))
# total = salgado + suco
# print(f"Sua compra ficou no valor de {total:.2f}")
# print("Sua compra ficou no total de...", round(total,2))

# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.
# anoatual = int(input("Qual o ano atual: "))
# idade = int(input("Quantos anos você fez o fará no ano atual: "))
# anodenascimento = anoatual - idade
# print(f"Você nasceu em: {anodenascimento}")

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".
# print("Bem-vindo ao TikTok!")
# idade = int(input("Qual a sua idade: "))
# if idade < 13:
#     print("Acesso restrito!")
# elif idade in range(13, 18):
#     print("Acesso moderado.")
# elif 13 < idade < 17:
#     print("Acesso Moderado").
# elif idade >= 18:
#     print("Acesso liberado.")
# else:
#     print("idade inválida")


# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".


# print("Bateria")
# print("ততততত")
# import time

# bateria = 100

# while bateria >= 10:
#  print(f"Bateria em: {bateria}%")
#  bateria = bateria - 10 #bateria =- 10
#  time.sleep(1)
# print("Por favor, conecte o carregador!")

# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".
# import time

# limite = int(input("Digite a quantidade de curtidas: "))

# for curtidas in range(1, limite + 1):
#     print(f"♥ Curtida n° {curtidas} recebida!")
#     time.sleep(0.5)

    
# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).

# contador = 0

# produto = 0

# while produto != "sair":
#     contador = contador + 1
#     produto = input("Digite o nome do produto (ou sair, para finalizar): ")
# print(f"Você adicionou {contador - 1} itens ao carrinho")


# contador = 0

# produto = ""

# while produto.lower() != "sair":
#     produto = input("Digite o nome do produto (ou sair, para finalizar): ")
#     contador += 1
#     if produto.lower() != "sair":
#         print(f"Produto '{produto}' adicionado ao carrinho!")
# print(f"Você adicionou {contador - 1} itens ao carrinho")

# print("Obrigado por comprar conosco")
