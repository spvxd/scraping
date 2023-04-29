import requests
from bs4 import BeautifulSoup as BS
stroka = "Сегодня"
page = 1
file = open('parse.txt', 'w', encoding='utf-8')
while True:
    r = requests.get(
        "https://stopgame.ru/news/all/p" + str(page))
    html = BS(r.content, 'html.parser')
    items = html.select(".items > .article-summary")


    if len(items):
        for el in items:
            title = el.select(".article-description > .caption > a")
            date = el.select(".article-description > .info > .timestamp")

            print("Название обзора:", title[0].text)
            if date == stroka:
                print("Дата:", date[0].text)
            else:
                print(date[0].text)
            file.write(str(title[0]))
            print("------------------------")
        page += 1
    else:
        break
