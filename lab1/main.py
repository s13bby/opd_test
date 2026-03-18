#Вычислить данные о погоде в Омске за февраль, результат записать в файл
import requests
from bs4 import BeautifulSoup

def parse():
    file = open('Погода февраль Омск.txt', 'w')
    url = "https://pogoda.365c.ru/russia/omsk/m/february"
 
    response = requests.get(url)
    content = BeautifulSoup(response.text, 'html.parser')
    date = [date.get_text(strip=True) for date in content.find_all("td", class_="d-name")]
    temp_day = [temp_day.get_text(strip=True) for temp_day in content.find_all("td", class_="d-temp")]
    temp_night = [temp_day.get_text(strip=True) for temp_day in content.find_all("td", class_="d-temp4")]
    file.write("Ферваль\n")
    for index in range(len(temp_day)):
        file.write(f"Дата: {date[index]} {date[0]}\n")
        file.write(f"Температура днем: {temp_day[index]}\n")
        file.write(f"Температура ночью: {temp_night[index]}\n\n")

if __name__ == '__main__':
    parse()
