from module_1.web_scrape import Website_Scraper #importing module one and all the classes inside
from module_2.file_scrape import Write_File #importing module two and all the classes inside
from module3.chatgpt import Write_Summary 
from dotenv import load_dotenv
import os
from openai import OpenAI


def main():
    urls = []   #creating a new array or list
    urls = open('urls.txt', 'r').read().split('\n') #reading in each url from urls.txt, line by line and storing them into a list
    load_dotenv()

    api_key = os.environ['WEB_API_KEY']
    web_scrape = Website_Scraper()  #creating an instance of the Website_Scraper() class
    file_scrape = Write_File()  #creating an instance of the Write_File() class
    
    summary = Write_Summary(api_key)

    #Iterating over the list of urls in urls
    for index, url in enumerate(urls):
        try:
            data = web_scrape.website_scrape(url)   #scraping the website using the Website_Scraper() instance and storing the data returned
        except AttributeError as e:
            print("could not retreive data because of unknown url", e)
        except Exception as err:
            if url == "":
                print("no url", err)
            elif url !="":
                print("invalid url", err)
        else:       
            file_scrape.write_rawfile(index, data)  #writing all the data besides the body into the raw file using the Write_File() instance
            file_scrape.write_processedfile(index, data['body']) #writing the body content into the processed file using the Write_File() instance
            file_scrape.test_raw_file_write()       # tests raw files
            file_scrape.test_processed_file_write() #Tests processed files
            try: #try to get summary
                Summary = summary.get_summary(data['body'])
            except Exception as e: #if not able to get summary throw error
                print("Error getting summary:", e)
            else: # if able to get summary write it to file, then test if it is in file
                summary.write_files(index, data['title'], Summary)
                summary.test_summary_files() # tests summary files
            
if __name__ == "__main__":
    main()