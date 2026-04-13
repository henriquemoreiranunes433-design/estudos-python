import requests
from bs4 import BeautifulSoup
import re

url = 'http://localhost:3333/'
responce = requests.get(url)
bytes_html = responce.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding= 'utf-8')

# print(parsed_html.title)
# print(parsed_html.title.text)

top_jobs_title = parsed_html.select_one('#intro > div > div > article > h2')
article = top_jobs_title.parent
print(top_jobs_title)
print(top_jobs_title.text)
for p in article.select('p'):
    #print(p)
    print(re.sub(r'\s{1,}', ' ', p.text).strip())