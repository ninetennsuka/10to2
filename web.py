import requests
from bs4 import BeautifulSoup

URLS = [
    'https://lenta.ru/',
    'https://www.rbc.ru/'
]

def fetch_headlines(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = []
    if 'lenta.ru' in url:
        for tag in soup.select('section span.card-mini__title'):
            headlines.append(tag.text.strip())
    elif 'rbc.ru' in url:
        for tag in soup.select('a.news-feed__item__title'):
            headlines.append(tag.text.strip())
    return headlines

def main():
    all_headlines = {}
    for url in URLS:
        try:
            print(f"\n*** Новости {url} ***")
            headlines = fetch_headlines(url)
            all_headlines[url] = headlines
            for i, h in enumerate(headlines, 1):
                print(f"{i}. {h}")
        except Exception as e:
            print(f"Ошибка получения с {url}: {e}")

if __name__ == '__main__':
    main()
