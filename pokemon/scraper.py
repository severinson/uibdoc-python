import os.path
import requests
import random

from pokemon import Pokemon
from bs4 import BeautifulSoup

def get_html(refresh=False,
             path='./pokemon.html',
             url='https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number'):

    # return a cached result
    if os.path.exists(path) and not refresh:
        with open(path) as f:
            return f.read()

    # query a new result
    resp = requests.get(url)
    with open(path, 'w') as f:
        f.write(resp.text)
    return resp.text

def get_pokemon():

    # get html page
    html = get_html()
    print('got {} chars of html'.format(len(html)))

    # create soup object for parsing the html
    soup = BeautifulSoup(html)

    pokemons = list()

    for tr in soup.find_all('tr', style='background:#FFF'):
        tds = tr.find_all('td')
        name = tds[2].find('a')['title']
        types = [td.find('a')['title'].strip(' (type)') for td in tds[4:]]
        pokemons.append(Pokemon(
            name=name,
            types=types,
            max_hp=random.randint(1, 100),
            strength=random.randint(1, 40),
        ))
    return pokemons

if __name__ == '__main__':
    pokemons = get_pokemon()
    for pokemon in pokemons:
        print(pokemon)
