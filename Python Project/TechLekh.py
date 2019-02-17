from bs4 import BeautifulSoup
import requests



url="https://techlekh.com/"
page=requests.get(url)
soup=BeautifulSoup(page.content, 'html.parser')



techlekh = soup.find_all('a')
techlekh
f = open("techlekh.txt", "a")

for each in techlekh:
    f.write(each.text + "\n")