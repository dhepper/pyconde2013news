import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://2013.de.pycon.org/konferenz/neuigkeiten/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content)
    news = [e.get_text() for e in soup.find(id='content-main').find_all('h2')]
    for n in news:
        print n


if __name__ == '__main__':
    main()
