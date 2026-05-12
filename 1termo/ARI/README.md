# Script para gerar o arquivo Markdown da aula de IoT
conteudo_md = """# Aula: Arquitetura de Redes IoT
## Programação com C++ (Hardware) e Python (Dados/Cloud)

---

## 1. Arquitetura de Referência (3 Camadas)

Para entender IoT, dividimos o sistema em três níveis principais:

1.  **Camada de Percepção (Dispositivos):** Sensores e atuadores (Ex: Arduino, ESP32).
2.  **Camada de Rede (Conectividade):** Protocolos que levam o dado (Ex: Wi-Fi, MQTT, LoRa).
3.  **Camada de Aplicação (Processamento):** Onde os dados são exibidos e analisados.

---

## 2. Código do Dispositivo (Arduino / C++)

```cpp
const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
}

void loop() {
  int valor = analogRead(sensorPin);
  Serial.print("DADO_SENSOR:");
  Serial.println(valor);
  delay(2000);
}
```

---

## 3. Código do Gateway (Python)

```python
import serial
import time

# Conexão com a porta serial do Arduino
try:
    arduino = serial.Serial('COM3', 9600, timeout=1)
    print("Conectado ao Arduino!")
except:
    print("Erro: Verifique a porta COM.")

while True:
    if arduino.in_waiting > 0:
        dados = arduino.readline().decode('utf-8').strip()
        print(f"Recebido: {dados}")
    time.sleep(0.5)
```

---

## 4. Tabela de Protocolos


| Protocolo | Camada | Uso |
| :--- | :--- | :--- |
| **MQTT** | Aplicação | Baixo consumo, ideal para sensores. |
| **HTTP** | Aplicação | Integração com APIs Web. |
| **LoRaWAN** | Rede | Longas distâncias (Km). |
"""

# Criando e escrevendo o arquivo .md
nome_arquivo = "aula_iot_arquitetura.md"

try:
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo_md)
    print(f"Sucesso! O arquivo '{nome_arquivo}' foi gerado com sucesso.")
except Exception as e:
    print(f"Ocorreu um erro ao gerar o arquivo: {e}")
