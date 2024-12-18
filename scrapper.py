import requests
from bs4 import BeautifulSoup

response = requests.get("https://wikipedia.com")
soup = BeautifulSoup(response.text, "html.parser")

print(type(soup) )
