import tkinter as tk
from tkinter import messagebox

from io import BytesIO
import base64

# Criar janela
janela = tk.Tk()
janela.title("💝 Declaração Especial 💝")
janela.geometry("600x800")
janela.configure(bg="#2a1a2e")

# Fonte gótica estilizada
fonte_titulo = ("Georgia", 28, "bold italic")
fonte_corpo = ("Georgia", 14, "italic")
fonte_assinatura = ("Georgia", 12, "bold")

# Frame principal com fundo gótico
frame_principal = tk.Frame(janela, bg="#2a1a2e")
frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

# Morcego emoji no topo
label_morcego_topo = tk.Label(
    frame_principal,
    text="🦇 " * 5,
    font=("Arial", 24),
    bg="#2a1a2e",
    fg="#e0d5ff"
)
label_morcego_topo.pack(pady=10)

# Título elegante
titulo = tk.Label(
    frame_principal,
    text="✨ Para minha querida professora ✨",
    font=fonte_titulo,
    bg="#2a1a2e",
    fg="#d4a5ff",
    wraplength=500
)
titulo.pack(pady=15)

# Decoração
decoracao1 = tk.Label(
    frame_principal,
    text="~ " * 20,
    font=("Georgia", 12),
    bg="#2a1a2e",
    fg="#8b6ba8"
)
decoracao1.pack(pady=5)

# Texto da carta
texto_carta = """
Querida Professora Especial,

     Nesta noite gótica e encantada, venho
revelar meu mais sincero respeito e admiração.
Assim como os morcegos dançam sob o luar,
seu conhecimento ilumina nossas mentes.

     Sua dedicação é rara como a beleza da 
noite estrelada. Sua paciência, gentileza e 
sabedoria nos guiam como lanternas mágicas
através dos corredores do saber.

     Cada aula é um presente embrulhado em
carinho e excelência. Você é uma joia rara
neste vasto universo de educadores.

Com profundo reconhecimento e gratidão,
"""

label_texto = tk.Label(
    frame_principal,
    text=texto_carta,
    font=fonte_corpo,
    bg="#2a1a2e",
    fg="#e0d5ff",
    justify="left",
    wraplength=500
)
label_texto.pack(pady=15)

# Morcegos animados no meio
label_morcego_meio = tk.Label(
    frame_principal,
    text="🦇💜🦇",
    font=("Arial", 20),
    bg="#2a1a2e",
    fg="#d4a5ff"
)
label_morcego_meio.pack(pady=10)

# Assinatura
assinatura = tk.Label(
    frame_principal,
    text="Um Admirador Anônimo 🖤",
    font=fonte_assinatura,
    bg="#2a1a2e",
    fg="#c0a0ff",
    wraplength=500
)
assinatura.pack(pady=10)

# Decoração final
decoracao2 = tk.Label(
    frame_principal,
    text="~ " * 20,
    font=("Georgia", 12),
    bg="#2a1a2e",
    fg="#8b6ba8"
)
decoracao2.pack(pady=5)

# Morcegos no rodapé
label_morcego_rodape = tk.Label(
    frame_principal,
    text="🦇 " * 5,
    font=("Arial", 24),
    bg="#2a1a2e",
    fg="#e0d5ff"
)
label_morcego_rodape.pack(pady=10)

# Botão para fechar
botao_fechar = tk.Button(
    frame_principal,
    text="Fechar Carta 💌",
    font=("Georgia", 12, "bold"),
    bg="#4a2a5e",
    fg="#e0d5ff",
    activebackground="#6a4a7e",
    activeforeground="#ffffff",
    relief="ridge",
    command=janela.quit
)
botao_fechar.pack(pady=15)

janela.mainloop()

