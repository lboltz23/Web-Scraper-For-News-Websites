from bs4 import BeautifulSoup
import requests

urls = []

urls = open('urlsfile.txt', 'r').read().split('\n')

for index, url in enumerate(urls):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    with open(f'{index}.txt', 'w') as f:

        titles = soup.find('h1', class_="headline__text inline-placeholder").text
        f.write(titles)

        authors = soup.find('div', class_='byline__names').text
        f.write(authors)

        timestamp = soup.find('div', class_="timestamp").text
        f.write(timestamp)

        body_information = soup.find_all('p', class_="paragraph inline-placeholder")
        for information in body_information:
            f.write(f'{information.text} \n \n')

