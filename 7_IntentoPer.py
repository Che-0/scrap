import bs4 
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin 

link = 'https://books.toscrape.com/index.html'
r = requests.get(link)
#print(r)

soup = BeautifulSoup(r.text,'lxml')

#titulos = soup.find_all('article',class_= 'product_pod')#.find_all('h3').get_text()
#lista_t = [x.find('h3').get_text() for x in titulos]



#print(lista_t)
#for x in lista_t:
#    print(x)

#nuevo = soup.select('li.next > a')
#
#nuevo = urljoin(link,str(nuevo))
#print(nuevo)

#precio = soup.find('article',class_= 'product_pod').find('div',class_='product_price').find('p').get_text()
re = soup.find_all('div',class_='product_price')#.find('p').get_text()
precios = [x.find('p').get_text() for x in re]
print(precios)