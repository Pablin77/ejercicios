"""
2- Use the HTTP GET method to retrieve information about recent television shows. Query
https://jsonmock.hackerrank.com/api/tvseries to find all the shows in a genre. The query result is
paginated. To access additional pages, append ?page={num} to the URL where num is the page
number.
Return
string: the highest-rated show in the genre, with the lowest name alphabetically if there is a tie
Version de Python: Python 3.10.9
"""
import requests
import json


def bestInGenre(s):
   """
   Funcion que recorre las paginas y analiza los elementos de tal manera que devuelve la serie
   de TV con mayor rating, ordenando los resultados en el caso que exista un empate.
   """
   genero = s.capitalize()
   url = "https://jsonmock.hackerrank.com/api/tvseries"
   response = requests.get(url)
   data = response.json()
   total_page = data['total_pages']
   imdb_rating = float(0)
   for page in range(1, total_page + 1):
       content = requests.get(url+"?page="+str(page)).json()
       # Actualizo cantidad de resultados por pagina 
       per_page = content['per_page']
       for per_p in range(per_page):
           # Separo los generos para tratarlos por separado
           generos = content['data'][per_p]['genre'].split(", ")
           # Convierto cada genero al formato capitalize para solucionar el caso de Sci-Fi y Reality-TV
           generos = [xgeneros.capitalize() for xgeneros in generos]
           if genero in generos:
               rating_content = float(content['data'][per_p]['imdb_rating'])
               if imdb_rating < rating_content:
                   name= []
                   name.append(content['data'][per_p]['name'])
                   imdb_rating = rating_content
               elif imdb_rating == rating_content:
                   name.append(content['data'][per_p]['name'])
   if imdb_rating == 0:
       return('No hay series con el genero '+ s)
   else:
       name = sorted(name)
       return name


if __name__ == "__main__":
   genero = input('Ingrese genero: ')
   print(bestInGenre(genero))
