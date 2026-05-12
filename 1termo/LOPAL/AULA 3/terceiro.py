# 1. O laço "for" (repetições determinadas)
# Use o"for"quando você sabe extamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1:

# for lote in range(1, 6):
#     print(f"Processando lote número{lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

# for b in range(10):
#     print(f"Quantidade total {b} foi...")

# # Imagine o seguinte cenário, iremos produzir 20 discos de vinil

# for discos in range(1, 21):
#     print(f"Quantidade de discos {discos} produzidos foi de")
#     print("Qualidade verifica [OK]")
# print("Produção finalizada!")

# Exemplo 4
# pecas = ["Engrenagem", "Eixo", "Rolamento",  "Parafuso", "Martelo"]
# itempecas = ["Cilíndricas", "Eixo Cônico", "Radiais", "Madeira", "Bola", "Cabeça Chata", "Chave Metálica Vermelha Comunista"]
# for item in pecas:
#     print(f"Item em estoque: {item} {itempecas}")

# # ou 
# pecas = ["Engrenagem", "Eixo", "Rolamento",  "Parafuso", "Martelo"]
# itempecas = ["Cilíndricas", "Eixo Cônico", "Radiais", "Madeira", "Bola", "Cabeça Chata", "Chave Metálica Vermelha Comunista"]
# for item in pecas:
#     print(f"Item em estoque: {item}")
#     for item2 in itempecas:
#         print(f"Item de peças em estoque: {itempecas}")

# Exemplo 5
# Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos
print("Seja Bem-Vindos a loja Meliora")
print("Opção 1- Vinis")
print("Opção 2- CD`s")
menu = int(input("Escolha uma opção"))
Vinis = ["Vinil Meliora - Ghost", "Vinil Prequelle - Ghost", "Vinil Impera - Ghost", "Vinil Opus Eponymous - Ghost", "Vinil Infestissuman - Ghost", " Vinil Skeletá - Ghost"]
CDs = ["Meliora - Ghost", "Impera - Ghost", "Opus Eponymous - Ghost", "Infestissuman - Ghost", "Skeletá - Ghost"]

if menu == 1:
    for item1 in Vinis:
        print(f"Sua lista de Vinis do Ghost {Vinis} está aqui...")
elif menu == 2:
    for item1 in CDs: #opcional
        print(f"Sua lista de CDs {CDs} está aqui...")
else:
     print("Opção inválida: Encerrando sistema.")

