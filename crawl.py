import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.naver.com')
html = req.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')

issues = soup.select(
    '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a'
    )
#print(issues)

for issue in issues:
    print("["+issue.select_one('span[class="ah_r"]').text +"] "+ issue.select_one('span[class="ah_k"]').text)
    
    
