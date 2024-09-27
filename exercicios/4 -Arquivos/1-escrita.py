name = input("Digite o seu nome:\n")
"""
- Arquivos:
opção w - write
opção a - append
opção r - read
"""

"""#Alternativa 1
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()"""

#Alternativa 2
with open("names.txt", "a") as file:
    file.write(f"{name}\n")