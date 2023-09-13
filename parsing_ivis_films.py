from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


data = []
browser = Chrome('/Users/Eugeniy/Desktop/chromedriver')
#url = 'https://www.ivi.ru/movies/2022?rating_model=ready&rating_part=main&sort=ivi'
url = "https://www.ivi.ru/movies/2022/page1"
browser.get(url)
sleep(1)

while True:
    find_element = browser.find_element(By.CLASS_NAME, 'nbl-poster__properties')

    if browser.find_elements(By.CLASS_NAME, 'nbl-slimPosterBlock__titleText'):
        with open('html_ivi', 'w') as file:
            file.write(browser.page_source)
            break
    else:
        actions = ActionChains(browser)
        actions.move_to_element(find_element).perform()
        sleep(3)

with open('html_ivi', 'r') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
films = soup.findAll('div', class_='gallery__item gallery__item_virtual')

data = []

for film in films:
    link = 'https://www.ivi.ru/' + film.find('a').get('href')
    name = film.find('div', class_='nbl-slimPosterBlock__title').find('span').text
    genre = film.find('div', class_='nbl-poster__propertiesInfo').find('div').text
    marks = film.find('div', class_='nbl-poster__propertiesRow').text
    data.append(['ссылка:', link, name, 'жанр:', genre, 'оценка:', marks])
print(data)


