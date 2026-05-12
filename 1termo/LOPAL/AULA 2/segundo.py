# CondiÃ§Ãµes LÃ³gicas
# O programa toma caminhos diferentes dependendo da condiÃ§Ã£o
# FunÃ§Ãµes de LÃ³gicas Se e SenÃ£o
# If , elif e else
# if = se (verdadeiro)
# elif = continua sendo (verdadeiro)
# else = falso

#exemplo 1 
# print("Bem-Vindo as LÃ³gicas e DecisÃµes")
# print("Para iniciar digite a opÃ§Ã£o desejada")
# print("Digite 1 para Filmes e 2 para SÃ©ries e para 3 Novelas")

# escolha = int(input("Digite a opÃ§Ã£o que deseja: "))

# if escolha == 1:
#     print("VocÃª escolheu Filmes")
# elif escolha == 2:
#     print("VocÃª escolheu SÃ©ries")
# elif escolha == 3:
#     print("VocÃª escolheu Novelas")
# else:
#     print("VocÃª nÃ£o escolheu nenhuma opÃ§Ã£o do catalogo")
    
# # Exemplo 2
# print("PokÃ©mon")
# print("Escolha seu personagem")
# print("Pikachu = P")
# print("Charizard = C")
# print("MewTwo = M")
# print("Absol = A")

# pokemons = input("Digite a letra do seu personagem:")

# if pokemons == "P":
#     print("Você escolheu o PIKACHU")
# elif pokemons == "C":
#     print("Você escolheu o CHARIZARD")
# elif pokemons == "M":
#     print("Você escolheu o MEWTWO")
# elif pokemons == "A":
#     print("Você escolheu o ABSOL")
# else:
#     print("Espero você na próxima, até mais!!")

# Exemplo 3
# Valores númericos e flutuantes
print("Valores")
print("Comparações de números")

numeros = int(input("Digite um número"))

if numeros > 100:
    print("Número Alto")
elif numeros < 100:
    print("Número Baixo")
else:
    print("Escolher um valor que não temos")
    