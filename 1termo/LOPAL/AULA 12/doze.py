import tkinter as tk
from tkinter import messagebox

# o . get() serve para buscar informação na caixa de texto

def janela_bemvindo():
    idade = idade_usuario.get()
    nome = nome_usuario.get()
    if nome == "" and idade == "": 
        messagebox.showarning("Aviso!", "Digite seu nome: ")
        messagebox.showarning("Digite sua idade: ")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá usuário, {nome}, {idade} - Seja bem-vindo ao nosso sistema")
    
# janela

janela = tk.Tk()
janela.title("Exemplo 2")
janela.geometry("300x300")
janela.configure(bg="#eb160f")

# Componentes:
# nome:

# label é lbl
lbl_mensagem = tk.Label(janela, text="Digite seu nome: ")
# lbl_mensagem.pack(pady=10)
lbl_mensagem.grid(row=0, column=0, pady=10, padx=10)

nome_usuario = tk.Entry(janela, font=("Arial", 12))
nome_usuario.grid(row=0, column=1, pady=10, padx=10)
# btn é Button
btn_mensagem = tk.Button(janela, text="Enter", command=janela_bemvindo)
btn_mensagem.grid(row=3, column=1, padx=10, pady=10)

# idade:
lbl_mensagem = tk.Label(janela, text="Digite sua idade: ")
lbl_mensagem.grid(row=2, column=0, pady=10, padx=10)

idade_usuario = tk.Entry(janela, font=("Arial", 12))
idade_usuario.grid(row=2, column=1, pady=10, padx=10)

# Rodar Interface:
janela.mainloop()