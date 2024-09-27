import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
"""
Cursor é um interador que permite navegar e manipular os registros em um BD.
"""
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
id = int(input("Informe o id do filme que deseja remover:\n"))

# 4 - Removendo dados
cursor.execute("""
        DELETE FROM movies
        WHERE id = ?
               """, (id,)) #dica: utilize uma virgula para que entenda que é um elemento de uma tupla, e não uma string

connection.commit()
print("Filme removido com sucesso!")

# 6 - Fechando conexão
connection.close()