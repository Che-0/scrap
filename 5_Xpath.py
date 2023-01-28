import requests
import lxml.html as html

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
#request esta madre desempaqueta el desmadre que paso categorias_url o la puta pagina en la que se esta
r = requests.get(categorias_url[1]) # pongo un pinche numero porque necesito indicar la seccion
#estamos mandando un request a esa direccion en especifico

home = r.content.decode('utf-8') # para que no la haga de a pedo con simbolos raros
parser = html.fromstring(home)

titulos_book = parser.xpath(titulo)
prc = parser.xpath(precio)
print(titulos_book)
print(prc)

