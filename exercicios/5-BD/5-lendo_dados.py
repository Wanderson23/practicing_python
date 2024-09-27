import sqlite3


# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
"""
Cursor é um interador que permite navegar e manipular os registros em um BD.
"""
cursor = connection.cursor()

# 3 - Lendo dados da tabela
data = cursor.execute("""
        SELECT name, year, score FROM movies
                      """)
print(data.fetchall())

# 4 - Iterando os dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}\n")
    
# 5 - Ordenando os dados pelo score
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f"{row}")


# 6 - Fechando conexão
connection.close()