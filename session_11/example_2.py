import requests
from bs4 import BeautifulSoup

r = requests.get('https://divar.ir/s/tehran/rent-residential/abshar?credit=-700000000&rent=-20000000&sort=sort_date')

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.find('div', {'class': 'kt-post-card__description'}).text)

