# Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

import tkinter as tk
from tkinter import messagebox


# def janela_bemvindo():
#     turno = turno_operador.get().strip()
#     nome = nome_operador.get().strip()

#     if not nome and not turno:
#         messagebox.showwarning("Aviso!", "Digite seu nome e seu turno.")
#     elif not nome:
#         messagebox.showwarning("Aviso!", "Digite seu nome.")
#     elif not turno:
#         messagebox.showwarning("Aviso!", "Digite seu turno.")
#     else:
#         messagebox.showinfo("Bem-vindo", f"Operador {nome} registrado no Turno {turno}. Boa jornada")


# janela = tk.Tk()
# janela.title("Operação")
# janela.geometry("550x320")
# janela.configure(bg="#63201e")

# label_nome = tk.Label(janela, text="Digite seu nome:", bg="#63201e", fg="white", font=("Arial", 12))
# label_nome.grid(row=0, column=0, pady=10, padx=10, sticky="w")

# nome_operador = tk.Entry(janela, font=("Arial", 12))
# nome_operador.grid(row=0, column=1, pady=10, padx=10, sticky="w")

# label_turno = tk.Label(janela, text="Digite seu turno:", bg="#63201e", fg="white", font=("Arial", 12))
# label_turno.grid(row=1, column=0, pady=10, padx=10, sticky="w")

# turno_operador = tk.Entry(janela, font=("Arial", 12))
# turno_operador.grid(row=1, column=1, pady=10, padx=10, sticky="w")

# label_titulos = tk.Label(janela, text="Turnos disponíveis:", bg="#63201e", fg="white", font=("Arial", 12, "bold"))
# label_titulos.grid(row=2, column=0, columnspan=2, pady=(20, 5), padx=10, sticky="w")

# label_turno_a = tk.Label(janela, text="Turno A", bg="#63201e", fg="white", font=("Arial", 11))
# label_turno_a.grid(row=3, column=0, pady=2, padx=10, sticky="w")

# label_turno_b = tk.Label(janela, text="Turno B", bg="#63201e", fg="white", font=("Arial", 11))
# label_turno_b.grid(row=4, column=0, pady=2, padx=10, sticky="w")

# label_turno_c = tk.Label(janela, text="Turno C", bg="#63201e", fg="white", font=("Arial", 11))
# label_turno_c.grid(row=5, column=0, pady=2, padx=10, sticky="w")

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, font=("Arial", 12))
# btn_mensagem.grid(row=6, column=1, padx=10, pady=20, sticky="e")

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
# janela.title("Calculadora de Peças")
# janela.geometry("480x240")
# janela.configure(bg="#ad1a15")


# janela.columnconfigure(0, weight=1)
# janela.columnconfigure(1, weight=1)

# container = tk.Frame(janela, bg="#ad1a15")
# container.grid(row=0, column=0, padx=20, pady=20)

# lbl_mensagem = tk.Label(
#     container,
#     text="Digite o número de peças produzidas em 1 hora:",
#     font=("Arial", 12, "bold"),
#     bg="#ad1a15",
#     fg="white"
# )
# lbl_mensagem.grid(row=0, column=0, sticky="w", pady=(0, 10))

# pecas_por_hora = tk.Entry(container, font=("Arial", 14), width=12, justify="center")
# pecas_por_hora.grid(row=1, column=0, pady=(0, 15))

# btn_mensagem = tk.Button(    container,   text="Calcular",    command=janela_bemvindo,    font=("Arial", 12, "bold"),    bg="#ffffff",    fg="#ad1a15",
#     activebackground="#f0f0f0",
#     relief="raised",
#     bd=3,
#     width=12
# )
# btn_mensagem.grid(row=2, column=0, pady=5)

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
# janela.title("Conversor de Bar para PSI")
# janela.geometry("320x220")
# janela.configure(bg="#f2f0ee")


# janela = tk.Frame(janela, bg="#f2f0ee", padx=20, pady=20)
# janela.pack(expand=True)

# lbl_mensagem = tk.Label(janela, text="Digite a pressão em Bar:", bg="#f2f0ee", fg="#333", font=("Arial", 12, "bold"))
# lbl_mensagem.pack(anchor="w", pady=(0, 10))

# conversor_de_unidades = tk.Entry(janela, font=("Arial", 14), width=15, bd=2, relief="groove")
# conversor_de_unidades.pack(pady=(0, 15))

# btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo, bg="#4b6584", fg="#ffffff", font=("Arial", 11, "bold"), activebackground="#3a4f6b", padx=10, pady=5)
# btn_mensagem.pack()

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
#         qualidade = (nota1 + nota2 + nota3) /3
#         messagebox.showinfo("Bem-Vindo", f"A média da qualidade da peça é de: {qualidade} ")



# janela = tk.Tk()
# janela.title("Média de Qualidade")
# janela.geometry("420x340")
# janela.configure(bg="#ece3d6")

# container = tk.Frame(janela, bg="#f7f2ec", bd=2, relief="groove")
# container.place(relx=0.5, rely=0.5, anchor="center", width=380, height=300)

# titulo = tk.Label(container, text="Avaliação de Qualidade", bg="#f7f2ec", fg="#4b3b2d", font=("Helvetica", 16, "bold"))
# titulo.pack(pady=(15, 10))

# pergunta = tk.Label(container, text="Digite as notas de inspeção da peça:", bg="#f7f2ec", fg="#5f4a3f", font=("Arial", 11))
# pergunta.pack(pady=(0, 15))

# janela = tk.Frame(container, bg="#f7f2ec")
# janela.pack(pady=5)

# lbl_primeira = tk.Label(janela, text="Primeira nota:", bg="#f7f2ec", fg="#4b3b2d", font=("Arial", 10))
# lbl_primeira.grid(row=0, column=0, sticky="e", padx=(0, 10), pady=5)
# primeira = tk.Entry(janela, font=("Arial", 11), width=18)
# primeira.grid(row=0, column=1, pady=5)

# lbl_segunda = tk.Label(janela, text="Segunda nota:", bg="#f7f2ec", fg="#4b3b2d", font=("Arial", 10))
# lbl_segunda.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=5)
# segunda = tk.Entry(janela, font=("Arial", 11), width=18)
# segunda.grid(row=1, column=1, pady=5)

# lbl_terceira = tk.Label(janela, text="Terceira nota:", bg="#f7f2ec", fg="#4b3b2d", font=("Arial", 10))
# lbl_terceira.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=5)
# terceira = tk.Entry(janela, font=("Arial", 11), width=18)
# terceira.grid(row=2, column=1, pady=5)

# btn_mensagem = tk.Button(container, text="Calcular", command=janela_bemvindo, bg="#795548", fg="#ffffff", font=("Arial", 11, "bold"), activebackground="#a67865", activeforeground="#ffffff", width=18)
# btn_mensagem.pack(pady=15) 

# janela.mainloop()


# Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# def janela_bemvindo():
#     temperatura = int(temperatura_motor.get())
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
# janela.geometry("420x330")
# janela.configure(bg="#dbd5d5")


# janela = tk.Frame(janela, bg="#f2f0ee", padx=20, pady=20)
# janela.pack(expand=True)

# lbl_mensagem = tk.Label(janela, text="Digite a temperatura do motor em graus Celsius: ", bg="#f2f0ee", fg="#333", font=("Arial", 12, "bold"))
# lbl_mensagem.pack(anchor="w", pady=(0, 10))

# temperatura_motor = tk.Entry(janela, font=("Arial", 14), width=15, bd=2, relief="groove")
# temperatura_motor.pack(pady=(0, 15))

# btn_mensagem = tk.Button(janela, text="Calcular", command=janela_bemvindo, bg="#4b846e", fg="#ffffff", font=("Arial", 11, "bold"), activebackground="#3a6b42", padx=10, pady=5)
# btn_mensagem.pack()

# janela.mainloop()

# Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".


# def janela_bemvindo():
#     codigo = codigo_produto.get().upper()
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
# janela.geometry("350x330")
# janela.configure(bg="#0e474b")

# janela = tk.Frame(janela, bg="#f2f0ee", padx=20, pady=20)
# janela.pack(expand=True)

# lbl_mensagem = tk.Label(janela, text="Digite o código do produto: ", bg="#f2f0ee", fg="#333", font=("Arial", 12, "bold"))
# lbl_mensagem.pack(anchor="w", pady=(0, 10))

# codigo_produto = tk.Entry(janela, font=("Arial", 14), width=15, bd=2, relief="groove")
# codigo_produto.pack(pady=(0, 15))

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#4b846e", fg="#ffffff", font=("Arial", 11, "bold"), activebackground="#3a6b42", padx=10, pady=5)
# btn_mensagem.pack()

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
# janela.geometry("300x220")
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
# janela.geometry("250x250")
# janela.configure(bg="#6978bb")

# janela = tk.Frame(janela, bg="#563788", padx=20, pady=20)
# janela.pack(expand=True)
    
# lbl_mensagem = tk.Label(janela, text="Digite o total de peças produzidas: ")
# lbl_mensagem.grid(row=0, column=1, pady=10, padx=10)

# lbl_mensagem = tk.Label(janela, text="Digite o total de peças defeituosas: ")
# lbl_mensagem.grid(row=2, column=1, pady=10, padx=10)

# total_produzidas = tk.Entry(janela, font=("Arial", 12))
# total_produzidas.grid(row=1, column=1, pady=10, padx=10)

# total_defeituosas = tk.Entry(janela, font=("Arial", 12))
# total_defeituosas.grid(row=3, column=1, pady=10, padx=10)

# btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo, bg="#111110", font=("Arial", 11, "bold"),  fg="#FFF")
# btn_mensagem.grid(row=4, column=1, padx=10, pady=10)



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

