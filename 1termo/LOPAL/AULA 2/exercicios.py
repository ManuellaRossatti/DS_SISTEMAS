# Exercí­cio 1
# Cálculo de Notas
# Somativa 1 e Somativo 2
# Valores de 0 a 100
# O valor deverá¡ ser atribuido por duas notas e uma média final e ao final deverá¡ ser apresentado o resultado

# print("Bem-Vindos a calculadora de Notas")
# print("Notas do Senai")
# print("As notas serÃ£o por somativa 1 e 2")

# nota1 = float(input("Digite nota da somativa 1: "))
# nota2 = float(input("Digite nota da somativa 2: "))
# média = (nota1 + nota2) / 2
# print("Sua média final foi: ", round(média,2))

# # Exercí­cio 2 
# # Criar um algoritmo para simular uma calculadora
# # Deverá¡ conter os operadores + - / *
# # Ao inserir o valor 1 e valor 2 ela deve apresentar o resultado

# print("Soma +")
# print("subtração -")
# print("multiplicacao *")
# print("divisão")

# valor1 = float(input("Digite o primeiro valor:"))
# valor2 = float(input("Digite o segundo valor:"))
# operador = input("Qual operador deseja?")

# if operador == "+":
#     soma = valor1 + valor1
#     print("A soma foi: ", soma)
# elif operador == "-":
#      subtração = valor1 - valor2
#      print("A subtração foi: ", subtração)
# elif operador == "*":
#      multiplicacao = valor1 * valor2
#      print("A  multiplicacao foi: ", multiplicacao)
# elif operador == "/":
#      divisão = valor1 / valor2
#      print("A divisão foi: ". divisão)
# else:
#      print("Obrigado por usar nossa calculadora") print("Calculadora")


# # Exercí­cio 3:

# # Loja de roupas, sapatos e perfumes 
# # Ao escolher uma das opÃ§Ãµes vocÃª deverÃ¡ perguntar o valor do produto, a quantidade e aplicar o desconto
# # roupas = 10%
# # sapatos = 5%
# # perfumes = 2%

# print("Bem-vindos a loja Star Wars, aqui temos roupas, spatos e perfumes de Star Wars\
#       O que você procura?: ")
# print("Roupas = 1")
# print("Sapatos = 2")
# print("Perfumes = 3")
# opcao = int(input("Digite a opção desejada: "))

# if opcao == 1:
#     print("você escolheu Roupas")
#     prod = float(input("Qual o preço da roupa?"))
#     qtde = int(input("Quantas roupas?"))
#     desconto = 10 * 100 / 100
#     total = (prod * qtde) - desconto
#     print("Sua compra no setor de Roupas foi de: ", total)
# elif opcao == 2:
#     print("você escolheu Sapatos")
#     prod = float(input("Qual o preço do sapato?"))
#     qtde = int(input("Quantos sapatos?"))
#     desconto = 5 * 100 / 100
#     total = (prod * qtde) - 5 / 100
#     print("Sua compra no setor de Sapatos foi de: ", total)
# elif opcao == 3:
#     print("você escolheu Perfumes")
#     prod = float(input("Qual o preço do perfume?"))
#     qtde = int(input("Quantos perfumes?"))
#     desconto = 2 * 100 / 100
#     total = (prod * qtde) * 2 / 100
#     print("Sua compra no setor de Perfumes foi de: ", total)
# else:
#     print("Obrigado pela preferência, e que a força esteja com você!")