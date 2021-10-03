import requests
from bs4 import BeautifulSoup
from googlesearch import search


def find_ratings(title):
    query = title + " site=\"imdb.com\""
    urls = search(query)
    for x in urls:
        url = x
        break
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    result = requests.get(url, headers=headers)
    site = BeautifulSoup(result.text, "html.parser")
    number_of_seasons = site.find('label', class_='ipc-simple-select__label').text.split()[0]
    print(number_of_seasons)

    season_urls = []
    for i in range(1,int(number_of_seasons)+1):
        season_urls.append(url + "episodes?season=" + str(i))

    ratings = []
    for urls in season_urls:
        result = requests.get(urls)
        site = BeautifulSoup(result.text, "html.parser")
        rating_divs = site.find_all('div', class_='ipl-rating-star small')
        season_rating = []
        for div in rating_divs:
            season_rating.append(float(div.find('span', class_='ipl-rating-star__rating').text))
        ratings.append(season_rating)
    print(ratings)
