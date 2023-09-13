import requests
from bs4 import BeautifulSoup

def one_film():
    url = 'https://www.ivi.ru/movies/2022?sort=ivi&rating_part=main&rating_model=ready'
    r = requests.get(url).text

    with open('projects.html', 'w') as file:
        file.write(r)

    with open('projects.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    link = 'https://www.ivi.ru/' + soup.find('li', class_='gallery__item gallery__item_virtual').find('a').get('href')
    name = soup.find('div', class_='nbl-slimPosterBlock__title').find('span').text
    genre = soup.find('div', class_='nbl-poster__propertiesInfo').find('div').text
    marks = soup.find('div', class_='nbl-poster__propertiesRow').text
    print(link, name, genre, marks, sep='\n')



#one_film()

def all_films():
    url = 'https://www.ivi.ru/movies/2022/page1?rating_model=ready&rating_part=main&sort=ivi'
    r = requests.get(url).text

    #with open('projects.html', 'w') as file:
        #file.write(r)

    with open('projects.html') as file:
        src = file.read()

    soup = BeautifulSoup(r, 'lxml')

    films = soup.findAll('li', class_='gallery__item gallery__item_virtual')

    data = []

    for film in films:
        link = 'https://www.ivi.ru/' + film.find('a').get('href')
        name = film.find('div', class_='nbl-slimPosterBlock__title').find('span').text
        genre = film.find('div', class_='nbl-poster__propertiesInfo').find('div').text
        marks= film.find('div', class_='nbl-poster__propertiesRow').text
        data.append(['ссылка:', link, name, 'жанр:', genre, 'оценка:', marks])

    for i in range(len(data)):
        print(data[i], sep='\n')

all_films()