import requests
from bs4 import BeautifulSoup 
from random import randint
a=randint (0,10)

response=requests.get("https://vlg.kinoafisha.info/").text 
soup=BeautifulSoup(response, "lxml") 
film=soup.find_all("a",class_="movieItem_title")
film_ditals=soup.find_all("div",class_="movieItem_details")
print(film[a].text)
print(film_ditals[a].text)