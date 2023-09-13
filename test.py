import pandas as pd
import requests
from bs4 import BeautifulSoup


def all_films():
    count = 0
    data = []
    for page in range(1, 7):
        url = f'https://www.ivi.ru/movies/2022/page{page}?rating_model=ready&rating_part=main&sort=ivi'
        r = requests.get(url).text


        #with open('projects.html', 'w') as file:
            #file.write(r)

        with open('projects.html') as file:
            src = file.read()

        soup = BeautifulSoup(r, 'lxml')

        films = soup.findAll('li', class_='gallery__item gallery__item_virtual')



        for film in films[count:]:
            try:
                link = 'https://www.ivi.ru/' + film.find('a').get('href')
            except:
                link = ''
            try:
                name = film.find('div', class_='nbl-slimPosterBlock__title').find('span').text
            except:
                name = '-'
            try:
                genre = film.find('div', class_='nbl-poster__propertiesInfo').find('div').text
            except:
                genre = '-'
            try:
                marks = film.find('div', class_='nbl-poster__propertiesRow').text
            except:
                marks = '-'
            data.append([link, name, genre, marks])
            count += 1

    headers = ['link', 'name', 'genre', 'marks']
    df = pd.DataFrame(data, columns=headers)
    df.to_excel(excel_writer='/Users/Eugeniy/Document/ivis_films.xlsx')


all_films()
