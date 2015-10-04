__author__ = 'Brian'

from bs4 import BeautifulSoup
from string import ascii_lowercase
import requests

url = 'https://rarediseases.info.nih.gov/gard/browse-by-first-letter/'

for c in ascii_lowercase:
    r = requests.get(url + c)
    soup = BeautifulSoup(r.text, 'html.parser')
    diseaseList = []
    superstring = ''

    for listItem in soup.find_all("td", class_="DiseaseList"):
        string = listItem.text
        string = '\"' + string[:string.find(' - ')].strip() + '\", '
        diseaseList.append(string)
        superstring += string

    with open('test', 'a') as myfile:
        myfile.write(superstring)