import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
from num2words import num2words
from datetime import date
import os


# Função para gerar o recibo em PDF
def gerar_recibo():
    cliente = entry_cliente.get()
    consulta = entry_consulta.get()
    valor = entry_valor.get()
    
    if not cliente or not consulta or not valor:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos!")
        return

    try:
        valor_float = float(valor)
    except ValueError:
        messagebox.showerror("Erro no valor", "O valor informado deve ser numérico.")
        return

    valor_msg = f"{valor} reais"
    valor_extenso = num2words(valor_float, lang='pt-br')
    valor_extenso_msg = f"{valor_extenso} reais".capitalize()
    
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year

    # Caminho dinâmico para a imagem
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório do script ou executável
    image_path = os.path.join(script_dir, 'dados/RECIBO.jpg')  # Caminho relativo para a imagem
    
    # Mensagem para depuração
    print(f"Caminho da imagem: {image_path}")

    # Configuração do PDF
    pdf = FPDF('L', 'pt', 'A4')  # 'L' para landscape, 'pt' para pontos, 'A4' como formato
    pdf.add_page()

    # Inserindo a imagem no tamanho correto
    pdf.image(image_path, x=0, y=0, w=842, h=595)

    # Definindo a fonte e cor do texto
    pdf.set_font("Arial", "", 20)
    pdf.set_text_color(0, 0, 0)

    # Adicionando os textos na imagem
    pdf.text(605, 142, valor_msg)  # Valor da consulta
    pdf.text(210, 236, cliente)  # Nome do cliente
    pdf.text(210, 272, valor_extenso_msg)  # Valor por extenso
    pdf.text(215, 345, consulta)  # Tipo de consulta

    # Adicionando a data (branca)
    pdf.set_text_color(0, 0, 0)
    pdf.text(107, 454, str(dia))
    pdf.text(165, 454, str(mes))
    pdf.text(225, 454, str(ano))

    try:
        nome_arquivo = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if nome_arquivo:
            pdf.output(nome_arquivo)
            messagebox.showinfo("Sucesso", f"Recibo gerado: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao gerar recibo: {e}")
        messagebox.showerror("Erro", f"Erro ao gerar recibo: {e}")

# Configuração da interface Tkinter
janela = tk.Tk()
janela.title("Gerador de Recibos")

# Ajuste do tamanho da janela
janela.geometry("500x300") # Definindo largura e altura da janela

# Configuração de fonte 
fonte_label = ("Arial", 12)
fonte_entry = ("Arial", 14)
fonte_botao = ("Arial", 14, "bold")


# Labels e campos de entrada
tk.Label(janela, text="Nome do Cliente:", font=fonte_label).grid(row=0, column=0, pady=10)
entry_cliente = tk.Entry(janela, font=fonte_entry, width=30)
entry_cliente.grid(row=0, column=1, pady=10)

tk.Label(janela, text="Tipo de Consulta:", font=fonte_label).grid(row=1, column=0, pady=10)
entry_consulta = tk.Entry(janela, font=fonte_entry, width=30)
entry_consulta.grid(row=1, column=1, pady=10)

tk.Label(janela, text="Valor (em reais):", font=fonte_label).grid(row=2, column=0, pady=10)
entry_valor = tk.Entry(janela, font=fonte_entry, width=30)
entry_valor.grid(row=2, column=1, pady=10)

# Botão para gerar o recibo
btn_gerar = tk.Button(janela, text="Gerar Recibo", font=fonte_botao, command=gerar_recibo)
btn_gerar.grid(row=3, columnspan=2, pady=20)

janela.geometry("510x220")  # Largura 400px e altura 200px, ajuste conforme necessário

# Executar a janela
janela.mainloop()


