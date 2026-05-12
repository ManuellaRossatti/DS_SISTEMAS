# Clean code aula 6
# Para que usar?
# Como usar?
# print("Clean Code - Aula 6")
# aula = 6
# print(f"Estamos na aula {aula} de Clean Code")

# Manipulação de arquivos e texto
# texto = "  Python é Muito legal!  "
# print(texto.strip().upper()) # "PYTHON"
# print(texto.strip().lower()) # "python"
# print(texto.strip().capitalize()) # "Python"
# print(texto.strip().title()) # "Python"
# print(texto.strip().replace(" ", "_")) # "Python"
# print(texto.strip().split()) # ["PYTHON"]

#Resultado:

# PYTHON É MUITO LEGAL!
# python é muito legal!
# Python é muito legal!
# Python É Muito Legal!
# Python_é_Muito_legal!
# ['Python', 'é', 'Muito', 'legal!']


# # Escrevendo
# with open("notas.txt", "w") as arquivo:
#     arquivo.write("Estudar Python hoje!")
#     arquivo.write("\nLer sobre Clean Code.")

# # # Lendo
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Resultado:
# Estudar Python hoje!
# Ler sobre Clean Code.


# Exercício 1:
# Crie um programa que peça ao usuário para inserir uma frase e, em seguida, exiba frases com com as seguintes trasnformações:
# - Remova os espaços extras no ínicio e no final da frase.

# frase = input("Insira uma frase: ")
# print(frase.strip().replace(" ", ".")) 


# Exemplo 1:
# Crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo. \n
# Exiba o resultado para o usuário.

# print("Contagem de palavras em arquivo")
# with open("notas.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras python é de... {contagem}")

# Execução de comandos do sistema 
import os #importa o módulo "os" para interagir com o sistema operacional "operating system"
# Onde estou?
# print(os.getcwd())
# # Listar arquivos na pasta
# print(os.listdir())
# print(os.listdir("..")) #Lista de arquivos da pasta pai
# print(os.listdir("..\\..")) # lista arquivos da pasta avô
# print(os.listdir("C:\\")) # lista arquivos da raiz do C
# print(os.listdir("C:\\Users")) # lista arquivos da pasta Users
# print(os.listdir("C:\\Users\\Public")) # lista arquivos da pasta public

# Outros comandos úteis:
# Criar pasta
# os.mkdir("nova_pasta")
# # Renomear pasta
# os.rename("nova_pasta", "pasta_renomeada")
# # Excluir
# os.rmdir("pasta_renomeada")

# exercicio 2: # Crie um script que mostre o caminho da pasta atual.
# print(os.getcwd())

# # exercicio 3: Liste os aarquivos da pasta atual.
# print(os.listdir())

# #Exercicio 4: crie uma pasta projetos, renomeie para meus_projetos. Por fim, exclua a pasta.
# os.mkdir("projetos")

# os.rename("projetos", "meus_projetos")

# os.rmdir("meus_projetos")

# Exercicio 5: Crie um arquivo chamado "log.txt" e escreva a mensagem "Log de atividades"
# dps, leia o conteudo do arquivo e exiba na tela.
# with open("log.txt", "w") as arquivo:
#     arquivo.write("Log de atividades")

# with open("log.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

# Exemplo de dicionário: Cire um dicionário com informações sobre uma pessoa e acesse um valor usando uma chave.

# pessoa = {
#     "nome": "Alice",
#     "idade": 30,
#     "cidade": "São Paulo",
#     "Profissão": "Engenheira"
# }

# pessoa2 = {
#     "nome": "Bruno",
#     "idade": 25,
#     "cidade": "SP",
#     "Profissão": "Designer"
# }

# print(pessoa["cidade"])
# print(pessoa2["nome"], pessoa["idade"])

# # 7:
# print("Bem-vindo à casa dos Animais")
# print("Temos duas filiais: a primeira na R. Anitta Battiston Coletta, 561 e Outra no Jd Europa.")
# print("Aqui está a lista de animais de cada filial: ")
# filial1 = {
#     "gatos": 47,
#     "cachorros": 30,
#     "cobras": 35,
#     "coelhos": 27
# }
# filial2 = {
#     "gatos": 31,
#     "cachorros": 52,
#     "cobras": 49,
#     "coelhos": 27

# }
# print("Primeira filial: ")

# print("Gatos:", filial1["gatos"])
# print("Cachorros:",filial1["cachorros"])
# print("Cobras:",filial1["cobras"])
# print("Coelhos:",filial1["coelhos"])

# print("Segunda filial: ")

# print("Gatos:",filial2["gatos"])
# print("Cachorros:",filial2["cachorros"])
# print("Cobras:",filial2["cobras"])
# print("Coelhos:",filial2["coelhos"])

# Exemplo 2: Desligar o PC:
with open("desliga.bat", "w") as desligar:
    desligar.write("Shutdown -s -t 60 -c \"Desligamento programado para daqui a 1 hora. Salve seu trabalho!\"")
    # -s comando para desligar
    # -t tempo definir
    # -a cancelar desligamento
    # -c mensagem pro usuário