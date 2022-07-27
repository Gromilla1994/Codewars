import requests
import bs4

r = requests.get("https://stopgame.ru/")

soup = bs4.BeautifulSoup(r.text, "html.parser")

my_divs = soup.find_all("div", {"role": "listitem"})

for div in my_divs:
    title = div.find("span", {"class": "_card__title_1u8os_226"})
    print(title.text)
