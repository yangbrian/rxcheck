__author__ = 'Brian'

from bs4 import BeautifulSoup
import requests, csv

def saveToDatabase(data):
    #Connect to mongodb client
    client = MongoClient('localhost', 27017)

    #Get the database
    db = client.rxcheck

    #Get the collection
    collection = db.conditions

    #Save a new document into the collection
    collection.insert_one(data)

url = 'https://rarediseases.info.nih.gov/gard/browse-by-first-letter/Z'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
diseaseList = []
superstring = ''

for listItem in soup.find_all("td", class_="DiseaseList"):
    string = listItem.text
    string = '\'' + string[:string.find(' - ')].strip() + '\', '
    diseaseList.append(string)
    superstring += string

with open('test', 'a') as myfile:
    myfile.write(superstring)