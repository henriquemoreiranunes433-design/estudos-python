import pymysql
import dotenv
import os

dotenv.load_dotenv()

TABLE_NAME = 'customers'
# CONECTANDO A BASE DE DADOS AO PYMYSQL
connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],       
    password=os.environ['MYSQL_PASSWORD'],  
    database=os.environ['MYSQL_DATABASE']
)
# CONECTANDO O CURSOR
cursor = connection.cursor()

cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(50) NOT NULL,
        idade INT NOT NULL,
        endereço VARCHAR(100) NOT NULL,
        PRIMARY KEY (id)
    )
""")
# LIMPA A TABELA
cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')


# COMANDO PARA INSERIR VALORES NA TABELA 
sql = f""" INSERT INTO {TABLE_NAME} 
    (nome, idade, endereço) VALUES (%s, %s, %s) """

# DADOS QUE SERÃO INSERIDOS 
dados = [
    ('Henrique',22, 'São Paulo'),
    ('Cláudio', 30, 'Brasília'),
    ('Carla', 40, 'Rio De Janeiro'),
    ('Pâmela',12, 'Manaus'),
    ('Joana', 20,'Minas Gerais'),
    ('Vinicius', 27, 'Bahia')
]

cursor.executemany(sql, dados)

# ALTERA A IDADE
mudança_idade = f'UPDATE {TABLE_NAME} SET idade = %s WHERE id = %s'

dados_idade = [
    (39, 3),
    (45, 4)
]
cursor.executemany(mudança_idade, dados_idade)

# ALTERA OS NOMES
mudança_nome = f'UPDATE {TABLE_NAME} SET nome = %s WHERE id = %s'

dados_nome = [
    ("JANEVALEIDE", 1),
    ("CLODOVIL", 2)
]
cursor.executemany(mudança_nome, dados_nome)

# DELETA UMA LINHA 
deleta = f'DELETE FROM {TABLE_NAME} WHERE id = %s'

cursor.execute(deleta, (4,))

# SELECIONA TODOS OS VALORES DA TABELA
cursor.execute(f'SELECT * FROM {TABLE_NAME}')

registros = cursor.fetchall()

for row in registros:
   print(f"ID: {row[0]} | Nome: {row[1]} | Idade: {row[2]} | endereço: {row[3]}")
connection.commit()

# FECHANDO CONEXÕES
cursor.close()
connection.close()