'''
El webscraping es un proceso que se puede utilizar para
extraer automáticamente información de un sitio web y se puede realizar fácilmente en cuestión de
minutos y no de horas. Para empezar, solo necesitamos un poco de código Python y la ayuda de
dos módulos llamados Requests y Beautiful Soup. 
'''

#Importamos BeautifulSoup, Podemos almacenar el HTML de la página web como una cadena en la variable HTML. 

#aqui un ejemplo

from bs4 import BeautifulSoup
import requests

html = None #aca viene el codigo html de la pagina 

soup = BeautifulSoup(html,'html5lib') #volvemos el html a un objeto sopu de la libreria beautifulsoup , soup representa la estructura de datos organizada 

page = requests.get("http://websiteurl").text

#Crear el objeto de beatifulsoup

soup = BeautifulSoup(page,'html.parser')

#Traer todas las instancias que esten con <a>
artists = soup.findAll('a')

#limpiar la data de todos las etiquetas

for artist in artists:
    names = artist.contents[0]
    fullLink = artist.get('href') 
    print(names)
    print(fullLink)


#buscar por el arbol html, en este caso el atributo boldest

tag_object = soup.title
tag_child = tag_object.b
parent_tag =tag_child.parent #navegar hacia arriba en el arbol

#podemos acceder al atributo que tiene un html, como el id y su valor 

tag_child.attrs #{'id':'boldest'}

#podemos traer su str 

tag_child.string 


#FIND ALL busca los descendietnes de una etiqueta html y recupera todos sus datos
table = soup
table_row = table.find_all(name='tr')

table_row: None 

#podemos seleccionar el primer valor 

first_row  = table_row[0]

#podemos iterar por los valores

for i,row in enumerate(table_row):
    print("row",i  )
    cell= row.find_all("td")

    for j,cell in enumerate(cell):
        print("column",j,"cell", cell)