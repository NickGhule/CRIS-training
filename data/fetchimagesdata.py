# extract movies data from a web page

import requests
from bs4 import BeautifulSoup
import os
import re
import urllib.request

# get the html content of the web page
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        return r.text
    except:
        print("Error")

# get the movie name and image url
def get_movies(html):
    soup = BeautifulSoup(html, 'html.parser')
    movies = soup.find_all('div', class_='flw-item')
    # print(movies[0])
    for movie in movies:

        print(movie.find('a', class_='film-poster-ahref flw-item-tip').get('title'))
        name = movie.find('a', class_='film-poster-ahref flw-item-tip').get('title')
        image = movie.find('img').get('data-src')
        # print(image)
        # exit()
        # print(movie.find('span', class_='fdi-item'))
        year = movie.find('span', class_='fdi-item').text
        # print(movie.find('span', class_='fdi-item fdi-duration'))
        duration = movie.find('span', class_='fdi-item fdi-duration')
        if duration == None:
            duration = 'N/A'
        else:
            duration = duration.text
        yield {
            'name': name,
            'image': "https://fmoviesto.site/" + image,
            'year': year,
            'duration': duration
        }
def main():
    url = 'https://fmoviesto.site/home'
    html = get_html(url)
    movies = get_movies(html)
    
    with open('/var/www/html/CRIS-training/data/movies.json', 'w+') as f:
        f.write("[")
        for movie in movies:
            f.write("\n\t{")
            f.write('\n\t\t"name": "' + movie['name'] + '",\n\t\t"src": "' + movie['image'] + '",\n\t\t"year": "' + movie['year'] + '",\n\t\t"duration": "' + movie['duration'] + '"\n')
            f.write("\t},")
        f.write("]")
       
    print("Done")

if __name__ == '__main__':
    main()
    
    