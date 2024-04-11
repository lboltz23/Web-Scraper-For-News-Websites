#The open/closed principle is used here to define an interface for writing the data to a file, there are two abstract methods defined, each to be used in the class to write to a certain file, either processed or raw
#This code is open for extension and closed for modification, by allowing the user to add new functionalies by implementing new subclasses without modifying the exisitng abstract methods defined in the FileWrite class
#inputs the data from the urls and outputs raw and processed files containing the data
#The benefit of using the open/closed principle is that if the user needed to implement different functionalities to the abstract methods they can just create a new subclasses to the interface without modifying the old code
#For example if they wanted to just have the author and body paragraphs in the processed file they can do that without changing the interface
from abc import ABC, abstractmethod
import os
#Create an abstract base class for writing to files
class FileWrite(ABC):
    #defining the abstract method for writing raw data to a file
    @abstractmethod
    def write_rawfile(self, index, data):
        pass
    #defining the abstract method for writing processed data to a file
    @abstractmethod
    def write_processedfile(self, index, body):
        pass
#creating a concrete class that implements the FileWrite interface  
class Write_File(FileWrite):    
    def write_rawfile(self, index, data):
        with open(f'data/raw/{index}raw.txt', 'w') as f: #writing the title,author, timestamp, and body to the raw file
            f.write(data['title'] + '\n\n')
            f.write(data['author']+ '\n\n')
            f.write(data['timestamp']+ '\n\n')
            f.write(data['body'] + '\n\n')
    
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

        except IOError as e:
            print(f"Error testing raw file write: {e}")

    def write_processedfile(self, index, body):
        with open(f'data/processed/{index}_processed.txt', 'w') as f: #writing just the body information to the processed file
            f.write(body + '\n\n')  

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

        except IOError as e:
            print(f"Error testing processed file write: {e}")
