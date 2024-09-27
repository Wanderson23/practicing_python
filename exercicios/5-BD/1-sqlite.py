import sqlite3

# Criando o BD
connection = sqlite3.connect("title.db")

# 2 - Verifica se houve alterações na base de dados
print(connection.total_changes)