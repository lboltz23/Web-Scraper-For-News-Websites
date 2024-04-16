#Open/Closed Principle is being used by having an interface for webscraper that enforces the abstract method website_scrape, which the class website_scraper must utilize
#The Web_Scrape abstract base class allows for different implementation of the abstract methods in subclasses without having the user modify the existing code
#So this code follows the open for extension and closed for modification principle
#The open/closed principle is helpful because subclasses can be created from the interface without having to modify any of the existing code, so if the website needs to be scraped in a difference way the interface can be used with a different functionality without modification of previous code
#For example if the user only wanted to scrape the author data and body paragraph data, they can without changing the interface
from bs4 import BeautifulSoup
import requests
import json
from abc import ABC, abstractmethod

#defining the abstract base class Web_Scrape for web scraping 
class Web_Scrape(ABC):
    #defining the abstract method website_scrape for website scraping
    @abstractmethod
    def website_scrape(self, url):
        pass

#defining the concrete class Website_Scraper that uses the Web_Scrape() interface
class Website_Scraper(Web_Scrape):
    def website_scrape(self, url): #implementing the website_scrape method, inputs the url, outputs the data

        #Send a GET request to the specified url and store the response (returns response object containing content, encoding, status,...)
        response = requests.get(url)
        #parses the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        #Extracting the title
        try:
            titles = soup.find('h1', class_="headline__text inline-placeholder").text
        
        except AttributeError as err: #prints out attribute error if the html tag could not be found
            print("could not find title in article", err)
        #Extracting the authors
        authors = soup.find('div', class_='byline__names').text
        #Extracting the timestamp
        timestamp = soup.find('div', class_="timestamp").text
        #Extracting all of the body paragraphs
        try:
            body_information = soup.find_all('p', class_="paragraph inline-placeholder")
        
        except AttributeError as err: #prints out attribute error if html paragraph tag can not be found in article
            print("could find body information", err)
        #Joins all of the body paragraphs into a single string separated by two newlines
        body = '\n\n'.join([information.text for information in body_information])
        #returns an associative array with all the data used for writing to a file
        return {
            'title': titles,
            'author': authors,
            'timestamp': timestamp,
            'body':body
        }


