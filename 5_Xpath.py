import requests
import lxml.html as html
import pandas as pd 

link = 'https://books.toscrape.com'
linkcomplemento = 'https://books.toscrape.com/'

#obtener listado de categorias de libros
#esta madre se hace manual, es como para obtener las coordenadas

links_categorias = '//ul[@class="nav nav-list"]//ul/li//a/@href'

#titulos
titulo = '//article[@class="product_pod"]//h3/a/text()'

#Precio
precio = '//div[@class="product_price"]/p[@class ="price_color"]/text()'


#request  pinches links
r = requests.get(link)
home = r.content.decode('utf-8') # para que no la haga de a pedo con simbolos raros
parser = html.fromstring(home)
categorias_url = parser.xpath(links_categorias)
categorias_url = [linkcomplemento+x for x in categorias_url ]


#------------------------
#request esta madre desempaqueta el desmadre que paso categorias_url
r = requests.get(categorias_url[1]) # pongo un pinche numero porque al parecer son un chingo de cat (50)

home = r.content.decode('utf-8') # para que no la haga de a pedo con simbolos raros
parser = html.fromstring(home)

categorias_url = parser.xpath(links_categorias)

categorias_url = [linkcomplemento+x for x in categorias_url ]
print(categorias_url)