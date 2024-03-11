#The open/closed principle is used here to define an interface for writing the data to a file, there are two abstract methods defined, each to be used in the class to write to a certain file, either processed or raw
#This code is open for extension and closed for modification, by allowing the user to add new functionalies by implementing new subclasses without modifying the exisitng abstract methods defined in the FileWrite class
#inputs the data from the urls and outputs raw and processed files containing the data
#The benefit of using the open/closed principle is that if the user needed to implement different functionalities to the abstract methods they can just create a new subclasses to the interface without modifying the old code
from abc import ABC, abstractmethod
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
    
    def write_processedfile(self, index, body):
        with open(f'data/processed/{index}_processed.txt', 'w') as f: #writing just the body information to the processed file
            f.write(body + '\n\n')   