from bs4 import BeautifulSoup
import requests

link = 'https://subslikescript.com/movie/Mega_Lightning-19119598'
result = requests.get(link)
content = result.text

soup = BeautifulSoup(content,'lxml')
#bien = soup.prettify()

#with open ("4_OtraPutaPractice.txt", 'w', encoding= 'utf-8') as file:

# El desmadre de encoding se puede arreglar haciendo el encode antes
#pero a la chingada , empiezo de cero de nuevo
#esta vez con Xpath

#    file.write(bien)
#