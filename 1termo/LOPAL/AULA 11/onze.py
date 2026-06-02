import tkinter as tk
from tkinter import messagebox
janela = tk.Tk()
janela.title("Minha Primeira GUI")
janela.geometry("400x200") # Largura x Altura

def mostrar_mensagem():
    messagebox.showinfo("Sucesso!", "Você clicou no botão e o evento funcionou!")
lbl_titulo = tk.Label(janela, text="Bem-vindo à aula de Tkinter!",font=("Arial", 14, "bold"))
btn_clique = tk.Button(janela, text="Clique Aqui 🚀", font=("Arial", 11), bg="#5d39ff", fg="white", command=mostrar_mensagem)
lbl_titulo.pack(pady=20) # 'pady' adiciona um espaçamento vertical
btn_clique.pack(pady=10)
janela.mainloop()

