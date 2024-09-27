"""
## Lendo n linhas de um arquivo

Escreva um programa Python para ler as primeiras n linhas de um arquivo.

1. O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.

"""

def file_read_from_line(fname, nlines): 
    from itertools import islice #islice permite cortar um iterável, como um arquivo, e obter uma fatia dele sem precisar ler todo o conteúdo na memória.
    with open(fname, encoding="utf-8") as file:
        for line in islice(file, nlines):
            print(line)
            
file_read_from_line("4 -Arquivos/dados/texto.txt",3)