import sqlite3


# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor
"""
Cursor é um interador que permite navegar e manipular os registros em um BD.
"""
cursor = connection.cursor()

# 3 - Solicitando dados do usuário
#Inserindo os dados utilizando o input
name = input("Nome do filme:\n")
year = int(input("Ano do filme:\n"))
score = float(input("Nota do filme:\n"))

# 4 - Inserindo dados
cursor.execute("""
    INSERT INTO movies(name, year, score)
    VALUES (?,?,?)
               """, (name, year, score)) #Utilize uma tupla no final da instrução sql, passando as variáveis dos inputs, na mesma ordem



# 5 - Gravando dados no BD
connection.commit()
print("Dados inseridos com sucesso")

# 6 - Fechando conexão
connection.close()