import requests
from bs4 import BeautifulSoup as bs

r=requests.get("https://flappybird.gg/")
print(r.status_code) # if 200 then request was successful !
soup=bs(r.content, "html.parser")

s=soup.prettify()
# content = soup.find_all('container', class_='container')

print(soup.find_all('game'))