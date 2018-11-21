import requests
from bs4 import BeautifulSoup
import json
import csv
import os
req = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=wed')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

webtoons = soup.select(
    '#content > div.list_area.daily_img > ul > li > dl > dt > a'
    )

data = {}

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

for title in webtoons:
  data[title.text] = title.get('href')
  
with open(os.path.join(CURRENT_DIR, 'result.json'), 'w+') as json_file:
  json.dump(data, json_file)

json_file.close()

jsonfile = open('result.json','r')
json_data = json.load(jsonfile)
#print(json_data)

csvfile = open(file='wed_webtoon.csv',mode='w',newline='', encoding='euc_kr')
csvwriter = csv.writer(csvfile)

count = 0

for key in json_data:
      if count == 0:
             csvwriter.writerow(["TITLE", "LINK"])
             count += 1
      #print(key+json_data[key])
      csvwriter.writerow([key, json_data[key]])

jsonfile.close()

