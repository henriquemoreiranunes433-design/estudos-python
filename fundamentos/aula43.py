from dotenv import load_dotenv
import os

load_dotenv()

#print(os.environ)

print(os.getenv('BD_PASSWORD'))
print(os.getenv('USER_BD'))
print(os.getenv('BD_HOST'))
print(os.getenv('BD_PORT'))