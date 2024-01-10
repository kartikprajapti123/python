import zipfile

# working with fils in python 
with open("content.txt","w+") as f:
    f.write("hello kartik this is very good")
    f.write("hello this is our message from bca class")
    
    f.write("")
    # this will empty the file 
    
    f.close()

# this is file using json read in python
import json

with open("xyz.json","r") as js:
    data=json.load(js)

print(data)    
    


# this is used for unzip the zipfile    
def zip(zip_file_path,extract_to):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)



zip_file_path = 'zipping.zip'
extract_to_directory = ''
zip(zip_file_path,extract_to_directory)


# this is file openeing using csv 
import csv

def read_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            print(i)
        # Iterate through rows in the CSV file
# Example usage:
csv_file_path = 'test.csv'
read_csv(csv_file_path)

