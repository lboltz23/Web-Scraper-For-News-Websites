from module_1.web_scrape import Website_Scraper #importing module one and all the classes inside
from module_2.file_scrape import Write_File #importing module two and all the classes inside

def main():
    urls = []   #creating a new array or list
    urls = open('urls.txt', 'r').read().split('\n') #reading in each url from urls.txt, line by line and storing them into a list

    web_scrape = Website_Scraper()  #creating an instance of the Website_Scraper() class
    file_scrape = Write_File()  #creating an instance of the Write_File() class


    #Iterating over the list of urls in urls
    for index, url in enumerate(urls):

        data = web_scrape.website_scrape(url)   #scraping the website using the Website_Scraper() instance and storing the data returned
        file_scrape.write_rawfile(index, data)  #writing all the data besides the body into the raw file using the Write_File() instance
        file_scrape.write_processedfile(index, data['body']) #writing the body content into the processed file using the Write_File() instance


if __name__ == "__main__":
    main()