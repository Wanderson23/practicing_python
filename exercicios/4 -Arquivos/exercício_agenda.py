"""
Agenda de Contatos

Desenvolva uma agenda de contatos persistindo as informações em arquivo. O programa deve seguir as especificidades:

1. Criar o arquivo Agenda contendo quatro métodos:
    1. Um método para adicionar contato.
    2. Um método para listar contatos.
    3. Um método para remover contatos.
2. Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.

"""

import os

#Método para adicionar contato
def add_contact():
    name = input("Informe o nome:\n")
    address = input("Informe o endereço:\n")
    phone = input("Informe o fone:\n")
    
    contact = f"Nome: {name} \nEndereço: {address} \nTelefone: {phone}\n"
    
    with open ("4 -Arquivos/dados/contatos.txt","a", encoding="utf-8") as file:
        file.write(contact)
        
#Método para listar contato
def view_contacts():
    if not os.path.exists("4 -Arquivos/dados/contatos.txt"):
        print("Lista de contatos está vazia!")
        return
    with open("4 -Arquivos/dados/contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("Lista de contatos")
    print(contacts)
    
#Método para remover contato
def delete_contacts():
    if not os.path.exists("4 -Arquivos/dados/contatos.txt"):
        print("Lista de contatos está vazia!")
        return
    with open("4 -Arquivos/dados/contatos.txt", "w", encoding="utf-8") as file:
        file.write("")
    print("Contatos removidos com sucesso")
    