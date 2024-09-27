#Instale por linha de comando a biblioteca fpdf

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World')
pdf.output('4 -Arquivos/dados/exemplo.pdf')