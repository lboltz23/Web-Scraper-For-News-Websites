# Web Scraper for News Articles
### This repository contains a web scraper, coded in Python, that can take any URL from a news website and output a file containing the article, without all of the ads or unnecessary parts included. 
## How the web scraper works
* The file labeled web_scraper.py reads the URLs in the text file, urlsfile.txt, and puts each into an array. 
* Then the program runs a for loop to enumerate each URL in the array.
* Each URL is first checked to be valid using the response.get method
* Then the HTML markup of the website is parsed and set to a variable using the BeautifulSoup constructor
* In the next lines of the for loop, using soup.find().text and knowledge of HTML tags, the *program can search through the markup, find the text in that tag, and write it to the output file
## Dependencies
* Install Python programming language
* Create a conda environment by installing Miniconda 
* Install the BeautifulSoup package 
* Install the Requests package

