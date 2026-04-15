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

cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(50) NOT NULL,
        idade INT NOT NULL,
        PRIMARY KEY (id)
    )
""")

cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')

cursor. execute(f"""
    INSERT INTO {TABLE_NAME} 
    (nome,idade) VALUES ("Henrique",22)

""")

connection.commit()
# FECHANDO CONEXÕES
cursor.close()
connection.close()