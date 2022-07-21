# расписание 88 автобуса
import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://busti.me/volgograd/bus-88EE/?hl=ru")
soup = bs(r.text, "html.parser")

my_divs = soup.find_all("div", {"class": "labels"})

start = my_divs[0].find_all("div", {"class": "label"})
end = my_divs[1].find_all("div", {"class": "label"})

count = len(start) if len(start) > len(end) else len(end)

print("Покупочка")

for div in start:
    print(div.text)

print("Вокзал")

for div in end:
    print(div.text)
