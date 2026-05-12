# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
# programação em Python!".

# print("Bem-vindo ao mundo da programação Python!")

# # Atividade 2: Informações Pessoais
# # Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# # Exemplo de saída:
# # Fulano de Tal
# # 30

# questao1 = input("Qual o seu nome: ")
# questao2 = int(input("Qual a sua idade: "))
# print("Seu nome é:", questao1)
# print("Sua idade é:", questao2)



# # Atividade 3: Calculadora de Soma e Subtração
# # Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# # por 128. Cada resultado deve ser exibido em uma linha separada.
# # ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# # ● Obs: Realize também a mesma situação com variáveis

# # 1:

# (print(135 + 246))
# (print(512 - 128))

# # 2:
# print("Bem-vindo a calculadora de soma e subtração!")
# print("Vamos somar")
# valor1 = float(input("Digite o primeiro número: "))
# valor2 = float(input("Digite o segundo número:"))
# total1 = valor1 + valor2
# print("A soma é:", total1)

# print("Agora vamos subtrair")
# valor3 = float(input("Digite o primeiro número: "))
# valor4 = float(input("Digite o segundo número: "))
# total2 = valor3 - valor4
# print("A subtração é: ", total2)


# # Atividade 4: Multiplicação e Divisão
# # Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# # divisão de 78 por 3.
# # 1:
# (print(15 * 8))
# (print(78 / 3))

# print("Bem-vindo a calculadora de multiplicação e divisão!")
# print("Vamos multiplicar")
# valor1 = float(input("Digite o primeiro número: "))
# valor2 = float(input("Digite o segundo número: "))
# total1 = valor1 * valor2
# print("O produto é: ", total1)

# print("Agora vamos dividir (distribuição igualitária)")
# valor3 = float(input("Digite o primeiro número: "))
# valor4 = float(input("Digite o segundo número: "))
# total2 = valor3 / valor4
# print("A divisão é: ", total2)

# # Atividade 5: Potenciação
# # Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# # ● Dica: O operador de potenciação em Python é **.

# (print(5 ** 3))

# # Atividade 6: Concatenando Palavras
# # Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# # o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# # ● Exemplo: print("Maria" + " " + "Silva")


# q1 = input("Qual seu primeiro nome: ")
# q2 = input("Qual seu sobrenome: ")
# print("Seu nome: " + q1 + " Seu sobrenome: " + q2)

# # Atividade 7: Cálculo de Eficiência (OEE)
# # ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# # e exiba a taxa de aproveitamento (peças boas / total).

# qtdeproduzida = int(input("Qual foi a quantidade de peças produzidas: "))
# qtdedefeituosas = int(input("Qual a quantidade de peças defeituosas: "))
# qtdepecasboas = qtdeproduzida - qtdedefeituosas
# taxadaproveitamento = qtdepecasboas / qtdeproduzida
# print("A taxa de aproveitamento é: ", taxadaproveitamento)

# #Atividade 8: Descrição com Cálculos
# # Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# # "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# # ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# # ● Ex: print("Texto", 25 + 10).

# idade = int(input("Idade:")
# print("Eu tenho", idade , "e em 10 anos terei", idade + 10 ,"anos.")

# # Atividade 9: Orçamento de Viagem (Cálculo com float)
# # Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# # o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# # ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

# print("Planejamento da viagem:")
# custo_hotel = float(input("Qual o custo do hotel?"))
# custo_passagem = float(input("Qual o preço da passagem? "))
# noites = int(input("Quantas noites? "))
# total = (custo_hotel * noites) + custo_passagem
# print("O custo total da viagem será de:" , total )

# # Atividade 10: Desafio - Mini Relatório
# # Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# # saída de forma organizada.
# # ● Exemplo de saída:

# # ==========================
# # Relatório de Vendas
# # ==========================
# # Produto: Notebook Gamer
# # Quantidade vendida: 15
# # Preço unitário: R$ 5499.50
# # Total de vendas: R$ 82492.50
# # ==========================


# produto = input("Produto: ")
# QtdeVendida = int(input("Quantidade vendida: "))
# precounitario = float(input("Qual o preço unitário: "))
# TotaldeVendas = QtdeVendida * precounitario
# print("==========================")
# print("Relatório de Vendas")
# print("==========================")
# print("Produto: " , produto )
# print("Quantidade vendida: " , QtdeVendida )
# print("Preço unitário: " , precounitario )
# print("Total de vendas: " , TotaldeVendas )
# print("==========================")
