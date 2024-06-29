from tkinter import *
from tkinter import messagebox
import random

# -- CONSTANTES -- #
FONTE = ("Helvetica", 11)

# -- GERADOR DE SENHA -- #
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '_', '-', '@']

def gerador_senha(tamanho):
    c = 0
    senhas_lista = []
    while c < tamanho:
        aleatorio = random.randint(0, 2)
        if aleatorio == 0:
            senha_letra = random.choice(letras)
            senhas_lista.append(senha_letra)
            c += 1
        elif aleatorio == 1:
            senha_numero = random.choice(numeros)
            senhas_lista.append(senha_numero)
            c += 1
        else:
            senha_simbolo = random.choice(simbolos)
            senhas_lista.append(senha_simbolo)
            c += 1

    random.shuffle(senhas_lista)

    senha = "".join(senhas_lista)

    senha_gerada = senha_entry.get()
    senha_entry.delete(0, len(senha_gerada))
    senha_entry.insert(0, senha)

def gerar_senha():
    gerador_senha(int(senha_tamanho.get()))

def copiar_para_clipboard():
    senha = senha_entry.get()
    if len(senha) == 0:
        messagebox.showerror(title="Gerenciador de Senhas", message="Nenhuma senha para copiar.")
    else:
        messagebox.showinfo(title="Gerenciador de Senhas", message="Senha copiada.")
        janela.clipboard_clear()
        janela.clipboard_append(senha)

# -- SALVAR SENHA -- #
def salvar_senha():
    website = website_entry.get()
    email_usuario = email_usuario_entry.get()
    senha = senha_entry.get()
    if len(website.strip()) > 0 and len(email_usuario.strip()) > 0 and len(senha.strip()) > 0:
        salvar_pergunta = messagebox.askyesno(title="Gerenciador de Senhas", message=f"Website: {website}\n"
                                                                       f"Email/Usuário: {email_usuario}\n"
                                                                       f"Senha: {senha}\n"
                                                                       f"\n"
                                                                       f"Salvar dados?")
        if salvar_pergunta == YES:
            with open("dados.txt", mode="a") as file:
                file.write(f"{website} | {email_usuario} | {senha}\n")

            website_entry.delete(0, END)
            email_usuario_entry.delete(0, END)
            senha_entry.delete(0, END)
    else:
        messagebox.showerror(title="Gerenciador de Senhas", message="Ao menos um campo está vazio.")

# -- INTERFACE -- #
# Janela
janela = Tk()
janela.title("Gerenciador de Senhas")
janela.config(pady=40, padx=40)

# Labels
website_label = Label(text="Website:", font=FONTE)
website_label.grid(column=0, row=1, sticky="e")

email_usuario_label = Label(text="Email/Usuário:", font=FONTE)
email_usuario_label.grid(column=0, row=2)

senha_label = Label(text="Senha:", font=FONTE)
senha_label.grid(column=0, row=3, sticky="e")

senha_tamanho_label = Label(text="Tamanho da senha:", font=FONTE)
senha_tamanho_label.grid(column=0, row=4)

# Buttons
copiar_senha_btn = Button(text="Copiar", font=FONTE, width=15, command=copiar_para_clipboard)
copiar_senha_btn.grid(column=2, row=5, pady=10)

gerar_senha_btn = Button(text="Gerar Senha", font=FONTE, command=gerar_senha)
gerar_senha_btn.grid(column=2, row=3)

salvar_senha_btn = Button(text="Salvar Senha", font=FONTE, width=22, command=salvar_senha)
salvar_senha_btn.grid(column=1, row=5, pady=10)

# Spinbox (para determinar tamanho da senha)
senha_tamanho = Spinbox(from_=4, to=30, width=3)
senha_tamanho.grid(column=1, row=4, sticky="w")

# Entries
website_entry = Entry(width=60)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="w", columnspan=2)

email_usuario_entry = Entry(width=60)

# Você pode usar essa linha para ter um email padrão escrito nesta widget
# email_usuario_entry.insert(0, "exemplo@gmail.com")

email_usuario_entry.grid(column=1, row=2, sticky="w", columnspan=2)

senha_entry = Entry(width=35)
senha_entry.grid(column=1, row=3, sticky="w")

janela.mainloop()
