from conexao_postg import conn

cursor_obj = conn.cursor()

sql = """
    DELETE from game
    WHERE id = %s
"""

cursor_obj.execute(sql, (6,))

conn.commit()
print("Dados removidos com sucesso!")
conn.close()