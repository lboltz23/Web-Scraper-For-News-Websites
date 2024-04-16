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
* Install Miniconda
* Create a conda environment after installing Miniconda 
* Install the BeautifulSoup package in the terminal
* Install the Requests package in the terminal
## How to use:
* Copy and paste desired news article urls in the urlsfile.txt
* In the terminal activate your conda environment with the packages, BeautifulSoup and Requests, installed
* Then in the terminal type: python web_scraper.py
* You should receive an output of files containing each article being scraped and organized
## Connecting to an AI to generate a summary of the news article using OpenAI
### Setup OpenAI account
* Create an account through OpenAI or sign in
* Then after signing in, find the API key page
* Click "Create new secret key"
### Connect with python
* To connect with Python, if not already installed, download python
* Then set up a virtual environment using miniconda
* After in the virtual environment install the OpenAI python library:
  ```
  pip install --upgrade openai
  ```
* Since the code also utilizes a .env file the python-dotenv package also needs to be installed in the environment
  ```
  pip install python-dotenv
  ```
  
### Setup API key for project
* First create a .env file in the root of your project directory
* Setting your API key to an environment variable here allows for seamless committing and pushing in the future as you cannot push files with the secret key inside unless done this way
* Then create a .gitignore file and insert the .env file inside:
```
.env
```
*Inside the .env file set a global variable to the secret key:
```
OPENAI_PROJECT_KEY: thekey
```
### Use API key in code file
* Import the openai module and os to use in the file
```
from openai import OpenAI
import os
```
* Then import python-dotenv to be able to use the .env file in python
  ```
  from dotenv import load_dotenv
  ```
* Then the environment variables need to be loaded from .env
  ```
  load_dotenv()
  ```
* To access the actual key the statement will look like this:
  ```
  api_key = os.envrion['KEY_NAME']
  ```
### To generate a response
* First you need to use the openai module to initialize the key
  ```
  openai.api_key = api_key
  ```
* Then using the ChatCompletions module you can send a prompt to OpenAI using the API key and in return get a response from the AI
  ```
  summary = openai.chat.completions.create(
    module = "gpt-3.5-turbo",
    messages = ["role": "user", "content": "whatever question or prompt"],)
  return summary.choices[0].message.content
  ```
  ## Test issues
  ### Checking the URLs provided in the urlsfile.txt
  ### There are three possibilities:
  * No URL given: there are no URLs in the text file
  * Invalid URL: the URL cannot be located
  * Incompatible URL: the URL is not able to be scraped because the scraper cannot find proper tags in the HTML code
  #### Using a Try-Except statement to test for either an attribute error or an exception error
  ```
  try:
      data = web_scrape.website_scrape(url)   #scraping the website using the Website_Scraper() instance and storing the data returned
  except AttributeError as e:
      print("could not retrieve data because of unknown url", e) #prints could not retrieve data because of unknown url and the error
  except Exception as err:
      if url == "":
          print("no url", err) #prints no url and the error given
      elif url !="":
          print("invalid url", err) #prints invalid url and the error given
  ```
  ##### The statement will print out an error statement with the corresponding error output
  
  ### Checking if the title can be scraped from the article in web_scrape.py
  #### Using a Try-Except statement that is implemented in the method website_scrape()
  ```
  try:
      titles = soup.find('h1', class_="headline__text inline-placeholder").text
        
  except AttributeError as err: #prints out attribute error if the html tag could not be found
      print("could not find title in article", err)
  ```
  ##### The statement checks if the header HTML tag can be found in the article's HTML and prints out an error statement if it cannot be found

  ### Checking if the body paragraphs can be scraped from the article in web_scrape.py
  #### Using a Try-Except statement that is implemented in the method website_scrape()
  ```
  try:
      body_information = soup.find_all('p', class_="paragraph inline-placeholder")
        
  except AttributeError as err: #prints out attribute error if html paragraph tag can not be found in article
      print("could find body information", err)
  ```
  ##### The statement checks if the paragraph HTML tag can be found in the article's HTML and prints out an error statement if it cannot be found

  ### Checking if there are the proper files in data/raw after scraping the article
  #### Calling the method in run.py
  ```
  file_scrape.test_raw_file_write()
  ```
  #### The method in the class Write_File() that is used to test if there are the expected raw files
  ```
  def test_raw_file_write(self):
        """Test raw file writing."""
        try:
            # Check if the data/raw directory exists
            if not os.path.exists('data/raw'):
                print("The data/raw directory does not exist.")
                return
            # Get a list of files in the data/raw directory
            files = os.listdir('data/raw')
            # if no files return
            if not files:
                print("No files found in the data/raw directory.")
                return
            # Check if files have content
            for file in files:
                with open(os.path.join('data/raw', file), 'r') as f:
                    content = f.read()
                    if not content:
                        print(f"The file {file} in data/raw is empty.")
                    else:
                        print(f"The file {file} in data/raw contains data.")
        #  throw error if needed
        except IOError as e:
            print(f"Error testing raw file write: {e}")
   ```
  ##### The method checks three events that could occur. The first is checking if the directory path data/raw exists. The second checks if there are files in raw. Lastly, it checks if there is content in the files. An IOError is thrown if any of those fail which includes a print statement. 

### Checking if there are the proper files in data/processed after scraping the article
  #### Calling the method in run.py
  ```
  file_scrape.test_processed_file_write()
  ```
  #### The method in the class Write_File() that is used to test if there are the expected processed files
  ```
  def test_processed_file_write(self):
        """Test processed file writing."""
        try:
            # Check if the data/processed directory exists
            if not os.path.exists('data/processed'):
                print("The data/processed directory does not exist.")
                return
            # Get a list of files in the data/processed directory
            files = os.listdir('data/processed')
            # if no files return
            if not files:
                print("No files found in the data/processed directory.")
                return
            # Check if files have content
            for file in files:
                with open(os.path.join('data/processed', file), 'r') as f:
                    content = f.read()
                    if not content:
                        print(f"The file {file} in data/processed is empty.")
                    else:
                        print(f"The file {file} in data/processed contains data.")
        #  throw error if needed
        except IOError as e:
            print(f"Error testing processed file write: {e}")
   ```
  ##### The method checks three events that could occur. The first is checking if the directory path data/processed exists. The second checks if there are files in processed. Lastly, it checks if there is content in the files. An IOError is thrown if any of those fail which includes a print statement. 

### Checking if there are the proper files in data/summary after scraping the article and getting an API response
  #### Calling the method in run.py
  ```
  summary.test_summary_files() # tests summary files
  ```
  #### The method in the class Write_Summary() that is used to test if there are the expected summary files
  ```
  def test_summary_files(self):
        """Test summary files."""
        try:
            # Check if the data/summary directory exists
            if not os.path.exists('data/summary'):
                print("The data/summary directory does not exist.")
                return

            # Get a list of files in the data/summary directory
            files = os.listdir('data/summary')

            if not files:
                print("No files found in the data/summary directory.")
                return

            # Check if files are empty
            for file in files:
                with open(os.path.join('data/summary', file), 'r') as f:
                    content = f.read()
                    if not content:
                        print(f"The file {file} in data/summary is empty.")
                    else:
                        print(f"The file {file} in data/summary contains data.")
        #  throw error if needed
        except IOError as e:
            print(f"Error testing summary files: {e}")

   ```
  ##### The method checks three events that could occur. The first is checking if the directory path data/summary exists. The second checks if there are files in summary. Lastly, it checks if there is content in the files. An IOError is thrown if any of those fail which includes a print statement. 







