#Вычислить данные о погоде в Омске за февраль, результат записать в файл
import requests
from bs4 import BeautifulSoup

def parse():
    file = open('Погода февраль Омск.txt', 'w')
    url = 'https://omsk.nuipogoda.ru/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BD%D0%B0-%D1%84%D0%B5%D0%B2%D1%80%D0%B0%D0%BB%D1%8C'
    times = []
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    block = soup.find_all('td')

    for td in block:
        if td.has_attr('time'):
            times.append(td)

    for index in times:
        if index.find('span', class_='month'):
            month = "Месяц: " + index.find('span', class_='month').text
        else:
            month = ''

        date = index.find('span', class_='number').text

        if index.find('div', class_='i'):
            weather = index.find('div', class_='i').get('title')
        else:
            weather = ''

        day_temp = index.find('span', class_='max').text
        night_temp = index.find('span', class_='min').text

        file.write(f"{month}\n")
        file.write(f"Дата: {date}\n")
        file.write(f"Погода: {weather}\n")
        file.write(f"Температура днем: {day_temp}\n")
        file.write(f"Температура ночью: {night_temp}\n")

def main():
    parse()

if __name__ == '__main__':
    main()