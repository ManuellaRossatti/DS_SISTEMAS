# Projeto de Revisão: Sistema de Empréstimo "Biblioteca Digital"
# Contexto: Você foi contratado para desenvolver o módulo de validação de
# empréstimos de livros de uma biblioteca comunitária. O sistema precisa coletar os dados
# do usuário, do livro e decidir se o empréstimo será aprovado, negado ou se haverá
# cobrança de taxa de segurança.
# Regras de Negócio (O que o sistema deve fazer):
# 1. Classificação do Usuário: A biblioteca atende [1] Alunos e [2] Comunidade Geral.
# 2. Limite de Dias: Alunos podem ficar com o livro por até 14 dias de graça.
#    A Comunidade Geral pode ficar por até 7 dias de graça.
# 3. Taxa de Renovação: Se o usuário quiser ficar mais tempo do que o limite do seu
#    perfil, será cobrada uma taxa fixa de R$ 5,00 por dia adicional.
# 4. Restrição de Categoria: Livros da categoria "Raros" não podem ser emprestados
#    para a Comunidade Geral, apenas para Alunos.

import tkinter as tk
from tkinter import messagebox, ttk


nome_usuario = ""
tipo_usuario = ""  
limite_dias = 0
taxa_diaria = 5.00

def limpar_janela():
    """Remove todos os widgets da janela"""
    for widget in janela.winfo_children():
        widget.destroy()

def tela_bemvindo():
    """Tela inicial para entrada do nome do usuário"""
    global nome_usuario
    
    limpar_janela()
    
    lbl_titulo = tk.Label(janela, text="Bem-Vindo à Biblioteca Digital", font=("Arial", 16, "bold"), bg="#572725", fg="#FFF")
    lbl_titulo.grid(row=0, column=0, columnspan=2, pady=20, padx=10)
    
    lbl_nome = tk.Label(janela, text="Digite seu nome:", font=("Arial", 12), bg="#572725", fg="#FFF")
    lbl_nome.grid(row=1, column=0, pady=10, padx=10, sticky="w")
    
    entry_nome = tk.Entry(janela, font=("Arial", 12), width=25)
    entry_nome.grid(row=1, column=1, pady=10, padx=10)
    entry_nome.focus()
    
    def prosseguir():
        nome = entry_nome.get().strip()
        if nome == "":
            messagebox.showwarning("Aviso", "Por favor, digite seu nome!")
        else:
            nome_usuario_texto = nome
            tela_classificacao(nome)
    
    btn_enter = tk.Button(janela, text="Prosseguir", command=prosseguir, bg="#D4A574", font=("Arial", 11, "bold"))
    btn_enter.grid(row=2, column=1, pady=20, padx=10, sticky="ew")

def tela_classificacao(nome):
    """Tela para seleção do tipo de usuário"""
    global tipo_usuario, limite_dias
    
    limpar_janela()
    
    lbl_titulo = tk.Label(janela, text=f"Bem-vindo, {nome}!", font=("Arial", 14, "bold"), bg="#572725", fg="#FFF")
    lbl_titulo.grid(row=0, column=0, columnspan=2, pady=20, padx=10)
    
    lbl_pergunta = tk.Label(janela, text="Qual é sua classificação?", font=("Arial", 12), bg="#572725", fg="#FFF")
    lbl_pergunta.grid(row=1, column=0, columnspan=2, pady=10, padx=10)




janela = tk.Tk()
janela.title("Biblioteca Digital - Sistema de Empréstimos")
janela.geometry("550x550")
janela.configure(bg="#572725")


tela_bemvindo()


janela.mainloop()