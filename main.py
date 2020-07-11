import requests
from bs4 import BeautifulSoup
from csv import writer 

log = open("log.txt", "w")

url = 'https://www.uhd.edu/academics/sciences/Pages/sciences-scholarships.aspx'

response = requests.get(url, timeout=20)

soup = BeautifulSoup(response.text, 'html.parser')


section = soup.find('ul', class_='f_standard')

for item in section.find_all('li'):
    item = item.a.text 
    print(item + "\n")
