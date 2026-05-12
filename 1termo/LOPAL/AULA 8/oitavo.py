# Exercícios de Programação Python: "O Caça-Erros"

# 1. O Problema da Idade
# Errado:
# idade = input("Digite sua idade")
# if idade >= 18:
#     print("Você é maior de idade")

# # Corrigido:
# idade = int(input("Digite sua idade"))
# if idade >= 18:
#     print("Você é maior de idade.")


# # Melhorado:
# print("--------------------------------------------------")
# print("    Bem-vindo ao site de apostas de Las Vegas")
# print("--------------------------------------------------")
# print("Por favor, informe sua idade para que possamos começar seu cadastro!")
# idade_do_usuario = int(input("Digite aqui sua idade: "))
# if idade_do_usuario >= 18:
#     print("Você é maior de idade.")
#     print("Acesso permitido.")
# elif idade_do_usuario < 18:
#     print("Você é menor de idade.")
#     print("Acesso negado.")
# else:
#     print("Acesso bloqueado")

# 2. A Escrita Fiel
#Errado:
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# Corrigido:
# nome = "Mariana"
# print("Seja bem-vinda,", nome,"!")

# Melhorado:
# print("Olá somos da equipe, MelqLanches felizes, por favor digite seu nome para nos referirmos corretamente a você!")
# nome_do_usuario = input("Digite seu nome aqui: ")
# print(f"Seja bem-vindo/a, {nome_do_usuario}!")
# print("Como podemos lhe ajudar?")

# 3. Falta de Espaço
# Errado:
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# # Corrigido:
# numero = 10
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# # Melhorado:
# print("Números: Maiores ou Menores... São números!")
# print("é maior ou menor que cinco? Eis a questão! \n" \
# "Vamos descobrir juntos!!")
# numero = float(input("Digite um número: "))
# if numero > 5:
#     print("O número é maior que cinco.")
# else:
#     print("O número é menor ou igual a cinco.")

# 4. Esquecimento Fatal
# Errado:
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

# Corrigido:
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

# Melhorado:
# print("Olá, seja bem-vindo ao Melq Livros")
# print("Caso seja aluno faça login como aluno123)\n" \
# "Caso seja professor faça logindo com professor123")
# usuario = input("Por favor digite o seu nome de usuário: ")
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")
# elif usuario == "professor123":
#     print("Login realizado com sucesso.")
# else:
#     print("Login incorreto, por favor tente novamente.")



# 5. Atribuição vs. Comparação
# Errado
# clima = "ensolarado"
# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")

# # Corrigido:
# clima = "chuvoso"
# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")


# # Melhorado:
# print("Planejamento com base no clima")
# print("Clima 1: Ensolarado")
# print("Clima 2: Nublado")
# print("Clima 3: Chuvoso")
# clima = input("Como está o clima hoje? ")
# if clima == "Chuvoso":
#     print("Leve um guarda-chuva!")
# elif clima == "Ensolarado":
#     print("Leve uma sombrinha para se proteger do sol, e não esqueça de usar protetor solar.")
# elif clima == "Nublado":
#     print("Leve apenas um agasalho.")
# else:
#     print("Sistema encerrado.")

#6. Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# Corrigido: 
# pontos = 50
# print("Parabéns! Você fez +",pontos, "pontos.")

# Melhorado:
# print("Faça login hoje para obter mais 50 pontos meu jovem padawan!")
# login = input("Digite seu nickname: ")
# pontos = 50
# print(f"Parabéns! Jovem padawan {login}")
# print(f"Você acabou de ganhar +{pontos} pontos.")

# 7. A Ordem dos Fatores
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

# Corrigido: 
# nota = 9.5
# if 7 < nota < 9:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

#Melhorado:
# print("Saiba aqui se você foi aporvado!")
# nota = float(input("Digite aqui sua nota: "))
# if nota < 7:
#     print("Reprovado")
# elif 7 < nota < 9:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")


# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
#     print(i)

# Corrigido:
# for i in range(1, 6):
#     print(i)

# Melhorado:
# print("Você sabe como contar até cinco?")
# print("Vamos conta juntos jovem padawan!")
# for i in range(1, 6):
#     print(i)
# print("Agora sim jovem padawan, segure-se porque a nave vai viajar na velocidade da luz!")

# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
# O código deveria parar após 3 tentativas

#Corrigido:
# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas += 1

# Melhorado:
# tentativas = 1
# while tentativas <= 3:
#     print(f"Tentativa {tentativas} de 3...")
#     print("Tentando conectar...")
#     tentativas += 1
# print("Falha na conexão. Tente novamente mais tarde.")


#10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Corrigido:
# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
#     print("Acesso concedido!")

# Melhorado: 
# senha_correta = "python123"
# senha = ""

# while senha != senha_correta:
#     senha = input("Digite a senha secreta: ")
#     if senha != senha_correta:
#         print("Senha incorreta. Tente novamente.")
# print("Acesso concedido! Bem-vindo ao sistema.")



