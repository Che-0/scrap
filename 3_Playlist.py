"""
El punto de este desmadre es tratar de descargar una playlist
con scraping
Una pinche playlist completa
"""

from bs4 import BeautifulSoup
import requests


link = 'https://www.youtube.com/playlist?list=PLgPrQqJ5nn_TeQ8rTEr02hzV5DlmpRUU1'
resultado = requests.get(link)
content = resultado.text

soup = BeautifulSoup(content,'lxml')

#print(soup.prettify())

box = soup.find_all('ytd-two-column-browse-results-renderer')


print(box)
#for boxes in box:
#    print(boxes)

