import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = 'post123',
    host = 'localhost',
    port = '5432'
)