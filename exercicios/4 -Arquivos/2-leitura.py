"""
- Arquivos:
opção w - write (sobescreve os nomes)
opção a - append (insere)
opção r - read
"""


with open("4 -Arquivos/dados/names.txt", "r", encoding="utf-8") as file: #encoding para caracteres especiais
    for line in file:
        print(f"Olá, {line.rstrip()}") #rstrip tira o espaço entre as linhas