import openai
import os
from abc import ABC, abstractmethod
#abstract base class
#imports openai module
#initializes instances of class with API key
class Summary(ABC):
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
    #abstract method gets summary from provided content
    @abstractmethod
    def get_summary(self, content):
        pass
    #abstract method that writes summary to file
    @abstractmethod
    def write_files(self, title, data):
        pass
#concrete class Write_Summary, inherits base class Summary
#initializes instance of the class with the API key
class Write_Summary(Summary):
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        #returns summary of 75 words or less from ai response message given the complete article content(prompt)
    def get_summary(self, content):
        prompt = f"Write a summary about this article in 75 words or less:{content}"
        #OpenAI API request to get reponse using the key
        summary = openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": prompt}],
        )
        return summary.choices[0].message.content
    #writes the summary and title of the article to the processed file folder in data
    #the index, title, and summary is passed through the method
    def write_files(self, index, title, data):
        with open(f'data/summary/{index}_summary.txt', 'w') as f: #writing just the body information to the processed file
            #splits the summary into sentences alone to then write to file
            f.write(title +'\n\n')
            for line in data.split('.'):
                #if the line is not empty, write to the file
                if line.strip():
                    f.write(line.strip() + '.' + '\n\n')   
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
