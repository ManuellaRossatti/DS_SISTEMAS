# SOMATIVA BRUNO 
# MANUELLA BARROS DE SOUZA ROSSATT

# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O
# jogador [nick] está no nível [nível] e pronto para a partida!"
print(".⋆｡⋆☂˚｡⋆｡˚☽˚｡⋆.")
print(" 𓂀𝖌𝖍𝖔𝖘𝖙 𝖌𝖆𝖒𝖊")
print(".⋆｡⋆☂˚｡⋆｡˚☽˚｡⋆.")
nick = input("Por favor digite seu nickname: ")
nivel = int(input("Por favor digite seu nível atual: "))
print(f"O jogador {nick} está no nível {nivel} e pronto para a partida!")


# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e
# multiplique por 4 para mostrar quanto ele terá no final do mês.
print("︵‿︵‿︵‿︵‿︵‿︵‿︵")
print("CALCULADORA DE MESADA")
print("︵‿︵‿︵‿︵‿︵‿︵‿︵")
valorSemana = float(input("Quanto o aluno ganha por semana: "))
mesada = valorSemana * 4
print(f"Sua mesada será de: {mesada}")


# 3. Conversor de Internet: Peça um valor em Gigabytes (GB) e converta para
# Megabytes (MB) (multiplique por 1024).
print(". ・ 。. ・ ゜ ✭ ・. ・ ✫ ・ ゜ ・ 。.")
print("       Bem-vindo ao conversor!")
print(". ・ 。. ・ ゜ ✭ ・. ・ ✫ ・ ゜ ・ 。.")
valorGB = int(input("Digite o valor em gigabytes: "))
valorMB = valorGB * 1024 
print(f"O resultado em Megabytes é: {valorMB}")

# 4. Média de Notas: Peça as notas de Matemática e Português. Calcule e mostre a
# média final.
print("▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼")
print(" Bem-Vindo a Calculadora de Média!")
print("▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼ △ ▼")
mat = float(input("Digite sua nota de matemática: "))
port = float(input("Digite sua nota de português: "))
media = (mat + port) / 2
print(f"Essa é sua média: {media} ")
print("▼ △ ▼ △ ▼ △ ▼ △ ▼ △")
print(" Cálculo encerrado.")
print("▼ △ ▼ △ ▼ △ ▼ △ ▼ △")

# 5. Seguidores: Peça a quantidade de seguidores atuais e quantos novos seguidores
# o aluno ganhou hoje. Exiba o total atualizado.
print(".｡❅ * ⋆⍋ * ∞ *｡")
print("  SEGUIDORES")
print(".｡❅ * ⋆⍋ * ∞ *｡")

seguidores = int(input("Qual a quantidade de seguidores atuais: "))
seguidoresnovos = int(input("Qual a quantidade de seguidores novos: "))
total = seguidores + seguidoresnovos
print(f"Parabéns, agora você possui um total de {total} seguidores!")


# 6. Idade em Dias: Peça a idade do aluno e calcule aproximadamente quantos dias
# ele já viveu (idade * 365).
print("°。 °。 °。 °。 °。 °。°。 °。 °。 °。 °。 °。°。 °。")
print("    Já se perguntou quantos dias você já viveu?")
print("°。 °。 °。 °。 °。 °。°。 °。 °。 °。 °。 °。°。 °。")
idade = int(input(" Qual a sua idade: "))
idadeemdias = idade * 365
print(f"Você já viveu {idadeemdias} dias!")

# 7. Consumo de Lanche: Peça o preço do salgado e o preço do suco. Exiba o valor
# total da conta.
print("====================")
print(" Gastos com lanche: ")
print("====================")
salgado = float(input("Preço do salgado: "))
suco = float(input("Preço do suco: "))
total = salgado + suco
print(f"Total da conta foi de: {total} reais")

# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano
# em que ele nasceu.
print("==================================")
print(" Calculando o ano de nascimento")
print("==================================")
anoatual = int(input("Qual o ano atual: "))
idade = int(input("Quantos anos você fez o fará no ano atual: "))
anodenascimento = anoatual - idade
print(f"Você nasceu em: {anodenascimento}")

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba
# "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou
# mais, "Acesso liberado".
print("✺✳ ┅ ⑅ ┅ ✳✺✺✳ ┅ ⑅ ┅ ✳✺")
print("   Bem-vindo ao TikTok!")
print("✺✳ ┅ ⑅ ┅ ✳✺✺✳ ┅ ⑅ ┅ ✳✺")
idade = int(input("Qual a sua idade: "))
if idade < 13:
    print("Acesso restrito!")
elif idade in range(13, 18):
    print("Acesso moderado.")
elif idade >= 18:
    print("Acesso liberado.")
else:
    print("Error. Não foi possível finalizar cadastro. Tente novamente.")


# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada
# repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando
# chegar em 10 e exibe: "Por favor, conecte o carregador!".


print("Bateria")
print("ততততত")
import time

bateria = 100

while bateria >= 10:
 print(f"Bateria em: {bateria}%")
 bateria = bateria - 10
 time.sleep(1)
print("Por favor, conecte o carregador")



# 11. Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma
# foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até
# esse número, printando: "Curtida no [i] recebida!".
import time

print("✧ ･ ﾟ: * ✧ ･ ﾟ: *")
print("    Curtidas ♡")
print("✧ ･ ﾟ: * ✧ ･ ﾟ: *")
limite = int(input("Digite a quantidade de curtidas: "))

for curtidas in range(1, limite + 1):
    print(f"♥ Curtida nº {curtidas} recebida!")
    time.sleep(0.5)

# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o
# aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre
# quantas vezes ele adiciona itens ao carrinho (use um contador).


print("༶ • ┈┈┈┈┈┈┈┈⛧┈┈┈┈┈┈┈ • ༶ ") 
print("  Carrinho de compra 🛒")
print("༶ • ┈┈┈┈┈┈┈┈⛧┈┈┈┈┈┈┈ • ༶ ") 

contador = 0

produto = 0

while produto != "sair":
    contador = contador + 1
    produto = input("Digite o nome do produto (ou sair, para finalizar): ")

print(f"Você adicionou {contador - 1} itens ao carrinho")
