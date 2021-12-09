from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.ipl.org/essay/Essay-On-Trout-Fishing-FJ9L5UVYVG').text

soup = BeautifulSoup(source, "html.parser")

match = soup.div.text

print(match)





