import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

porta = "COM3"  # ajuste para sua porta

ser = serial.Serial(porta, 115200)

temperaturas = []
amostras = []

fig, ax = plt.subplots()

def atualizar(frame):
    linha = ser.readline().decode().strip()

    try:
        temperatura, umidade = linha.split(",")

        temperaturas.append(float(temperatura))
        amostras.append(len(amostras))

        if len(temperaturas) > 50:
            temperaturas.pop(0)
            amostras.pop(0)

        ax.clear()
        ax.plot(amostras, temperaturas)
        ax.set_title("Temperatura DHT11")
        ax.set_ylabel("°C")
        ax.set_xlabel("Leitura")

    except:
        pass

ani = FuncAnimation(fig, atualizar, interval=1000)

plt.show()
