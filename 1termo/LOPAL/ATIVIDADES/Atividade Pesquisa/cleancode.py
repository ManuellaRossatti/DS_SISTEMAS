#1. Registro de Veículo: Peça o modelo do veículo e a placa. ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!" 
print("Registro de Veículo: ")
modelo = input("Qual é o modelo do veículo? ")
placa = input("Qual é a placa do veículo? ")
print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

#2. Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l). ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque cheio.

print("Cálculo de Autonomia:")
capacidade_do_tanque = float(input("Qual a capacidade do tanque em litros? "))
consumo_medio = float(input("Qual o consumo médio do caminhão em km/L? "))
distancia_total = capacidade_do_tanque / consumo_medio
print(f"A distância total que o veículo pode percorrer com o tanque cheio é: {distancia_total}km")


