# Tente criar um código que conte de 1 A 10, MAS USE O CONTINUE PARA NÃO IMPRIMIR O N° 5 (simule falha no sensor)
# import time
# leitura = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in leitura:
#     if num != 5:
#         time.sleep(1)
#         print(f"Sensor n° {num}, operando corretamente.")
#         continue 
#     print("Falha no sensor.")

# print("Fim.")

# import time

# for num in range(1, 11):
#     if num != 5:
#         time.sleep(1)
#         print(f"Sensor n° {num}, operando corretamente.")
#         continue 
#     print("Falha no sensor.")

# print("Fim.")

#Exercicio 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudas para tal cor ele represente uma pausa para cada cor. use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela).

# import time

# lista = [ "Verde", "Amarelo", "Vermelho",]

# for cor in lista:
#     if cor != "Amarelo":
#         print(f"Semáforo {cor} funcionando")
#         time.sleep(3)
#         continue
#     print(f"Semáforo {cor} falhando...")
#     time.sleep(3)

# print("Semáforo com defeito")

# exercício 4:
# Uma fábrica tem cinco máquinas. Peça ao usuário (via imput dentro do loop) o consumo de kwh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica:

# total = 0
# for maq in range(1, 6):
#     KWH = float(input(f"Qual o consumo da máquina n°{maq} em kWh? "))
#     total += KWH #Acumula o consumo total
# print("O consumo total é de", total)
    
# Exercício 5 - Identificador de peças defeituosas (for = if)
# Percorra uma lista de medidas de peças: # medidas [50.q, 49.8, 52.0, 50.0, 48.5]
# for medida in pecas:
#   if medida >= 50.0:
#     print(f"peça com medida {medida}mm: Aprovada")
#   else:
#     print(f"Peça com medida {medida}mm: Rejeitada")
# print("Fim da avaliação de peças.")



# exercicio 5 uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.
# crie um programa que peça ao usuario o peso de cado saco (via input dentro do loop) e, para cada um, informe se ele está "dentro do limite"(entre 48kg e 52kg) ou fora do limite
# no final, exiba quantos sacos estão dentro do limite
  
# sacos_d1=0
# for saco in range(1,7):
#      peso = float(input(f"Digite o peso {saco}:"))
# if 48 <= peso <= 52:
#     print(f"Saco {saco} com peso {peso}kg: Dentro do limite")
#     sacos_d1 += 1
# else:
#      print(f"Saco {saco} com peso {peso}kg: fora do limite")
# print(f"Quantidade de sacos dentro do limite: {sacos_d1}")



# o desafio gestao de ciclo termico 
# voce deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças
# regras do sistema 
# o programa deve rodar em um loop até que 5 peças validas sejam processadas
# para cada peça peça ao usuario a temperatura atual input
# Filtro de erro (continue) se o usuario digitar uma temperatura negativa exiba "erro de leitura no sensor" e use o continue para pedir a temperatura novamente ( essa leitura nao conta como peça processada).
# paradara de emergencia (break) Se a temperatura for maior qu 150, o sistema deve exibir
# "Alerta critico: risco de explosão!", interromper o loop imediatamente e encerrar o programa.



# meu
# lote_t=0
# import time
# temperatura = 1
# while temperatura < 150:
#     for lote in range(1,6):lote + float (input(f"digite a temperatura do lote{lote}"))
#     if 0 <= temperatura <= 150
# ciclo = 0
# while ciclo < 5:
#     temperatura = float(input(f'Digite a temperatura da peça {ciclo + 1} em °C:'))

#     if temperatura < 0:
#         print ("Erro de leitura do Sensor. Por favor, digite uma temperatura valida.")
#         continue

#     if temperatura > 150:
#         print("ALERTA CRÍTICO: Risco de explosão!")
#         break
    
#     print(f"Peça {ciclo + 1} processada com temperatura {temperatura}°C.")
#     ciclo += 1

#     print(f"Peça {ciclo} processada com sucesso. temperatura dentro do limite.")
# print("Fim do monitoramento de temperatura.")

# exercicio 6 contador de peças com falha while + if + continue uma linha de produçao deve Contar quantas peças com faLHA  foram detectadas o usuario deve digitar sim para indicar que uma peça tem falha e nao para indicar que esta peça é boa o programa deve continuar pedindo a condiçao da peça ate que o usuario digite fim no final exiba o total
