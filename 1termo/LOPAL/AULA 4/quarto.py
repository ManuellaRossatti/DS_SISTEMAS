# 1 O laço while (repetições indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (comum sensor de segurança oum botão de emergência)
# Exemplo Monitor de temperatura (loop infinito controlado)
# repete enquanto a temperatura estiver segura
# inicio

# import time
# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3 # simulando o aquecimento da máquina
# print("ALERTA! Temperatura atingiu o limite. Desligando motor...")

# 2 Lista de temperaturas lidas pelo sensor por minuto  
# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui e não lê os próximos valores (85 e 80)
#     print(f"Temperatura está em {temp}°C. Operação normal.")

# print("Sitema desligado. Aguardando manutenção.")

# Exemplo 3 

# import time

# materiais = ["metal", "metal", "plástico", "metal", "vidro", "metal"]
# for pecas in materiais:
#     if pecas != "metal":
#         time.sleep(1)
#         print(f"Aviso: Peça de {pecas} detectada. Desviando para descarte...")
#         continue # Pula o restante do código abaixo e vai para a próxima peça
#     # este código só roda se for peça de metal
#     print(f"Processando peça de {pecas}. Furando e polindo...")

# print("Fim do lote de produção.")

