# Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

import tkinter as tk
from tkinter import messagebox

# def janela_bemvindo():
#     turno = turno_operador.get()
#     nome = nome_operador.get()
#     if nome == "" and turno == "": 
#         messagebox.showarning("Aviso!", "Digite seu nome: ")
#         messagebox.showarning("Digite seu turno: ")
#     else:
#         messagebox.showinfo("Bem-Vindo", f"Operador {nome} registrado no Turno {turno}. Boa jornada")
    

# janela = tk.Tk()
# janela.title("Operação")
# janela.geometry("550x550")
# janela.configure(bg="#63201e")
    
# lbl_mensagem = tk.Label(janela, text="Digite seu nome: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Turno A ")
# lbl_mensagem.grid(row=2, column=1, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Turno B ")
# lbl_mensagem.grid(row=3, column=1, pady=10, padx=10)

# lbl_mensagem= tk.Label(janela, text="Turno C ")
# lbl_mensagem.grid(row=4, column=1, pady=10, padx=10)


# lbl_mensagem = tk.Label(janela, text="Digite seu turno: ")
# lbl_mensagem.grid(row=5, column=0, pady=10, padx=10)

# turno_operador = tk.Entry(janela, font=("Arial", 12))
# turno_operador.grid(row=5, column=1, pady=10, padx=10)

# nome_operador = tk.Entry(janela, font=("Arial", 12))
# nome_operador.grid(row=0, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo)
# btn_mensagem.grid(row=6, column=1, padx=10, pady=10)


# janela.mainloop()


# Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# def janela_bemvindo():
#     pecas = int(pecas_por_hora.get())
#     if pecas == "": 
#         messagebox.showwarning("Aviso!", "Digite o número de peças produzidas em 1 hora: ")
#     elif pecas > 0:
#         pecas_oito_horas = pecas * 8
#         messagebox.showinfo("Bem-Vindo", f"Em 8 horas serão produzidas {pecas_oito_horas} peças no turno.")


# janela = tk.Tk()
# janela.title("Peças")
# janela.geometry("600x600")
# janela.configure(bg="#ad1a15")
    
# lbl_mensagem = tk.Label(janela, text="Digite o número de peças produzidas em 1 hora: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)


# pecas_por_hora = tk.Entry(janela, font=("Arial", 12))
# pecas_por_hora.grid(row=0, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo)
# btn_mensagem.grid(row=6, column=1, padx=10, pady=10)



# janela.mainloop()


# Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.


# def janela_bemvindo():
#     bar = float(conversor_de_unidades.get())
#     if bar == "": 
#         messagebox.showwarning("Aviso!", "Digite a pressão em Bar: ")
#     elif bar > 0:
#         pressao_psi = bar * 14.5
#         messagebox.showinfo("Bem-Vindo", f"A pressão em PSI é de: {pressao_psi} ")


# janela = tk.Tk()
# janela.title("Conversor de Bar em PSI")
# janela.geometry("200x200")
# janela.configure(bg="#dbd5d5")
    
# lbl_mensagem = tk.Label(janela, text="Digite a presão em Bar: ")
# lbl_mensagem.grid(row=0, column=2, pady=10, padx=10)


# conversor_de_unidades = tk.Entry(janela, font=("Arial", 12))
# conversor_de_unidades.grid(row=2, column=2, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=3, column=2, padx=10, pady=10)



# janela.mainloop()



# Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.


# def janela_bemvindo():
#     nota1 = float(primeira.get())
#     nota2 = float(segunda.get())
#     nota3 = float(terceira.get())
#     if nota1 and nota2 and nota3 == "": 
#         messagebox.showwarning("Aviso!", "Digite as notas de inspeção da peça: ")
#     elif nota1 and nota2 and nota3 >= 0:
#         qualidade = (nota1 + nota2 + nota3) /2
#         messagebox.showinfo("Bem-Vindo", f"A média da qualidade da peça é de: {qualidade} ")


# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("400x400")
# janela.configure(bg="#dbd5d5")
    
# lbl_mensagem = tk.Label(janela, text="Digite as notas de inspeção da peça: ")
# lbl_mensagem.grid(row=0, column=1, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Digite a primeira nota: ")
# lbl_mensagem.grid(row=1, column=0, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Digite a segunda nota: ")
# lbl_mensagem.grid(row=2, column=0, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Digite a terceira nota: ")
# lbl_mensagem.grid(row=3, column=0, pady=10, padx=10)

# primeira = tk.Entry(janela, font=("Arial", 12))
# primeira.grid(row=1, column=1, pady=10, padx=10)

# segunda = tk.Entry(janela, font=("Arial", 12))
# segunda.grid(row=2, column=1, pady=10, padx=10)

# terceira = tk.Entry(janela, font=("Arial", 12))
# terceira.grid(row=3, column=1, pady=10, padx=10)


# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=1, padx=10, pady=10)



# janela.mainloop()

# Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# def janela_bemvindo():
#     temperatura = int(temperatura_do_motor.get())
#     if temperatura == "": 
#         messagebox.showwarning("Aviso!", "Digite a temperatura do motor em graus Celsius: ")
#     elif temperatura < 40:
#         messagebox.showinfo("Baixa carga", "Baixa carga")
#     elif temperatura >= 40 and temperatura < 70:
#         messagebox.showinfo("Normal", "Normal. Tudo correto.")
#     elif temperatura > 70:
#         messagebox.showwarning("ALERTA!", "ALERTA: Resfriamento Ativado!")



# janela = tk.Tk()
# janela.title("Termostato Inteligente")
# janela.geometry("400x400")
# janela.configure(bg="#dbd5d5")
    
# lbl_mensagem = tk.Label(janela, text="Digite a temperatura do motor em graus Celsius: ")
# lbl_mensagem.grid(row=0, column=1, pady=10, padx=10)

# temperatura_do_motor = tk.Entry(janela, font=("Arial", 12))
# temperatura_do_motor.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=1, padx=10, pady=10)



# janela.mainloop()

# Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".


# def janela_bemvindo():
#     codigo = codigo_do_produto.get().upper()
#     if codigo == "": 
#         messagebox.showwarning("Aviso!", "Digite o código do produto! ")
#     elif codigo == "A":
#         messagebox.showinfo("A", "Alimentos")
#     elif codigo == "E":
#         messagebox.showinfo("E", "Eletrônicos")
#     else:
#         messagebox.showwarning("!", "Desconhecido!")



# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("400x400")
# janela.configure(bg="#0e474b")
    
# lbl_mensagem = tk.Label(janela, text="Digite o código do produto: ")
# lbl_mensagem.grid(row=0, column=1, pady=10, padx=10)

# codigo_do_produto = tk.Entry(janela, font=("Arial", 12))
# codigo_do_produto.grid(row=1, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=1, padx=10, pady=10)



# janela.mainloop()

# Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.


# def janela_bemvindo():
#     sensor_porta = sensor.get().lower()
#     botao_emergencia = emergencia.get().lower()
#     if sensor_porta == "" and botao_emergencia == "": 
#         messagebox.showwarning("Aviso!", "Digite as informações! ")
#     elif sensor_porta == "fechada" and botao_emergencia == "desligado":
#         messagebox.showinfo("Máquina Ligada", "A máquina já pode ser iniciada!")
#     else:
#         messagebox.showerror("Erro!", "A máquina não pode ser iniciada!")


# janela = tk.Tk()
# janela.title("Segurança de operação")
# janela.geometry("300x200")
# janela.configure(bg="#0e474b")
    
# lbl_mensagem = tk.Label(janela, text="A porta está fechada ou aberta? ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="O botão de emergência está ligado ou desligado? ")
# lbl_mensagem.grid(row=2, column=0, pady=10, padx=10)

# sensor = tk.Entry(janela, font=("Arial", 12))
# sensor.grid(row=1, column=0, pady=10, padx=10)

# emergencia = tk.Entry(janela, font=("Arial", 12))
# emergencia.grid(row=3, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=0, padx=10, pady=10)



# janela.mainloop()

# Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".


# def janela_bemvindo():
#     produzidas = int(total_produzidas.get())
#     descarte = int(total_defeituosas.get())
#     if descarte > 0.05 * produzidas: 
#         messagebox.showwarning("Aviso!", "Revisar Processo")
#     else:
#         messagebox.showinfo("Info!", "Processo Otimizado")


# janela = tk.Tk()
# janela.title("Cálculo de Descarte")
# janela.geometry("500x500")
# janela.configure(bg="#0e474b")
    
# lbl_mensagem = tk.Label(janela, text="Digite o total de peças produzidas: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Digite o total de peças defeituosas: ")
# lbl_mensagem.grid(row=2, column=0, pady=10, padx=10)

# total_produzidas = tk.Entry(janela, font=("Arial", 12))
# total_produzidas.grid(row=1, column=0, pady=10, padx=10)

# total_defeituosas = tk.Entry(janela, font=("Arial", 12))
# total_defeituosas.grid(row=3, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=0, padx=10, pady=10)



# janela.mainloop()

# Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.


# def janela_bemvindo():
#     medida = float(medida_correta.get())
#     if medida >= 9.8 and medida <= 10.2:
#         messagebox.showinfo("Info!", "A medida está dentro da tolerância!")
#     elif medida < 9.8:
#         messagebox.showwarning("Info!", "A medida está abaixo da tolerância!")
#     elif medida > 10.2:
#         messagebox.showwarning("Info!", "A medida está acima da tolerância!")
#     else:
#         messagebox.showerror("Aviso!", "Por favor, forneça a informação!")


# janela = tk.Tk()
# janela.title("Validação de Medida")
# janela.geometry("200x200")
# janela.configure(bg="#0e474b")
    
# lbl_mensagem = tk.Label(janela, text="Digite a medida da peça: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# medida_correta = tk.Entry(janela, font=("Arial", 12))
# medida_correta.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=0, padx=10, pady=10)



# janela.mainloop()


# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".


# def janela_bemvindo():
#     prensa = int(prensa_iniciar.get())
#     if prensa == 1:
#         for prensa in range(10, 1,-1):
#             messagebox.showinfo("Info!", f"Prensa Ativada! Em {prensa}")
#     else:
#         messagebox.showwarning("Aviso!", "Não é possível iniciar a prensa!")

# janela = tk.Tk()
# janela.title("Contagem Regressiva de Setup")
# janela.geometry("400x400")
# janela.configure(bg="#621e8a")

# lbl_mensagem = tk.Label(janela, text="Digite 1 caso queira iniciar a prensa: ")
# lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

# prensa_iniciar = tk.Entry(janela, font=("Arial", 12))
# prensa_iniciar.grid(row=1, column=0, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Clique aqui para iniciar a prensa", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=0, padx=10, pady=10)



# janela.mainloop()


