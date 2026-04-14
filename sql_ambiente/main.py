import pymysql
import dotenv
import os

dotenv.load_dotenv()

# CONECTANDO A BASE DE DADOS AO PYMYSQL
cconnection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],       
    password=os.environ['MYSQL_PASSWORD'],  
    database=os.environ['MYSQL_DATABASE']
)
# CONECTANDO O CURSOR
cursor = cconnection.cursor()


# FECHANDO CONEXÕES
cursor.close()
cconnection.close()