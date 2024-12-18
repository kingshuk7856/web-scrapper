import requests
from bs4 import BeautifulSoup

response= requests.get("https://en.wikipedia.org/wiki/MS_Dhoni")
soup=BeautifulSoup(response.text,"html.parser")

print(soup.title.text)