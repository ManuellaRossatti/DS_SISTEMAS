# Robõ deve pegar peça verde e vermelha
print("Meu primeiro robô" \
"Nome: Bruno Vader")

print("Peças:")
print("COR: Vermelho (peça defeituosa)")
print("COR: Verde (peça boa)")
cor = input("Qual cor você deseja?")
if cor == "Vermelho":
    andar = int(input("Quantos passos deseja andar (de 0-66)?"))
    if andar == 0:
        print("Ficar parado")
    elif 0 < andar < 66:
        print(f"Andar {andar} passos..")
        print("agachar...")
        print("Agarrar peça Vermelha...")
        print("Levantar...")
        print("Agora volte...")
        graus = int(input("Quantos graus você quer virar a direita (de 0-176)? "))
        if graus == 0:
            print("Não gire.")
        elif 0 < graus < 176:
            print(f"Vire {graus}° a direita.")
        graus2 = int(input("Quantos graus você quer virar a esquerda (de 0-176)? "))
        if graus2 == 0:
            print("Não gire.")
        elif 0 < graus2 < 176:
            print(f"Vire {graus2}° a esquerda.")
        else:
            print("Encerrar sistema")
        passos = int(input("Quantos passos você quer andar (de 0-66)? "))
        if passos == 0:
            print("Não andar")
        elif 0 < passos < 66:
            print(f"Andar {passos} passos")
            print("Entregar a peça ao programador")
        else:
            print("Encerrar sistema")
elif cor == "Verde":
    andar1 = int(input("Quantos passos deseja andar (de 0-36)?"))
    if andar1 == 0:
        print("Ficar parado")
    elif 0 < andar1 < 36:
        print(f"Andar {andar1} passos...")
        print("agachar...")
        print("Agarrar peça Verde...")
        print("Levantar...")
        print("Agora volte...")
        graus3 = int(input("Quantos graus você quer virar a direita (de 0-181)? "))
        if graus3 == 0:
            print("Não gire.")
        elif 0 < graus3 < 181:
            print(f"Vire {graus3}° a direita.")
        graus4 = int(input("Quantos graus você quer virar a esquerda (de 0-181)? "))
        if graus4 == 0:
            print("Não gire.")
        elif 0 < graus4 < 181:
            print(f"Vire {graus4}° a esquerda.")
        else:
            print("Encerrar sistema")
        passos1 = int(input("Quantos passos você quer andar (de 0-36)? "))
        if passos1 == 0:
            print("Não andar")
        elif 0 < passos1 < 36:
            print(f"Andar {passos1} passos")
            print("Entregar a peça ao programador")
        else:
            print("Encerrar sistema")
else:
    print("Encerrar sistema")

print("Bom trabalho Bruno Vader! Até mais!!")
