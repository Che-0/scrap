from bs4 import BeautifulSoup
import requests

website = 'https://subslikescript.com/movie/Titanic-120338'
result  = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')

#print(soup.prettify())


box = soup.find("article", class_="main-article") #almacenamos el bloque que necesitamos 
#de esta forma podemos delimitar el resto de cossas que estan fuera de este rango

title = box.find("h1").get_text()

guion = box.find('div', class_="full-script").get_text(strip=True,separator= ' ')
# strip  -- Borra espacios en blanco al principio y al final " python " --> "python"
# separtator -- quita los saltos de linea y los sustituye por un espacio en blanco o lo que le des de 
#argumento

#print(title)
#print(guion)

with open (f'{title}.txt' ,'w',encoding='utf-8') as file:
    file.write(guion)
