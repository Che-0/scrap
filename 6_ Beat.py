import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urljoin 

url_inicial = "https://books.toscrape.com/index.html"
url_root = "https://books.toscrape.com/index.html"


r = requests.get(url_inicial)

s = BeautifulSoup(r.text,"lxml")

lista_article = s.find_all('article',class_='product_pod')
links_libros = [x.find('h3').find('a').get('href') for x in lista_article]
#print(links_libros) el pedo de esto es que sale sin el link completo

links_libros = [urljoin(url_root,i) for i in links_libros] # more elegante que concatenar para que esten completos
