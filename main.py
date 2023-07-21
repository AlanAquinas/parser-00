import requests
from bs4 import BeautifulSoup as BS

films = soup.find_all('div', class_="styles_content__nT2IG")
 
data = []
 
for film in films:
    title = film.find("span", class_ = "styles_activeMovieTittle__kJdJj").text
    link = "https://www.kinopoisk.ru"+film.find('a', class_="base-movie-main-info_link__YwtP1").get('href')
    original_name = film.find('div', class_='desktop-list-main-info_secondaryTitleSlot__mc0mI').find('span').text
    rating = film.find('div', class_='styles_kinopoiskValueBlock__qhRaI').find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg styles_top250Type__mPloU').text
    rating_count = film.find('span', class_='styles_kinopoiskCount__2_VPQ').text
 
    data.append([title, original_name, link, rating, rating_count])
 