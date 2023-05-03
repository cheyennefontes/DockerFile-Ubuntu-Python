import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', class_='chart')

    titles = []
    for row in table.find_all('tr'):
        title_column = row.find('td', class_='titleColumn')
        if title_column:
            title = title_column.find('a').text
            titles.append(title)

    sorted_titles = sorted(titles)

    for i, title in enumerate(sorted_titles, 1):
        print(f"{i}. {title}")
else:
    print("Falha na requisição HTTP")
